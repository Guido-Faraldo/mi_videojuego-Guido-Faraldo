import pygame

class Rectangulo:
    def __init__(self, posicion, tamaño, color, grozor=0):
        self.x = posicion[0]
        self.y = posicion[1]
        self.base = tamaño[0]
        self.altura = tamaño[1]
        self.rec = pygame.Rect(self.x, self.y, self.base, self.altura)
        self.color = color
        self.color_original = color
        self.grozor = grozor

    def dibujar(self, screen):
        pygame.draw.rect(screen, self.color, self.rec, self.grozor)

    def disappear(self):
        self.rec = pygame.Rect(0, 0, 0, 0)

    def recenter(self):
        self.rec = pygame.Rect(self.x, self.y, self.base, self.altura)

    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color

    def devolver_color(self):
        self.color = self.color_original

