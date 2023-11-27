import pygame
import sqlite3

def crear_tabla(path):
    with sqlite3.connect(path) as conexion:
        try:
            sentencia = ''' create table puntos
            (
            id integer primary key autoincrement,
            nombre text, 
            puntaje int
            )
            '''
            conexion.execute(sentencia)
            print("Se creo la tabla puntos")
        except:
            print("La tabla puntos ya existe")

    return conexion


def agregar_dato_tabla(conexion, nombre_usuario, puntaje):
    try:
        conexion.execute("insert into puntos(nombre,puntaje) values (?,?)", (nombre_usuario, puntaje))
        conexion.commit()
    except:
        print("Error")


def separar_cinco_mejores(conexion):
    lista = []
    cursor = conexion.execute("SELECT * FROM puntos ORDER BY puntaje DESC LIMIT 5")
    for fila in cursor:
        dict_usuario = {}
        dict_usuario['id'] = fila[0]
        dict_usuario['nombre'] = fila[1]
        dict_usuario['puntaje'] = fila[2]
        lista.append(dict_usuario)
    return lista


def crear_texto_valores_tabla(conexion):
    lista_tabla_puntaje = separar_cinco_mejores(conexion)
    ids = ""
    nombres = ""
    puntaje = ""
    for el in lista_tabla_puntaje:
        ids = ids + "\n" + str(el['id'])
        nombres = nombres + '\n' + el['nombre']
        puntaje = puntaje + '\n' + str(el['puntaje'])
    
    return ids, nombres, puntaje


def restaurar_img_y_rec(obj) -> None:
    '''Restaura la imagen y el rectangulo del objeto que se le pasa por parametro
    con el objetivo de que aparezcan de vuelta en la pantalla del juego'''
    obj.restaurar_imagen()
    obj.restaurar_rectangulo()


def resturar_manzanas(m_1, m_2, m_3, m_4, m_5, m_6, m_7):
    '''Restaura la imagen y el rectangulo de todas las manzanas para cuando se pasa de nivel,
    con el objetivo de que aparezcan de vuelta en la pantalla del juego'''
    restaurar_img_y_rec(m_1)
    restaurar_img_y_rec(m_2)
    restaurar_img_y_rec(m_3)
    restaurar_img_y_rec(m_4)
    restaurar_img_y_rec(m_5)
    restaurar_img_y_rec(m_6)
    restaurar_img_y_rec(m_7)


def desaparcer_img_y_rec(obj) -> None:
    '''Desaparace la imagen y el rectangulo del objeto que se le pasa por parametro
    con el objetivo de que ya no esten mas en la pantalla del juego'''
    obj.desaparecer_imagen()
    obj.desaparecer_rectangulo()


def desaparecer_corazones(contador:int, cor_1, cor_2, cor_3, game_over:bool) -> bool:
    '''Desaparece los corazones pasados por parametros dependiendo en cuanto este el conatdor de las vidas.
    Y en caso de que se pierdan las tres vidas se temrina el juego'''
    if contador == 1:
        desaparcer_img_y_rec(cor_3)
    elif contador == 2:
        desaparcer_img_y_rec(cor_2)
    elif contador == 3:
        desaparcer_img_y_rec(cor_1)
        game_over = True
    return game_over


def verificar_colision_manzanas(luchador, contador:int, m_1, m_2, m_3, m_4, m_5, m_6, m_7) -> int:
    '''Verifica si el rectangulo del luchador colisiono con las manzanas pasadas por parametro,
    sumando 1 al contador de manzanas que retorna si ocurre'''
    if luchador.rec.colliderect(m_1.rec):
        desaparcer_img_y_rec(m_1)
        contador += 1
    if luchador.rec.colliderect(m_2.rec):
        desaparcer_img_y_rec(m_2)
        contador += 1
    if luchador.rec.colliderect(m_3.rec):
        desaparcer_img_y_rec(m_3)
        contador += 1
    if luchador.rec.colliderect(m_4.rec):
        desaparcer_img_y_rec(m_4)
        contador += 1
    if luchador.rec.colliderect(m_5.rec):
        desaparcer_img_y_rec(m_5)
        contador += 1
    if luchador.rec.colliderect(m_6.rec):
        desaparcer_img_y_rec(m_6)
        contador += 1
    if luchador.rec.colliderect(m_7.rec):
        desaparcer_img_y_rec(m_7)
        contador += 1
    return contador


def verificar_colision_enemigo(luchador, contador_vidas:int, enemigo_1, enemigo_2, enemigo_3, enemigo_4, salto_desde_plataforma:bool) -> int:
    '''Verifica si el luchador colsiono con algun objeto enemigo, y en caso de que 
    eso ocurra, se dveuleve al luchador en su posion original y se suma 1 al contador
    de vidas que retorna la funcion'''
    if luchador.rec.colliderect(enemigo_1.rec):
        desaparcer_img_y_rec(luchador)
        luchador.posicion = [60, 461]
        contador_vidas += 1
        salto_desde_plataforma = True
    elif luchador.rec.colliderect(enemigo_2.rec):
        desaparcer_img_y_rec(luchador)
        luchador.posicion = [60, 461]
        contador_vidas += 1
        salto_desde_plataforma = True
    elif luchador.rec.colliderect(enemigo_3.rec):
        desaparcer_img_y_rec(luchador)
        luchador.posicion = [60, 461]
        contador_vidas += 1
        salto_desde_plataforma = True
    elif luchador.rec.colliderect(enemigo_4.rec):
        desaparcer_img_y_rec(luchador)
        luchador.posicion = [60, 461]
        contador_vidas += 1
        salto_desde_plataforma = True
    return contador_vidas, luchador.posicion, salto_desde_plataforma


def varificar_pos_luchador_en_bloque(luchador, piso_plataforma) -> bool:
    '''Verifica si el luchador esta en alguna poscion que sea por encima de los bloques
    de las platafromas, en caso de que sea cierto, no se aplica gravedad, es decir, 
    se retorna False. En caso contrario, si el luchador no se encuentra por encima de las 
    plafaromas, se aplica la gravedad, es decir, se retorna True'''
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

def aplicar_salto(luchador, gravedad, salto, plataforma, primer_piso, segundo_piso, tercer_piso):
    '''Verifica si al apretar la tecla hacia arriba, el luchador si se encuentre por encima de alguna plataforma.
    En caso de que sea cierto se realiza el salto, en caso contrario, el jugador no salta'''
    if luchador.posicion[1] > 460 and luchador.posicion[1] < 480:
        salto = True
        gravedad = False
        tercer_piso = False
        segundo_piso = False
        primer_piso = False
        plataforma = True
    elif ((((luchador.rec.x >= 185) and (luchador.rec.x <= 405)) and ((luchador.rec.y >= 360) and (luchador.rec.y <= 370))) or 
    (((luchador.rec.x >= 610) and (luchador.rec.x <= 830)) and ((luchador.rec.y >= 360) and (luchador.rec.y <= 370)))):
        salto = True
        gravedad = False
        tercer_piso = False
        segundo_piso = False
        primer_piso = True
        plataforma = False
    elif ((((luchador.rec.x >= 15) and (luchador.rec.x <= 165)) and ((luchador.rec.y >= 220) and (luchador.rec.y <= 230))) or 
    (((luchador.rec.x >= 425) and (luchador.rec.x <= 575)) and ((luchador.rec.y >= 220) and (luchador.rec.y <= 230))) or 
    (((luchador.rec.x >= 835) and (luchador.rec.x <= 980)) and ((luchador.rec.y >= 220) and (luchador.rec.y <= 230)))):
        salto = True
        gravedad = False
        tercer_piso = False
        segundo_piso = True
        primer_piso = False
        plataforma = False
    elif ((((luchador.rec.x >= 185) and (luchador.rec.x <= 405)) and ((luchador.rec.y >= 70) and (luchador.rec.y <= 80))) or 
            (((luchador.rec.x >= 610) and (luchador.rec.x <= 830)) and ((luchador.rec.y >= 70) and (luchador.rec.y <= 80)))):
        salto = True
        gravedad = False
        tercer_piso = True
        segundo_piso = False
        primer_piso = False
        plataforma = False
    return gravedad, salto, plataforma, primer_piso, segundo_piso, tercer_piso


def bajar_luchador(plataforma:bool, primer_piso:bool, segundo_piso:bool, tercer_piso:bool, luchador, gravedad:bool, salto:bool) -> bool:
    '''Aplica la gravedad en caso de que el luchador, luegho de relaizar el salto, llegue a cierta altura, dependiendo de en
    donde este parado'''
    if plataforma == True and luchador.posicion[1] < 340:
        gravedad = True
        salto = False
    elif primer_piso == True and luchador.posicion[1] < 190:
        gravedad = True
        salto = False
    elif segundo_piso == True and luchador.posicion[1] < 10:
        gravedad = True
        salto = False
    elif tercer_piso == True and luchador.posicion[1] < -100:
        gravedad = True
        salto = False
    return gravedad, salto


def reaparcer_veneno(escorpion, limite, pos_veneno, piso) -> list:
    '''Verifica si el veneno ya esta fuera de la pantalla para poder reapercer
    en la posicion deseada'''
    if escorpion.rec.x == 370 and pos_veneno[0] > limite:
        pos_veneno = [piso.rec.x + piso.base, 125]
    return pos_veneno


def desaparcer_escorpiones(cuchillo, luchador, e_1, e_2, e_3, e_4, disparar_cuchillo:bool, desparecer_e_1:bool, desparecer_e_2:bool, desparecer_e_3:bool, 
                            desparecer_e_4:bool, contador:int, pos_cuchillo:list) -> bool:
    '''Verifica si el cuchillo disparado por el personaje colisiono con alguno de los escopiones pasados
    por parametro. En caso de ser asi, los escorpiones desapareceny el cuchillo vuelve a su posicion normal'''
    if cuchillo.rec.x != luchador.rec.x:
        if cuchillo.rec.colliderect(e_1.rec):
            desparecer_e_1 = True
            contador += 1
            pos_cuchillo = [luchador.rec.x + luchador.base, luchador.rec.y + 50]
            disparar_cuchillo = False
        elif cuchillo.rec.colliderect(e_2.rec):
            desparecer_e_2 = True
            contador += 1
            pos_cuchillo = [luchador.rec.x + luchador.base, luchador.rec.y + 50]
            disparar_cuchillo = False
        elif cuchillo.rec.colliderect(e_3.rec):
            desparecer_e_3 = True
            contador += 1
            pos_cuchillo = [luchador.rec.x + luchador.base, luchador.rec.y + 50]
            disparar_cuchillo = False
        elif cuchillo.rec.colliderect(e_4.rec):
            desparecer_e_4 = True
            contador += 1
            pos_cuchillo = [luchador.rec.x + luchador.base, luchador.rec.y + 50]
            disparar_cuchillo = False
    return desparecer_e_1, desparecer_e_2, desparecer_e_3, desparecer_e_4, disparar_cuchillo, contador, pos_cuchillo


def disparar_cuchillo(disparar_c_d:bool, cuchillo_d, screen, limite_d:int, pos_c_d:list, luchador, disparar_c_i:bool, cuchillo_i, pos_c_i:list) -> bool:
    '''En caso de que se haya apretado la tecla 'f', dependiendo de a donde estaba mirando el perosnaje, se carga
    la imagen del cuchillo y se lanza hacia la izquierda o la derecha'''
    if disparar_c_d:
        cuchillo_d.cargar_imagen(screen)
        cuchillo_d.mover_derecha(15)
        if cuchillo_d.rec.x > limite_d:
            pos_c_d = [luchador.rec.x, luchador.rec.y + 50]
            disparar_c_d = False
    if disparar_c_i:
        cuchillo_i.cargar_imagen(screen)
        cuchillo_i.mover_izquierda(15)
        if cuchillo_i.rec.x < 0:
            pos_c_i = [luchador.rec.x, luchador.rec.y + 50]
            disparar_c_i = False
    return pos_c_d, pos_c_i, disparar_c_d, disparar_c_i


def cambiar_sprites(ruta:str, lista:list, img:int):
    '''Va cambiando la imagen del luchador a medida que se apreta la tecla'''
    ruta = lista[img]
    img += 1
    if img > len(lista) - 1:
        img = 0
    return ruta, img