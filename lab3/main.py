import pygame
from pygame.draw import *
pygame.init()
screen = pygame.display.set_mode((300, 200))
surface = pygame.Surface([200, 100], pygame.SRCALPHA)
pygame.draw.ellipse(surface, (255, 255, 255), [10, 20, 180, 80])
surface_rot = pygame.transform.rotate(surface, 13)
screen.fill((128, 0, 128))
screen.blit(surface_rot, [50, 50])

pygame.display.update()

FPS = 30
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
