from Clases.imagen import Imagen

class Personaje(Imagen):
    
    def __init__(self, ruta, tamaño, posicion):
        super().__init__(ruta, tamaño, posicion)

    def mover_abajo(self, velocidad=10):
        self.posicion[1] += velocidad

    def mover_arriba(self, velocidad=25):
        self.posicion[1] -= velocidad

    def mover_izquierda(self, velocidad=3):
            self.posicion[0] -= velocidad

    def mover_derecha(self, velocidad=3):
            self.posicion[0] += velocidad