import pygame
import sys

pygame.init()

SCREEN = pygame.display.set_mode((800, 600))

rectangles = []
rect_speed = 5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                new_rect = pygame.Rect(50, 300, 50, 30)
                rectangles.append(new_rect)
                print("Aprete la tecla 'F'")

    SCREEN.fill((0, 0, 0))
    for rect in rectangles:
        pygame.draw.rect(SCREEN, (255, 255, 255), rect)
        rect.x += 5

    pygame.display.flip()
    pygame.time.Clock().tick(30)