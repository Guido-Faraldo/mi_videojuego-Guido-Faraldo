from Clases.personaje import Personaje

class Luchador(Personaje):

    def __init__(self, ruta, tamaño, pos):
        super().__init__(ruta, tamaño, pos)
