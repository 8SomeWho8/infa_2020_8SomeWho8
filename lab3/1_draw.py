import pygame
from pygame.draw import *

pygame.init()

YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
FPS = 30
a = 500  # сторона квадратного окна в пикселях

screen = pygame.display.set_mode((a, a))
rect(screen, WHITE, (0, 0, a, a))
circle(screen, YELLOW, (250, 250), 100)
circle(screen, BLACK, (250, 250), 100, 1)
rect(screen, BLACK, (200, 300, 100, 13))
# правый глаз
circle(screen, RED, (290, 220), 13)
circle(screen, BLACK, (290, 220), 13, 1)
circle(screen, BLACK, (290, 220), 7)
# левый глаз
circle(screen, RED, (210, 220), 25)
circle(screen, BLACK, (210, 220), 25, 1)
circle(screen, BLACK, (210, 220), 13)

polygon(screen, BLACK, [(270, 220), (320, 190), (314, 182), (264, 212)])
polygon(screen, BLACK, [(255, 220), (155, 160), (161, 152), (261, 212)])
pygame.display.update()

clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
