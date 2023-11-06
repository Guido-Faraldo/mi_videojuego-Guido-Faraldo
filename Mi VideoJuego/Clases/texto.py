import pygame

class Texto:
    def __init__(self, texto:str, color:tuple, posicion:tuple, fuente:pygame.font.Font):
        self.texto = texto
        self.color = color
        self.posicion = posicion
        self.fuente = fuente
        self.texto_invisible = ""

    def mostrar_texto(self, screen):
        texto = self.fuente.render(self.texto, True, self.color)
        screen.blit(texto, self.posicion)

    def desaparcer_texto(self, screen):
        texto = self.fuente.render(self.texto_invisible, True, self.color)
        screen.blit(texto, self.posicion)