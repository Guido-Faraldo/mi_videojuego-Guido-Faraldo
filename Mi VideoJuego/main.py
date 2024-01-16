import sys
import pygame
from constantes import *
from Clases.texto import Texto
from Clases.veneno import Veneno
from Clases.escorpion import Escorpion
from mis_objetos import *
from mis_funciones import *

pygame.init()
conexion = crear_tabla("puntajes_mi_videojuego.bd")
agregar_datos = False
ingreso_usuario = True
nombre_usuario = ""
contador_escorpiones_muertos = 0
desaparecer_escorpion_1 = False
desaparecer_escorpion_2 = False
desaparecer_escorpion_3 = False
desaparecer_escorpion_4 = False
disparar_cuchillo_derecha = False
disparar_cuchillo_izquierda = False
nivel_tres = False
nivel_dos = False
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
texto_game_over = Texto("GAME OVER", COLOR_AZUL, POS_TEXTO_GAME_OVER, FUENTE_GRANDE)
texto_score = Texto("TU SCORE ES DE:", COLOR_AZUL, POS_TEXTO_SCORE, FUENTE_GRANDE)
texto_reiniciar = Texto("REINICIAR", COLOR_VERDE, POS_TEXTO_REINICIAR, FUENTE_CHICA)
texto_entendido = Texto("ENTENDIDO", COLOR_AZUL, POS_TEXTO_ENTENDIDO, FUENTE_CHICA)
texto_ingrese_nombre = Texto("INGRESE NOMBRE", COLOR_ROJO, POS_TEXTO_INGRESE_NOMBRE, FUENTE_GRANDE)
texto_mision_primer_nivel = Texto(TEXTO_PRIMER_NIVEL, COLOR_AZUL, POS_TEXTO_MISIONES, FUENTE_CHICA)
texto_mision_segundo_nivel = Texto(TEXTO_SEGUNDO_NIVEL, COLOR_AZUL, POS_TEXTO_MISIONES, FUENTE_CHICA)
texto_mision_tercer_nivel = Texto(TEXTO_TERCER_NIVEL, COLOR_AZUL, POS_TEXTO_MISIONES, FUENTE_CHICA)
texto_cabezera_puntaje = Texto("Id     Nombre     Puntaje", COLOR_ROJO, POS_TEXTO_CABEZERA_PUNTAJE, FUENTE_CHICA)

while True:
    lista_teclas = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or lista_teclas[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                nombre_usuario = nombre_usuario[0:-1]
            elif len(nombre_usuario) < 13:
                nombre_usuario += event.unicode
    
    valores_tabla = crear_texto_valores_tabla(conexion)
    ids = valores_tabla[0]
    nombres = valores_tabla[1]
    puntajes = valores_tabla[2]
    texto_ids = Texto(ids, COLOR_AZUL, POS_TEXTO_IDS, FUENTE_CHICA)
    texto_nombres = Texto(nombres, COLOR_AZUL, POS_TEXTO_NOMBRES, FUENTE_CHICA)
    texto_puntajes = Texto(puntajes, COLOR_AZUL, POS_TEXTO_PUNTAJES, FUENTE_CHICA)
    puntaje_int = contador_manzanas * 100.00
    milis = reloj.tick(60)
    texto_nombre_usuario = Texto(nombre_usuario, COLOR_NEGRO, POS_TEXTO_NOMBRE_USUARIO, FUENTE_CHICA)
    luchador = Luchador(ruta_luchador, TAMAÑO_LUCHADOR, POS_LUCHADOR)
    texto_manzanas_comidas = Texto(F"MANZANAS COMIDAS: {contador_manzanas}", COLOR_ROJO, POS_TEXTO_MANZANAS_COMIDAS, FUENTE_CHICA)
    texto_score_puntos = Texto(f"{puntaje_int} pts", COLOR_AZUL, POS_TEXTO_SCORE_PUNTOS, FUENTE_GRANDE)
    escorpion_1 = Escorpion(ruta_escorpion_1, TAMAÑO_ESCORPION, POS_ESCORPION_1)
    escorpion_2 = Escorpion(ruta_escorpion_2, TAMAÑO_ESCORPION, POS_ESCORPION_2)
    escorpion_3 = Escorpion(ruta_escorpion_3, TAMAÑO_ESCORPION, POS_ESCORPION_3)
    escorpion_4 = Escorpion(ruta_escorpion_4, TAMAÑO_ESCORPION, POS_ESCORPION_4)
    veneno_e_1 = Veneno(RUTA_VENENO_D, TAMAÑO_VENENO, POS_VENENO_E_1)
    veneno_e_2 = Veneno(RUTA_VENENO_I, TAMAÑO_VENENO, POS_VENENO_E_2)
    veneno_e_3 = Veneno(RUTA_VENENO_D, TAMAÑO_VENENO, POS_VENENO_E_3)
    veneno_e_4 = Veneno(RUTA_VENENO_I, TAMAÑO_VENENO, POS_VENENO_E_4)
    if disparar_cuchillo_izquierda == False and disparar_cuchillo_derecha == False:
        POS_CUCHILLO_IZQUIERDA = [luchador.rec.x, luchador.rec.y + 50]
        POS_CUCHILLO_DERECHA = [luchador.rec.x, luchador.rec.y + 50]
    cuchillo_derecha = Cuchillo(RUTA_CUCHILLO_DERECHA, TAMAÑO_CUCHILLO, POS_CUCHILLO_DERECHA)
    cuchillo_izquierda = Cuchillo(RUTA_CUCHILLO_IZQUIERDA, TAMAÑO_CUCHILLO, POS_CUCHILLO_IZQUIERDA)

    if event.type == pygame.MOUSEBUTTONDOWN:
        if rec_reiniciar.rec.collidepoint(event.pos) and game_over == True:
            restaurar_img_y_rec(corazon_1)
            restaurar_img_y_rec(corazon_2)
            restaurar_img_y_rec(corazon_3)
            resturar_manzanas(manzana_1, manzana_2, manzana_3, manzana_4, manzana_5, manzana_6, manzana_7)
            contador_escorpiones_muertos = 0
            contador_manzanas = 0
            contador_vidas = 0
            ruta_luchador = lista_luchador_caminando_derecha[0]
            game_over = False
            rec_texto_misiones.recenter()
            rec_texto_entendido.recenter()
            texto_mision_primer_nivel.volver_texto_normalidad()
            texto_entendido.volver_texto_normalidad()
            rec_texto_misiones.dibujar(SCREEN)
            rec_texto_entendido.dibujar(SCREEN)
            texto_entendido.mostrar_texto(SCREEN)
            ingreso_usuario = True
            if agregar_datos:
                agregar_dato_tabla(conexion, nombre_usuario, puntaje_int)
                agregar_datos = False
            nombre_usuario = ""
            rec_reiniciar.disappear()
        if rec_texto_entendido.rec.collidepoint(event.pos):
            if nivel_dos == False and nivel_tres == False:
                texto_mision_primer_nivel.desaparcer_texto()
                if contador_manzanas == 7:
                    contador_manzanas = 0
                    resturar_manzanas(manzana_1, manzana_2, manzana_3, manzana_4, manzana_5, manzana_6, manzana_7)
                    nivel_dos = True
                    salto_desde_plataforma = True
            elif nivel_dos:
                nivel_dos = False
                nivel_tres = True
                contador_manzanas = 0
                resturar_manzanas(manzana_1, manzana_2, manzana_3, manzana_4, manzana_5, manzana_6, manzana_7)
                salto_desde_plataforma = True
                texto_mision_segundo_nivel.desaparcer_texto()
            else:
                salto_desde_plataforma = True
                texto_mision_tercer_nivel.desaparcer_texto()
            rec_texto_misiones.disappear()
            texto_entendido.desaparcer_texto()
            rec_texto_entendido.disappear()

    posicion_mouse = pygame.mouse.get_pos()
    if rec_texto_entendido.rec.collidepoint(posicion_mouse):
        rec_texto_entendido.cambiar_color(COLOR_ROJO)
    else:
        rec_texto_entendido.devolver_color()
    if rec_reiniciar.rec.collidepoint(posicion_mouse):
            rec_reiniciar.cambiar_color(COLOR_ROJO)
    else:
        rec_reiniciar.devolver_color()

    #Colision con escorpiones
    var_col_enem = verificar_colision_enemigo(luchador, contador_vidas, escorpion_1, escorpion_2, escorpion_3, escorpion_4, salto_desde_plataforma)
    contador_vidas = var_col_enem[0]
    POS_LUCHADOR = var_col_enem[1]
    salto_desde_plataforma = var_col_enem[2]

    #Desaparcer corazones
    game_over = desaparecer_corazones(contador_vidas, corazon_1, corazon_2, corazon_3, game_over)

    #No aplico gravedad si el personaje esta en las plataformas
    aplicar_gravedad = varificar_pos_luchador_en_bloque(luchador, piso_plataforma)

    #Aplicar gravedad si el personaje llega a la altura deseada
    var_bajar_luchador = bajar_luchador(salto_desde_plataforma, salto_desde_primer_piso, salto_desde_segundo_piso, salto_desde_tercer_piso, luchador,
                                        aplicar_gravedad, realizar_salto)
    aplicar_gravedad = var_bajar_luchador[0]
    realizar_salto = var_bajar_luchador[1]

    #Bajar o subir al jugador
    if aplicar_gravedad:
        luchador.mover_abajo()
    if realizar_salto:
        luchador.mover_arriba()

    # Colision manzanas
    contador_manzanas = verificar_colision_manzanas(luchador, contador_manzanas, manzana_1, manzana_2, manzana_3, manzana_4, manzana_5, manzana_6, manzana_7)

    #Cargar las imagenes en la pantalla
    fondo.cargar_imagen(SCREEN)
    if ingreso_usuario:
        texto_ingrese_nombre.mostrar_texto(SCREEN)
        rec_ingreso_nombre.dibujar(SCREEN)
        texto_nombre_usuario.mostrar_texto(SCREEN)
        if lista_teclas[pygame.K_RETURN]:
            ingreso_usuario = False
    else:
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
        rec_texto_misiones.dibujar(SCREEN)
        rec_texto_entendido.dibujar(SCREEN)
        texto_mision_primer_nivel.mostrar_texto_con_saltos(SCREEN, [40, 35])
        texto_entendido.mostrar_texto(SCREEN)

    if contador_manzanas == 7 and nivel_tres == False:
        POS_LUCHADOR = [60, 450]
        rec_texto_misiones.recenter()
        rec_texto_entendido.recenter()
        rec_texto_misiones.dibujar(SCREEN)
        rec_texto_entendido.dibujar(SCREEN)
        texto_entendido.volver_texto_normalidad()
        texto_entendido.mostrar_texto(SCREEN)
        if nivel_dos == False:
            texto_mision_segundo_nivel.mostrar_texto_con_saltos(SCREEN, [40, 35])
        elif nivel_dos:
            texto_mision_tercer_nivel.mostrar_texto_con_saltos(SCREEN, [40, 35])

    if nivel_dos and contador_manzanas < 7:
        veneno_e_1.cargar_imagen(SCREEN)
        veneno_e_1.mover_derecha(5)
        veneno_e_2.cargar_imagen(SCREEN)
        veneno_e_2.mover_izquierda(5)
        veneno_e_3.cargar_imagen(SCREEN)
        veneno_e_3.mover_derecha(5)
        veneno_e_4.cargar_imagen(SCREEN)
        veneno_e_4.mover_izquierda(5)
        if escorpion_1.rec.x == 370 and POS_VENENO_E_1[0] > ANCHO_VENTANA:
            POS_VENENO_E_1 = [piso_bloque_grande_1.rec.x + piso_bloque_grande_1.base, 125]
        if escorpion_2.rec.x == 630 and POS_VENENO_E_2[0] < 0:
            POS_VENENO_E_2 = [piso_bloque_grande_2.rec.x, 125]
        if escorpion_3.rec.x == 375 and POS_VENENO_E_3[0] > ANCHO_VENTANA:
            POS_VENENO_E_3 = [piso_bloque_grande_3.rec.x + piso_bloque_grande_3.base, 420]
        if escorpion_4.rec.x == 635 and POS_VENENO_E_4[0] < 0:
            POS_VENENO_E_4 = [piso_bloque_grande_4.rec.x, 420]
        var_col_enem = verificar_colision_enemigo(luchador, contador_vidas, veneno_e_1, veneno_e_2, veneno_e_3, veneno_e_4, salto_desde_plataforma)
        contador_vidas = var_col_enem[0]
        POS_LUCHADOR = var_col_enem[1]
        salto_desde_plataforma = var_col_enem[2]

    if nivel_tres:
        var_disp_cuchll = disparar_cuchillo(disparar_cuchillo_derecha, cuchillo_derecha, SCREEN, ANCHO_VENTANA, POS_CUCHILLO_DERECHA, luchador,
                                            disparar_cuchillo_izquierda, cuchillo_izquierda, POS_CUCHILLO_IZQUIERDA)
        POS_CUCHILLO_DERECHA = var_disp_cuchll[0]
        POS_CUCHILLO_IZQUIERDA = var_disp_cuchll[1]
        disparar_cuchillo_derecha = var_disp_cuchll[2]
        disparar_cuchillo_izquierda = var_disp_cuchll[3]

        var_desp_escrp = desaparcer_escorpiones(cuchillo_derecha, luchador, escorpion_1, escorpion_2, escorpion_3, escorpion_4, disparar_cuchillo_derecha,
                                                desaparecer_escorpion_1, desaparecer_escorpion_2, desaparecer_escorpion_3, desaparecer_escorpion_4,
                                                contador_escorpiones_muertos, POS_CUCHILLO_DERECHA)
        desaparecer_escorpion_1 = var_desp_escrp[0]
        desaparecer_escorpion_2 = var_desp_escrp[1]
        desaparecer_escorpion_3 = var_desp_escrp[2]
        desaparecer_escorpion_4 = var_desp_escrp[3]
        disparar_cuchillo_derecha = var_desp_escrp[4]
        contador_escorpiones_muertos = var_desp_escrp[5]
        POS_CUCHILLO_DERECHA = var_desp_escrp[6]

        var_desp_escrp = desaparcer_escorpiones(cuchillo_izquierda, luchador, escorpion_1, escorpion_2, escorpion_3, escorpion_4, disparar_cuchillo_izquierda,
                                                desaparecer_escorpion_1, desaparecer_escorpion_2, desaparecer_escorpion_3, desaparecer_escorpion_4,
                                                contador_escorpiones_muertos, POS_CUCHILLO_IZQUIERDA)
        desaparecer_escorpion_1 = var_desp_escrp[0]
        desaparecer_escorpion_2 = var_desp_escrp[1]
        desaparecer_escorpion_3 = var_desp_escrp[2]
        desaparecer_escorpion_4 = var_desp_escrp[3]
        disparar_cuchillo_izquierda = var_desp_escrp[4]
        contador_escorpiones_muertos = var_desp_escrp[5]
        POS_CUCHILLO_IZQUIERDA = var_desp_escrp[6]

        if desaparecer_escorpion_1:
            escorpion_1.mover_abajo(33)
        if desaparecer_escorpion_2:
            escorpion_2.mover_abajo(33)
        if desaparecer_escorpion_3:
            escorpion_3.mover_abajo(33)
        if desaparecer_escorpion_4:
            escorpion_4.mover_abajo(33)

        if contador_escorpiones_muertos == 4 and contador_manzanas == 7:
            game_over = True

    if game_over:
        rec_reiniciar.recenter()
        agregar_datos = True
        POS_ESCORPION_1 = [250, 120]
        POS_ESCORPION_2 = [750, 120]
        POS_ESCORPION_3 = [270, 415]
        POS_ESCORPION_4 = [650, 415]
        POS_LUCHADOR = [60, 450]
        if nivel_dos:
            contador_manzanas += 7
            nivel_dos = False
        if nivel_tres:
            contador_manzanas += 14
            nivel_tres = False
        ruta_luchador = RUTA_LUCHADOR_MUERTO
        texto_mision_segundo_nivel.volver_texto_normalidad()
        texto_mision_tercer_nivel.volver_texto_normalidad()
        rec_game_over.dibujar(SCREEN)
        rec_reiniciar.dibujar(SCREEN)
        texto_game_over.mostrar_texto(SCREEN)
        texto_score.mostrar_texto(SCREEN)
        texto_score_puntos.mostrar_texto(SCREEN)
        texto_reiniciar.mostrar_texto(SCREEN)
        rec_puntaje.dibujar(SCREEN)
        texto_cabezera_puntaje.mostrar_texto(SCREEN)
        texto_ids.mostrar_texto_con_saltos(SCREEN, [680, 160])
        texto_nombres.mostrar_texto_con_saltos(SCREEN, [740, 160])
        texto_puntajes.mostrar_texto_con_saltos(SCREEN, [900, 160])
    else:
        #Movimineto escorpiones
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
            var_sprites = cambiar_sprites(ruta_luchador, lista_luchador_caminando_izquierda, img_luchador)
            ruta_luchador = var_sprites[0]
            img_luchador = var_sprites[1]
            ultima_tecla = "Izquierda"
        elif lista_teclas[pygame.K_RIGHT]:
            luchador.mover_derecha()
            var_sprites = cambiar_sprites(ruta_luchador, lista_luchador_caminando_derecha, img_luchador)
            ruta_luchador = var_sprites[0]
            img_luchador = var_sprites[1]
            ultima_tecla = "Derecha"
        elif lista_teclas[pygame.K_f]:
            if ultima_tecla == "Derecha":
                disparar_cuchillo_derecha = True
                ruta_luchador = RUTA_LUCHADOR_PUÑO_DERECHO
            else:
                disparar_cuchillo_izquierda = True
                ruta_luchador = RUTA_LUCHADOR_PUÑO_IZQUIERDO
        elif lista_teclas[pygame.K_SPACE]:
            if ultima_tecla == "Derecha":
                ruta_luchador = RUTA_LUCHADOR_PATADA_DERECHA
            else:
                ruta_luchador = RUTA_LUCHADOR_PATADA_IZQUIERDA
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
                ruta_luchador = RUTA_LUCHADOR_SALTO_DERECHA
            else:
                ruta_luchador = RUTA_LUCHADOR_SALTO_IZQUIERDA

    #Dibujar los rectangulos si mantengo apretado la tecla 'R'
    if ingreso_usuario:
        pass
    else:
        if lista_teclas[pygame.K_r]:
            cuchillo_derecha.dibujar_rectangulo(SCREEN)
            cuchillo_izquierda.dibujar_rectangulo(SCREEN)
            veneno_e_1.dibujar_rectangulo(SCREEN)
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