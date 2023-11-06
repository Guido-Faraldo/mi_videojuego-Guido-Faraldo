import pygame

class Imagen:

    def __init__(self, ruta:str, tamaño:tuple, posicion):
        self.ruta = ruta
        self.tamaño = tamaño
        self.base = tamaño[0]
        self.altura = tamaño[1]
        self.imagen = pygame.image.load(self.ruta)
        self.imagen_escalada = pygame.transform.scale(self.imagen, self.tamaño)
        self.escalada_original = pygame.transform.scale(self.imagen, self.tamaño)
        self.rec = self.imagen_escalada.get_rect()
        self.rec_original = self.escalada_original.get_rect()
        self.posicion = posicion
        self.rec.x = posicion[0]
        self.rec.y = posicion[1]
        self.color_rec = (0, 255, 0)

    def desaparecer_imagen(self):
        self.imagen_escalada = pygame.transform.scale(self.imagen_escalada, (0, 0))

    def restaurar_imagen(self):
        self.imagen_escalada = self.escalada_original

    def dibujar_rectangulo(self, screen):
        pygame.draw.rect(screen, self.color_rec, self.rec, 2)

    def cargar_imagen(self, screen):
        screen.blit(self.imagen_escalada, self.rec)

    def desaparecer_rectangulo(self):
        self.rec = pygame.Rect(0, 0, 0, 0)

    def restaurar_rectangulo(self):
        self.rec = pygame.Rect(self.posicion[0], self.posicion[1], self.base, self.altura)