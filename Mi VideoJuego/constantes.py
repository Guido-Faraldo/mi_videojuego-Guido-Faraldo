#PANTALLA-------------------------
ANCHO_VENTANA = 1000
ALTO_VENTANA = 650

#COLORES-------------------------
COLOR_NEGRO = (0, 0, 0)
COLOR_BLANCO = (255,255,255)
COLOR_VERDE = (0,255,0)
COLOR_ROJO = (255,0,0)
COLOR_GRIS = (128,128,128)
COLOR_AMARILLO = (255,255,0)
COLOR_CELESTE = (0,0,255)
COLOR_AZUL = (0,0,128)
GRAVEDAD = 1

#IMAGEN DE FONDO-------------------------
RUTA_FONDO = 'IMAGENES\Fondo Mi Videojuego.png'
TAMAÑO_FONDO = (ANCHO_VENTANA, ALTO_VENTANA)
POS_FONDO = (0, 0)

#PISOS-------------------------
#Piso plataforma
RUTA_PISO = "IMAGENES\piso.png"
POS_PISO = (-60, 565)
TAMAÑO_PISO = (1115, 110)
#Piso bloques grandes
RUTA_BLOQUE_GRANDE = "IMAGENES\Bloque de piso grande.png"
TAMAÑO_BLOQUE_GRANDE = (210, 35)
POS_BLOQUE_GRANDE_1 = (210, 165)
POS_BLOQUE_GRANDE_2 = (635, 165)
POS_BLOQUE_GRANDE_3 = (210, 460)
POS_BLOQUE_GRANDE_4 = (635, 460)
#Piso bloques chicos
RUTA_BLOQUE_CHICO = "IMAGENES\Bloque de piso chico.png"
TAMAÑO_BLOQUE_CHICO = (130, 40)
POS_BLOQUE_CHICO_1 = (45, 320)
POS_BLOQUE_CHICO_2 = (455, 320)
POS_BLOQUE_CHICO_3 = (870, 320)

#TEXTOS-------------------------
#Texto "vidas"
POS_TEXTO_VIDAS = (3, 0)
#Texto "manzanas comidas"
POS_TEXTO_MANZANAS_COMIDAS = (635, 5)
#Texto rectangulo juego terminado
POS_TEXTO_GAME_OVER = (330, 150)
POS_TEXTO_SCORE = (285, 220)
POS_TEXTO_SCORE_PUNTOS = (365, 300)
POS_TEXTO_REINICIAR = (380, 450)
#Texto misiones
POS_TEXTO_MISIONES = [40, 35]
POS_TEXTO_ENTENDIDO = (445, 365)
TEXTO_PRIMER_NIVEL = """NIVEL 1:\n\nMISIÓN:\nConsigue recoger todas las manzanas \npara pasar el nivel.
                        \nNOTA:\nTen cuidado, no puedes tocar a los \nescorpiones."""
TEXTO_SEGUNDO_NIVEL = """NIVEL 2:\n\nFelicitaciones! Conseguiste todas las 
manzanas.
Ten cuidado, ahora los escorpiones lanzan
veneno. Trata de recolectar las manzanas 
sin tocarlos a ellos, ni lo que lanzan."""
TEXTO_TERCER_NIVEL = """Muy bien! Llegaste a la etapa final.
Para completar el juego ahora no solo
tienes que recolectar todas las manzanas,
sino que tienes que matar a los escorpiones.
Para eso puedes ayudarte con la tecla 'F' 
con la cual puedes disparar cuchillos.
Recuerda que solo puedes usarlos cada 
cierto tiempo"""
#Texto nombre usuario
POS_TEXTO_NOMBRE_USUARIO = (405, 305)
POS_TEXTO_INGRESE_NOMBRE = (325, 100)
#Texto puntaje
POS_TEXTO_CABEZERA_PUNTAJE = (675, 155)
POS_TEXTO_IDS = [680, 160]
POS_TEXTO_NOMBRES = [740, 160]
POS_TEXTO_PUNTAJES = [900, 160]

#CORAZONES-------------------------
RUTA_CORAZON = "IMAGENES\corazon.png"
TAMAÑO_CORAZON = (55, 55)
POS_CORAZON_1 = (130, 1)
POS_CORAZON_2 = (190, 1)
POS_CORAZON_3 = (250, 1)

#MANZNAS-------------------------
RUTA_MANZANA = "IMAGENES\manzana.png"
TAMAÑO_MANZANA = (35, 35)
POS_MANZANA_1 = (295, 130)
POS_MANZANA_2 = (720, 130)
POS_MANZANA_3 = (85, 285)
POS_MANZANA_4 = (495, 285)
POS_MANZANA_5 = (910, 285)
POS_MANZANA_6 = (295, 425)
POS_MANZANA_7 = (720, 425)

#ESCORPIONES
RUTAS_ESCORPION = ["IMAGENES\enemigoDerecha.png", "IMAGENES\enemigoIzquierda.png"]
POS_ESCORPION_1 = [250, 120]
POS_ESCORPION_2 = [750, 120]
POS_ESCORPION_3 = [270, 415]
POS_ESCORPION_4 = [650, 415]
TAMAÑO_ESCORPION = (50, 50)

#LUCHADOR
POS_LUCHADOR = [60, 450]
TAMAÑO_LUCHADOR = (60, 100)
lista_luchador_caminando_derecha = ["IMAGENES\caminandoDerecha1.png",
                                    "IMAGENES\caminandoDerecha2.png",
                                    "IMAGENES\caminandoDerecha3.png",
                                    "IMAGENES\caminandoDerecha4.png"]
lista_luchador_caminando_izquierda = ["IMAGENES\caminandoIzquierda1.png",
                                    "IMAGENES\caminandoIzquierda2.png",
                                    "IMAGENES\caminandoIzquierda3.png",
                                    "IMAGENES\caminandoIzquierda4.png"]
ruta_luchador = lista_luchador_caminando_derecha[0]
RUTA_LUCHADOR_MUERTO = "IMAGENES\luchadormuerto.png"
RUTA_LUCHADOR_PUÑO_DERECHO = "IMAGENES\puñoDerecha2.png"
RUTA_LUCHADOR_PUÑO_IZQUIERDO = "IMAGENES\puñoIzquierda2.png"
RUTA_LUCHADOR_PATADA_DERECHA = "IMAGENES\patadaDerecha3.png"
RUTA_LUCHADOR_PATADA_IZQUIERDA = "IMAGENES\patadaIzquierda3.png"
RUTA_LUCHADOR_SALTO_DERECHA = "IMAGENES\saltoDerecha3.png"
RUTA_LUCHADOR_SALTO_IZQUIERDA = "IMAGENES\saltoIzquierda3.png"

#RECTANGULOS-------------------------
#Rectangulos juego terminado
POS_REC_GAME_OVER = (250, 100)
TAMAÑO_REC_GAME_OVER = (400, 500)
POS_REC_REINICIAR = (350, 420)
TAMAÑO_REC_REINICIAR = (200, 100)
#Rectangulos Texto Misiones
POS_REC_MISIONES = (25, 25)
TAMAÑO_REC_MISIONES = (600, 300)
POS_REC_ENTENDIDO = (425, 340)
TAMAÑO_REC_ENTENDIDO = (200, 100)
POS_REC_INGRESO_USUARIO = (400, 300)
TAMAÑO_REC_INGRESO_USUARIO = (200, 50)
#Rectangulo Puntaje
POS_REC_PUNTAJE = (660, 150)
TAMAÑO_REC_PUNTAJE = (330, 220)

#VENENO-------------------------
RUTA_VENENO_D = "IMAGENES\\venenoDerecha.png"
RUTA_VENENO_I = "IMAGENES\\venenoIzquierda.png"
TAMAÑO_VENENO = (20, 10)

#CUCHILLO-------------------------
RUTA_CUCHILLO_IZQUIERDA = "IMAGENES\cuchilloIzquierda.png"
RUTA_CUCHILLO_DERECHA = "IMAGENES\cuchilloDerecha.png"
TAMAÑO_CUCHILLO = (50, 20)
POS_CUCHILLO = (340, 60)