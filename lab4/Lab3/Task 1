import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

#Background 
rect(screen, (127, 127, 127), (0, 0, 400, 400))
#Face
circle(screen, (0, 0, 0), (200, 200), 100, 1)
circle(screen, (250, 250, 0), (200, 200), 99)
#Eyes
circle(screen, (0, 0, 0), (155, 170), 20, 2)
circle(screen, (255, 0, 0), (155, 170), 19)
circle(screen, (0, 0, 0), (155, 170), 10)
circle(screen, (0, 0, 0), (250, 170), 15, 2)
circle(screen, (255, 0, 0), (250, 170), 14)
circle(screen, (0, 0, 0), (250, 170), 7)
#Mouth
rect(screen, (0, 0, 0), (150, 250, 100, 18))
#Eyebrows
polygon(screen, (0, 0, 0), [[120, 118], [115, 123], [185, 168], [190, 163]])
polygon(screen, (0, 0, 0), [[220, 163], [225, 168], [300, 128], [295, 123]])

pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
