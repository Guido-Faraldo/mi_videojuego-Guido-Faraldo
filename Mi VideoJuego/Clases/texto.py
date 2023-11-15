import pygame

class Texto:
    def __init__(self, texto:str, color:tuple, posicion, fuente:pygame.font.Font):
        self.texto = texto
        self.color = color
        self.posicion = posicion
        self.fuente = fuente
        self.texto_original = texto
        self.texto_invisible = ""

    def mostrar_texto(self, screen):
        texto = self.fuente.render(self.texto, True, self.color)
        screen.blit(texto, self.posicion)

    def volver_texto_normalidad(self):
        self.texto = self.texto_original

    def desaparcer_texto(self):
        self.texto = self.texto_invisible

    def mostrar_texto_con_saltos(self, screen):
        self.posicion = [40, 35]
        for linea in self.texto.split('\n'):
            texto = self.fuente.render(linea, True, self.color)
            screen.blit(texto, self.posicion)
            self.posicion[1] += 32