from Clases.imagen import Imagen
from constantes import *

class Personaje(Imagen):
    
    def __init__(self, ruta, tamaño, posicion):
        super().__init__(ruta, tamaño, posicion)

    def mover_abajo(self):
        self.posicion[1] += 10

    def mover_arriba(self):
        self.posicion[1] -= 25

    def mover_izquierda(self):
        if self.posicion[0] > 0:
            self.posicion[0] -= 3

    def mover_derecha(self):
        if self.posicion[0] < ANCHO_VENTANA - self.base:
            self.posicion[0] += 3