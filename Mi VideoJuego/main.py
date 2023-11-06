import sys
import pygame
from constantes import *
from Clases.texto import Texto
from mis_objetos import *
from mis_funciones import *

pygame.init()
ultima_tecla = "Derecha"
game_over = False
contador_vidas = 0
aplicar_gravedad = True
realizar_salto = False
salto_desde_plataforma = False
salto_desde_primer_piso = False
salto_desde_segundo_piso = False
salto_desde_tercer_piso = False
img_luchador = 0
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
reloj = pygame.time.Clock()

FUENTE_GRANDE = pygame.font.SysFont("Arial", 45)
FUENTE_CHICA = pygame.font.SysFont("Arial", 35)
texto_vidas = Texto("VIDAS:", COLOR_ROJO, POS_TEXTO_VIDAS, FUENTE_GRANDE)
texto_manzanas_comidas = Texto(f"MANZANAS COMIDAS: {contador_manzanas}", COLOR_ROJO, POS_TEXTO_MANZANAS_COMIDAS, FUENTE_CHICA)
texto_game_over = Texto("GAME OVER", COLOR_AZUL, POS_TEXTO_GAME_OVER, FUENTE_GRANDE)
texto_score = Texto("TU SCORE ES DE:", COLOR_AZUL, POS_TEXTO_SCORE, FUENTE_GRANDE)
texto_score_puntos = Texto(f"{contador_manzanas * 100.00} pts", COLOR_AZUL, POS_TEXTO_SCORE_PUNTOS, FUENTE_GRANDE)
texto_reiniciar = Texto("REINICIAR", COLOR_VERDE, POS_TEXTO_REINICIAR, FUENTE_CHICA)

while True:
    lista_teclas = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or lista_teclas[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
    milis = reloj.tick(60)

    luchador = Luchador(ruta_luchador, TAMAÑO_LUCHADOR, POS_LUCHADOR)

    texto_manzanas_comidas = Texto(F"MANZANAS COMIDAS: {contador_manzanas}", COLOR_ROJO, POS_TEXTO_MANZANAS_COMIDAS, FUENTE_CHICA)
    texto_score_puntos = Texto(f"{contador_manzanas * 100.00} pts", COLOR_AZUL, POS_TEXTO_SCORE_PUNTOS, FUENTE_GRANDE)
    escorpion_1 = Escorpion(ruta_escorpion_1, TAMAÑO_ESCORPION, POS_ESCORPION_1)
    escorpion_2 = Escorpion(ruta_escorpion_2, TAMAÑO_ESCORPION, POS_ESCORPION_2)
    escorpion_3 = Escorpion(ruta_escorpion_3, TAMAÑO_ESCORPION, POS_ESCORPION_3)
    escorpion_4 = Escorpion(ruta_escorpion_4, TAMAÑO_ESCORPION, POS_ESCORPION_4)

    #Colision con escorpiones
    var_col_esc = verificar_colision_escorpion(luchador, contador_vidas, escorpion_1)
    contador_vidas = var_col_esc[0]
    POS_LUCHADOR = var_col_esc[1]
    var_col_esc = verificar_colision_escorpion(luchador, contador_vidas, escorpion_2)
    contador_vidas = var_col_esc[0]
    POS_LUCHADOR = var_col_esc[1]
    var_col_esc = verificar_colision_escorpion(luchador, contador_vidas, escorpion_3)
    contador_vidas = var_col_esc[0]
    POS_LUCHADOR = var_col_esc[1]
    var_col_esc = verificar_colision_escorpion(luchador, contador_vidas, escorpion_4)
    contador_vidas = var_col_esc[0]
    POS_LUCHADOR = var_col_esc[1]

    if contador_vidas == 1:
        desaparcer_img_y_rec(corazon_3)
    elif contador_vidas == 2:
        desaparcer_img_y_rec(corazon_2)
    elif contador_vidas == 3:
        desaparcer_img_y_rec(corazon_1)
        game_over = True

    aplicar_gravedad = varificar_pos_luchador_en_bloque(luchador, piso_plataforma)

    #Aplicar gravedad si el personaje llega a la altura deseada
    if salto_desde_plataforma == True and luchador.posicion[1] < 340:
        aplicar_gravedad = True
        realizar_salto = False
    elif salto_desde_primer_piso == True and luchador.posicion[1] < 190:
        aplicar_gravedad = True
        realizar_salto = False
    elif salto_desde_segundo_piso == True and luchador.posicion[1] < 10:
        aplicar_gravedad = True
        realizar_salto = False
    elif salto_desde_tercer_piso == True and luchador.posicion[1] < -100:
        aplicar_gravedad = True
        realizar_salto = False

    if aplicar_gravedad:
        luchador.mover_abajo()
    if realizar_salto:
        luchador.mover_arriba()

    # Colision manzanas
    contador_manzanas = verificar_colision_manzanas(luchador, contador_manzanas, manzana_1)
    contador_manzanas = verificar_colision_manzanas(luchador, contador_manzanas, manzana_2)
    contador_manzanas = verificar_colision_manzanas(luchador, contador_manzanas, manzana_3)
    contador_manzanas = verificar_colision_manzanas(luchador, contador_manzanas, manzana_4)
    contador_manzanas = verificar_colision_manzanas(luchador, contador_manzanas, manzana_5)
    contador_manzanas = verificar_colision_manzanas(luchador, contador_manzanas, manzana_6)
    contador_manzanas = verificar_colision_manzanas(luchador, contador_manzanas, manzana_7)

    #Cargar las imagenes en la pantalla
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

    if contador_manzanas == 7:
        pass

    if game_over:
        rec_game_over.dibujar(SCREEN)
        rec_reiniciar.dibujar(SCREEN)
        texto_game_over.mostrar_texto(SCREEN)
        texto_score.mostrar_texto(SCREEN)
        texto_score_puntos.mostrar_texto(SCREEN)
        texto_reiniciar.mostrar_texto(SCREEN)
        
        posicion_mouse = pygame.mouse.get_pos()
        if rec_reiniciar.rec.collidepoint(posicion_mouse):
            rec_reiniciar.cambiar_color(COLOR_ROJO)
        else:
            rec_reiniciar.devolver_color()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rec_reiniciar.rec.collidepoint(event.pos):
                restaurar_img_y_rec(corazon_1)
                restaurar_img_y_rec(corazon_2)
                restaurar_img_y_rec(corazon_3)
                restaurar_img_y_rec(manzana_1)
                restaurar_img_y_rec(manzana_2)
                restaurar_img_y_rec(manzana_3)
                restaurar_img_y_rec(manzana_4)
                restaurar_img_y_rec(manzana_5)
                restaurar_img_y_rec(manzana_6)
                restaurar_img_y_rec(manzana_7)
                manzana_1.restaurar_imagen()
                contador_vidas = 0
                game_over = False
                contador_manzanas = 0
                ruta_luchador = lista_luchador_caminando_derecha[0]
    else:
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

        if lista_teclas[pygame.K_LEFT]:
            luchador.mover_izquierda()
            ruta_luchador = lista_luchador_caminando_izquierda[img_luchador]
            img_luchador += 1
            if img_luchador > len(lista_luchador_caminando_izquierda) - 1:
                img_luchador = 0
                ultima_tecla = "Izquierda"
        elif lista_teclas[pygame.K_RIGHT]:
            luchador.mover_derecha()
            ruta_luchador = lista_luchador_caminando_derecha[img_luchador]
            img_luchador += 1
            if img_luchador > len(lista_luchador_caminando_derecha) - 1:
                img_luchador = 0
                ultima_tecla = "Derecha"
        elif lista_teclas[pygame.K_SPACE]:
            ruta_luchador = "IMAGENES\patadaDerecha3.png"
        elif lista_teclas[pygame.K_f]:
            ruta_luchador = "IMAGENES\puñoDerecha2.png"
        else:
            if ultima_tecla == "Derecha":
                ruta_luchador = lista_luchador_caminando_derecha[0]
            else:
                ruta_luchador = lista_luchador_caminando_izquierda[0]

        if lista_teclas[pygame.K_UP]:
            salto = aplicar_salto(luchador, aplicar_gravedad, realizar_salto, salto_desde_plataforma, salto_desde_primer_piso, salto_desde_segundo_piso, salto_desde_tercer_piso)
            aplicar_gravedad = salto[0]
            realizar_salto = salto[1]
            salto_desde_plataforma = salto[2]
            salto_desde_primer_piso = salto[3]
            salto_desde_segundo_piso = salto[4]
            salto_desde_tercer_piso = salto[5]
            if ultima_tecla == "Derecha":
                ruta_luchador = "IMAGENES\saltoDerecha3.png"
            else:
                ruta_luchador = "IMAGENES\saltoIzquierda3.png"

    #Dibujar los rectangulos si mantengo apretado la tecla 'R'
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