from constantes import *
from Clases.corazon import Corazon
from Clases.escorpion import Escorpion
from Clases.fondo import Fondo
from Clases.luchador import Luchador
from Clases.manzana import Manzana
from Clases.piso import Piso
from Clases.rectangulo import Rectangulo
from Clases.veneno import Veneno

fondo = Fondo(RUTA_FONDO, TAMAÑO_FONDO, POS_FONDO)

corazon_1 = Corazon(RUTA_CORAZON, TAMAÑO_CORAZON, POS_CORAZON_1)
corazon_2 = Corazon(RUTA_CORAZON, TAMAÑO_CORAZON, POS_CORAZON_2)
corazon_3 = Corazon(RUTA_CORAZON, TAMAÑO_CORAZON, POS_CORAZON_3)

manzana_1 = Manzana(RUTA_MANZANA, TAMAÑO_MANZANA, POS_MANZANA_1)
manzana_2 = Manzana(RUTA_MANZANA, TAMAÑO_MANZANA, POS_MANZANA_2)
manzana_3 = Manzana(RUTA_MANZANA, TAMAÑO_MANZANA, POS_MANZANA_3)
manzana_4 = Manzana(RUTA_MANZANA, TAMAÑO_MANZANA, POS_MANZANA_4)
manzana_5 = Manzana(RUTA_MANZANA, TAMAÑO_MANZANA, POS_MANZANA_5)
manzana_6 = Manzana(RUTA_MANZANA, TAMAÑO_MANZANA, POS_MANZANA_6)
manzana_7 = Manzana(RUTA_MANZANA, TAMAÑO_MANZANA, POS_MANZANA_7)

piso_plataforma = Piso(RUTA_PISO, TAMAÑO_PISO, POS_PISO)
piso_bloque_grande_1 = Piso(RUTA_BLOQUE_GRANDE, TAMAÑO_BLOQUE_GRANDE, POS_BLOQUE_GRANDE_1)
piso_bloque_grande_2 = Piso(RUTA_BLOQUE_GRANDE, TAMAÑO_BLOQUE_GRANDE, POS_BLOQUE_GRANDE_2)
piso_bloque_grande_3 = Piso(RUTA_BLOQUE_GRANDE, TAMAÑO_BLOQUE_GRANDE, POS_BLOQUE_GRANDE_3)
piso_bloque_grande_4 = Piso(RUTA_BLOQUE_GRANDE, TAMAÑO_BLOQUE_GRANDE, POS_BLOQUE_GRANDE_4)
piso_bloque_chico_1 = Piso(RUTA_BLOQUE_CHICO, TAMAÑO_BLOQUE_CHICO, POS_BLOQUE_CHICO_1)
piso_bloque_chico_2 = Piso(RUTA_BLOQUE_CHICO, TAMAÑO_BLOQUE_CHICO, POS_BLOQUE_CHICO_2)
piso_bloque_chico_3 = Piso(RUTA_BLOQUE_CHICO, TAMAÑO_BLOQUE_CHICO, POS_BLOQUE_CHICO_3)

LIMITE_ESCORPION_1_IZQ = piso_bloque_grande_1.rec.x
LIMITE_ESCORPION_2_IZQ = piso_bloque_grande_2.rec.x
LIMITE_ESCORPION_3_IZQ = piso_bloque_grande_3.rec.x
LIMITE_ESCORPION_4_IZQ = piso_bloque_grande_4.rec.x
LIMITE_ESCORPION_1_DER = LIMITE_ESCORPION_1_IZQ + piso_bloque_grande_1.base
LIMITE_ESCORPION_2_DER = LIMITE_ESCORPION_2_IZQ + piso_bloque_grande_2.base
LIMITE_ESCORPION_3_DER = LIMITE_ESCORPION_3_IZQ + piso_bloque_grande_3.base
LIMITE_ESCORPION_4_DER = LIMITE_ESCORPION_4_IZQ + piso_bloque_grande_4.base

luchador = Luchador(ruta_luchador, TAMAÑO_LUCHADOR, POS_LUCHADOR)

rec_game_over = Rectangulo(POS_REC_GAME_OVER, TAMAÑO_REC_GAME_OVER, COLOR_VERDE)
rec_reiniciar = Rectangulo(POS_REC_REINICIAR, TAMAÑO_REC_REINICIAR, COLOR_AZUL)

# veneno = Veneno()