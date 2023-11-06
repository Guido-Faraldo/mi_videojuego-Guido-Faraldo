import sys
import pygame
from constantes import *
from Clases.texto import Texto
from mis_objetos import *
from mis_funciones import *

pygame.init()
aplicar_gravedad = True
realizar_salto = False
salto_desde_plataforma = False
salto_desde_primer_piso = False
salto_desde_segundo_piso = False
salto_desde_tercer_piso = False
img_luchador = 0
ruta_luchador = lista_luchador_caminando_derecha[img_luchador]
contador_manzanas = 0
direccion_escorpion_1 = "Derecha"
direccion_escorpion_2 = "Derecha"
direccion_escorpion_3 = "Derecha"
direccion_escorpion_4 = "Derecha"
ruta_escorpion_1 = RUTAS_ESCORPION[0]
ruta_escorpion_2 = RUTAS_ESCORPION[0]
ruta_escorpion_3 = RUTAS_ESCORPION[0]
ruta_escorpion_4 = RUTAS_ESCORPION[0]

SCREEN = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA)) #800, 600
pygame.display.set_caption("Mi Videojuego")

FUENTE_VIDAS = pygame.font.SysFont("Arial", 45)
FUENTE_MANZNAS_COMIDAS = pygame.font.SysFont("Arial", 35)
texto_vidas = Texto("VIDAS:", COLOR_ROJO, POS_TEXTO_VIDAS, FUENTE_VIDAS)
texto_manzanas_comidas = Texto(F"MANZANAS COMIDAS: {contador_manzanas}", COLOR_ROJO, POS_TEXTO_MANZANAS_COMIDAS, FUENTE_MANZNAS_COMIDAS)

while True:
    lista_teclas = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or lista_teclas[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

    luchador = Luchador(ruta_luchador, TAMAÑO_LUCHADOR, POS_LUCHADOR)

    texto_manzanas_comidas = Texto(F"MANZANAS COMIDAS: {contador_manzanas}", COLOR_ROJO, POS_TEXTO_MANZANAS_COMIDAS, FUENTE_MANZNAS_COMIDAS)
    escorpion_1 = Escorpion(ruta_escorpion_1, TAMAÑO_ESCORPION, POS_ESCORPION_1)
    escorpion_2 = Escorpion(ruta_escorpion_2, TAMAÑO_ESCORPION, POS_ESCORPION_2)
    escorpion_3 = Escorpion(ruta_escorpion_3, TAMAÑO_ESCORPION, POS_ESCORPION_3)
    escorpion_4 = Escorpion(ruta_escorpion_4, TAMAÑO_ESCORPION, POS_ESCORPION_4)

    if luchador.rec.colliderect(piso_plataforma.rec):
        aplicar_gravedad = False
    elif ((luchador.rec.x >= 185) and (luchador.rec.x <= 405)) and ((luchador.rec.y >= 360) and (luchador.rec.y <= 370)):
        aplicar_gravedad = False
    elif ((luchador.rec.x >= 610) and (luchador.rec.x <= 830)) and ((luchador.rec.y >= 360) and (luchador.rec.y <= 370)):
        aplicar_gravedad = False
    elif ((luchador.rec.x >= 15) and (luchador.rec.x <= 160)) and ((luchador.rec.y >= 220) and (luchador.rec.y <= 230)):
        aplicar_gravedad = False
    elif ((luchador.rec.x >= 425) and (luchador.rec.x <= 570)) and ((luchador.rec.y >= 220) and (luchador.rec.y <= 230)):
        aplicar_gravedad = False
    elif ((luchador.rec.x >= 835) and (luchador.rec.x <= 980)) and ((luchador.rec.y >= 220) and (luchador.rec.y <= 230)):
        aplicar_gravedad = False
    elif ((luchador.rec.x >= 185) and (luchador.rec.x <= 405)) and ((luchador.rec.y >= 70) and (luchador.rec.y <= 80)):
        aplicar_gravedad = False
    elif ((luchador.rec.x >= 610) and (luchador.rec.x <= 830)) and ((luchador.rec.y >= 70) and (luchador.rec.y <= 80)):
        aplicar_gravedad = False
    else:
        aplicar_gravedad = True

    print(luchador.rec.x)

    if lista_teclas[pygame.K_LEFT]:
        luchador.mover_izquierda()

    if lista_teclas[pygame.K_RIGHT]:
        luchador.mover_derecha()

    if lista_teclas[pygame.K_UP]:
        if luchador.posicion[1] > 460 and luchador.posicion[1] < 480:
            realizar_salto = True
            aplicar_gravedad = False
            salto_desde_plataforma = True
        elif ((((luchador.rec.x >= 185) and (luchador.rec.x <= 405)) and ((luchador.rec.y >= 360) and (luchador.rec.y <= 370))) or 
        (((luchador.rec.x >= 610) and (luchador.rec.x <= 830)) and ((luchador.rec.y >= 360) and (luchador.rec.y <= 370)))):
            realizar_salto = True
            aplicar_gravedad = False
            salto_desde_primer_piso = True
            salto_desde_plataforma = False
        elif ((((luchador.rec.x >= 15) and (luchador.rec.x <= 160)) and ((luchador.rec.y >= 220) and (luchador.rec.y <= 230))) or 
        (((luchador.rec.x >= 425) and (luchador.rec.x <= 570)) and ((luchador.rec.y >= 220) and (luchador.rec.y <= 230))) or 
        (((luchador.rec.x >= 835) and (luchador.rec.x <= 980)) and ((luchador.rec.y >= 220) and (luchador.rec.y <= 230)))):
            realizar_salto = True
            aplicar_gravedad = False
            salto_desde_segundo_piso = True
            salto_desde_primer_piso = False
            salto_desde_plataforma = False
        elif ((((luchador.rec.x >= 185) and (luchador.rec.x <= 405)) and ((luchador.rec.y >= 70) and (luchador.rec.y <= 80))) or 
                (((luchador.rec.x >= 610) and (luchador.rec.x <= 830)) and ((luchador.rec.y >= 70) and (luchador.rec.y <= 80)))):
            realizar_salto = True
            aplicar_gravedad = False
            salto_desde_tercer_piso = True
            salto_desde_segundo_piso = False
            salto_desde_primer_piso = False
            salto_desde_plataforma = False
        
    if salto_desde_plataforma == True and luchador.posicion[1] < 340:
        aplicar_gravedad = True
        realizar_salto = False

    if salto_desde_primer_piso == True and luchador.posicion[1] < 190:
        aplicar_gravedad = True
        realizar_salto = False

    if salto_desde_segundo_piso == True and luchador.posicion[1] < 10:
        aplicar_gravedad = True
        realizar_salto = False

    if salto_desde_tercer_piso == True and luchador.posicion[1] < -100:
        aplicar_gravedad = True
        realizar_salto = False


    if aplicar_gravedad:
        luchador.mover_abajo()

    if realizar_salto:
        luchador.mover_arriba()


    if lista_teclas[pygame.K_SPACE]:
        ruta_luchador = "IMAGENES\patadaDerecha3.png"

    if lista_teclas[pygame.K_f]:
        ruta_luchador = "IMAGENES\puñoDerecha2.png"


    # Colision manzanas
    contador_manzanas = verificar_colison_manzanas(luchador, contador_manzanas, manzana_1)
    contador_manzanas = verificar_colison_manzanas(luchador, contador_manzanas, manzana_2)
    contador_manzanas = verificar_colison_manzanas(luchador, contador_manzanas, manzana_3)
    contador_manzanas = verificar_colison_manzanas(luchador, contador_manzanas, manzana_4)
    contador_manzanas = verificar_colison_manzanas(luchador, contador_manzanas, manzana_5)
    contador_manzanas = verificar_colison_manzanas(luchador, contador_manzanas, manzana_6)
    contador_manzanas = verificar_colison_manzanas(luchador, contador_manzanas, manzana_7)
    
    
    # Movimineto escorpiones
    var = escorpion_1.mover_escorpiones(direccion_escorpion_1, LIMITE_ESCORPION_1_IZQ, LIMITE_ESCORPION_1_DER, RUTAS_ESCORPION)
    ruta_escorpion_1 = var[0]
    direccion_escorpion_1 = var[1]
    var = escorpion_2.mover_escorpiones(direccion_escorpion_2, LIMITE_ESCORPION_2_IZQ, LIMITE_ESCORPION_2_DER, RUTAS_ESCORPION)
    ruta_escorpion_2 = var[0]
    direccion_escorpion_2 = var[1]
    var = escorpion_3.mover_escorpiones(direccion_escorpion_3, LIMITE_ESCORPION_3_IZQ, LIMITE_ESCORPION_3_DER, RUTAS_ESCORPION)
    ruta_escorpion_3 = var[0]
    direccion_escorpion_3 = var[1]
    var = escorpion_4.mover_escorpiones(direccion_escorpion_4, LIMITE_ESCORPION_4_IZQ, LIMITE_ESCORPION_4_DER, RUTAS_ESCORPION)
    ruta_escorpion_4 = var[0]
    direccion_escorpion_4 = var[1]

    fondo.cargar_imagen(SCREEN)
    texto_vidas.mostrar_texto(SCREEN)
    texto_manzanas_comidas.mostrar_texto(SCREEN)
    corazon_1.cargar_imagen(SCREEN)
    corazon_2.cargar_imagen(SCREEN)
    corazon_3.cargar_imagen(SCREEN)
    piso_plataforma.cargar_imagen(SCREEN)
    piso_bloque_grande_1.cargar_imagen(SCREEN)
    piso_bloque_grande_2.cargar_imagen(SCREEN)
    piso_bloque_grande_3.cargar_imagen(SCREEN)
    piso_bloque_grande_4.cargar_imagen(SCREEN)
    piso_bloque_chico_1.cargar_imagen(SCREEN)
    piso_bloque_chico_2.cargar_imagen(SCREEN)
    piso_bloque_chico_3.cargar_imagen(SCREEN)
    manzana_1.cargar_imagen(SCREEN)
    manzana_2.cargar_imagen(SCREEN)
    manzana_3.cargar_imagen(SCREEN)
    manzana_4.cargar_imagen(SCREEN)
    manzana_5.cargar_imagen(SCREEN)
    manzana_6.cargar_imagen(SCREEN)
    manzana_7.cargar_imagen(SCREEN)
    escorpion_1.cargar_imagen(SCREEN)
    escorpion_2.cargar_imagen(SCREEN)
    escorpion_3.cargar_imagen(SCREEN)
    escorpion_4.cargar_imagen(SCREEN)
    luchador.cargar_imagen(SCREEN)

    if lista_teclas[pygame.K_r]:
        manzana_1.dibujar_rectangulo(SCREEN)
        manzana_2.dibujar_rectangulo(SCREEN)
        manzana_3.dibujar_rectangulo(SCREEN)
        manzana_4.dibujar_rectangulo(SCREEN)
        manzana_5.dibujar_rectangulo(SCREEN)
        manzana_6.dibujar_rectangulo(SCREEN)
        manzana_7.dibujar_rectangulo(SCREEN)
        piso_plataforma.dibujar_rectangulo(SCREEN)
        piso_bloque_grande_1.dibujar_rectangulo(SCREEN)
        piso_bloque_grande_2.dibujar_rectangulo(SCREEN)
        piso_bloque_grande_3.dibujar_rectangulo(SCREEN)
        piso_bloque_grande_4.dibujar_rectangulo(SCREEN)
        piso_bloque_chico_1.dibujar_rectangulo(SCREEN)
        piso_bloque_chico_2.dibujar_rectangulo(SCREEN)
        piso_bloque_chico_3.dibujar_rectangulo(SCREEN)
        escorpion_1.dibujar_rectangulo(SCREEN)
        escorpion_2.dibujar_rectangulo(SCREEN)
        escorpion_3.dibujar_rectangulo(SCREEN)
        escorpion_4.dibujar_rectangulo(SCREEN)
        luchador.dibujar_rectangulo(SCREEN)

    pygame.display.flip()












    # if lista_teclas[pygame.K_LEFT]:
    #     ruta_luchador = lista_luchador_caminando_izquierda[img_luchador]
    #     luchador.mover_izquierda()
    #     img_luchador += 1
    #     if img_luchador > len(lista_luchador_caminando_izquierda) - 1:
    #         img_luchador = 0
    # elif lista_teclas[pygame.K_RIGHT]:
    #     ruta_luchador = lista_luchador_caminando_derecha[img_luchador]
    #     luchador.mover_derecha()
    #     img_luchador += 1
    #     if img_luchador > len(lista_luchador_caminando_derecha) - 1:
    #         img_luchador = 0
    # elif lista_teclas[pygame.K_UP]:
    #     luchador.mover_arriba()
    #     ruta_luchador = "IMAGENES\saltoDerecha3.png"
    # elif lista_teclas[pygame.K_DOWN]:
    #     pass
    # else:
    #     if ruta_luchador == lista_luchador_caminando_izquierda[img_luchador]:
    #         ruta_luchador = lista_luchador_caminando_izquierda[0]
    #     else:
    #         ruta_luchador = lista_luchador_caminando_derecha[0]