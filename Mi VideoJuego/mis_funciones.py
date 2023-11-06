import pygame

def restaurar_img_y_rec(obj):
    obj.restaurar_imagen()
    obj.restaurar_rectangulo()

def desaparcer_img_y_rec(obj):
    obj.desaparecer_imagen()
    obj.desaparecer_rectangulo()

def verificar_colision_manzanas(luchador, contador_manzanas, manzana):
    if luchador.rec.colliderect(manzana.rec):
        desaparcer_img_y_rec(manzana)
        contador_manzanas += 1

    return contador_manzanas

def verificar_colision_escorpion(luchador, contador_vidas, escorpion):
    if luchador.rec.colliderect(escorpion.rec):
        desaparcer_img_y_rec(luchador)
        luchador.posicion = [60, 360]
        contador_vidas += 1

    return contador_vidas, luchador.posicion

def varificar_pos_luchador_en_bloque(luchador, piso_plataforma):
    if (luchador.rec.colliderect(piso_plataforma.rec) or 
    (((luchador.rec.x >= 185) and (luchador.rec.x <= 405)) and ((luchador.rec.y >= 360) and (luchador.rec.y <= 370))) or 
    (((luchador.rec.x >= 610) and (luchador.rec.x <= 830)) and ((luchador.rec.y >= 360) and (luchador.rec.y <= 370))) or 
    (((luchador.rec.x >= 15) and (luchador.rec.x <= 165)) and ((luchador.rec.y >= 220) and (luchador.rec.y <= 230))) or 
    (((luchador.rec.x >= 425) and (luchador.rec.x <= 575)) and ((luchador.rec.y >= 220) and (luchador.rec.y <= 230))) or 
    (((luchador.rec.x >= 835) and (luchador.rec.x <= 980)) and ((luchador.rec.y >= 220) and (luchador.rec.y <= 230))) or 
    (((luchador.rec.x >= 185) and (luchador.rec.x <= 405)) and ((luchador.rec.y >= 70) and (luchador.rec.y <= 80))) or 
    (((luchador.rec.x >= 610) and (luchador.rec.x <= 830)) and ((luchador.rec.y >= 70) and (luchador.rec.y <= 80)))):
        aplicar_gravedad = False
    else:
        aplicar_gravedad = True

    return aplicar_gravedad

def aplicar_salto(luchador, aplicar_gravedad, realizar_salto, salto_desde_plataforma, salto_desde_primer_piso, salto_desde_segundo_piso, salto_desde_tercer_piso):
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
    elif ((((luchador.rec.x >= 15) and (luchador.rec.x <= 165)) and ((luchador.rec.y >= 220) and (luchador.rec.y <= 230))) or 
    (((luchador.rec.x >= 425) and (luchador.rec.x <= 575)) and ((luchador.rec.y >= 220) and (luchador.rec.y <= 230))) or 
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

    return aplicar_gravedad, realizar_salto, salto_desde_plataforma, salto_desde_primer_piso, salto_desde_segundo_piso, salto_desde_tercer_piso

