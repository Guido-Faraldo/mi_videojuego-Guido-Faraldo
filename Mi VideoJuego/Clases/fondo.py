import pygame
from Clases.imagen import Imagen

class Fondo(Imagen):

    def __init__(self, ruta, tamaño, posicion):
        super().__init__(ruta, tamaño, posicion)