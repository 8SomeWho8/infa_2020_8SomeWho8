import pygame
from pygame.draw import *


pygame.init()

pixels_x = 800
pixels_y = 1200
FPS = 30
screen = pygame.display.set_mode((pixels_x, pixels_y))
pygame.display.update()

CYAN = (0, 0.6*255, 0.6*255)


rect(screen, CYAN, (0, 0, pixels_x, 450))

clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()