import pygame
from pygame.draw import *
pygame.init()
screen = pygame.display.set_mode((600, 900))
ear_points_1 = []
ear_points_2 = []
size = 1
for i in range(14):
    ear_points_1.append((i, round(-19 / 14 ** 2 * (i - 14) ** 2 + 19)))
    ear_points_2.append((i, round(-17 / 14 ** 2 * (i - 14) ** 2 + 17)))
surface = pygame.Surface((round(size * 18), round(size * 24)), pygame.SRCALPHA)
polygon(surface, [255, 255, 255], ear_points_1 + ear_points_2[::-1])

screen.fill((128, 0, 128))
screen.blit(surface, [50, 50])

pygame.display.update()

FPS = 30
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
