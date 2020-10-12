import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball(t, dt):
    global x, y, r, color, velocity_x, velocity_y
    if t == 0:
        r = randint(10, 100)
        x = randint(r, 1200 - r)
        y = randint(r, 900 - r)
        velocity_x = randint(-60, 60)
        velocity_y = randint(-60, 60)
        color = COLORS[randint(0, 5)]
    circle(screen, color, (round(x), round(y)), r)
    x += velocity_x * dt
    y += velocity_y * dt


pygame.display.update()
clock = pygame.time.Clock()
finished = False

score = 0
dt = 0.1
t = -dt
while not finished:
    clock.tick(FPS)
    screen.fill(BLACK)
    new_ball(t, dt)
    t += dt
    if x + r >= 1200 or x - r <= 0:
        velocity_x *= -1
    if y - r <= 0 or y + r >= 900:
        velocity_y *= -1
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] - x)**2 + (event.pos[1] - y)**2 <= r**2:
            t = 0
            score += 1
pygame.quit()
