import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

rectangles = []

class Rectangle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.growing = True

    def update(self):
        if self.growing:
            self.rect.inflate_ip(1, 1)  # Hacer el rectángulo más grande
            if self.rect.width >= 100:  # Detener el crecimiento
                self.growing = False

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

# Crea el rectángulo inicial
rectangles.append(Rectangle(100, 100, 50, 50))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for rect in rectangles:
        rect.update()

    # Crea nuevos rectángulos más pequeños dentro de los rectángulos existentes
    for rect in rectangles[:]:
        if not rect.growing:
            x, y, w, h = rect.rect.x, rect.rect.y, rect.rect.width, rect.rect.height
            new_width, new_height = w / 2, h / 2
            rectangles.append(Rectangle(x, y, new_width, new_height))

    screen.fill((0, 0, 0))

    for rect in rectangles:
        rect.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
