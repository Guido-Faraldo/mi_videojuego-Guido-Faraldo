from Clases.personaje import Personaje

class Escorpion(Personaje):

    def __init__(self, ruta, tamaño, posicion):
        super().__init__(ruta, tamaño, posicion)

    def mover_escorpiones(self, direccion_escorpion, limite_i, limite_d, rutas_escorpion):
        if direccion_escorpion == "Derecha":
            self.mover_derecha()
            if self.rec.x + self.base >= limite_d:
                self.ruta = rutas_escorpion[1]
                direccion_escorpion = "Izquierda"
        elif direccion_escorpion == "Izquierda":
            self.mover_izquierda()
            if self.rec.x <= limite_i:
                self.ruta = rutas_escorpion[0]
                direccion_escorpion = "Derecha"
        
        return self.ruta, direccion_escorpion
