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

r_1 = randint(10, 100)
x_1 = randint(r_1, 1200 - r_1)
y_1 = randint(r_1, 900 - r_1)
velocity_x_1 = randint(-60, 60)
velocity_y_1 = randint(-60, 60)
color_1 = COLORS[randint(0, 5)]

r_2 = randint(10, 100)
x_2 = randint(r_2, 1200 - r_2)
y_2 = randint(r_2, 900 - r_2)
velocity_x_2 = randint(-60, 60)
velocity_y_2 = randint(-60, 60)
color_2 = COLORS[randint(0, 5)]

r_3 = randint(10, 100)
x_3 = randint(r_3, 1200 - r_3)
y_3 = randint(r_3, 900 - r_3)
velocity_x_3 = randint(-60, 60)
velocity_y_3 = randint(-60, 60)
color_3 = COLORS[randint(0, 5)]


def new_ball(x, y, r, velocity_x, velocity_y, color, t, dt):  #FIX ME
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
t = 0
while not finished:
    clock.tick(FPS)
    screen.fill(BLACK)
    new_ball(x_1, y_1, r_1, velocity_x_1, velocity_y_1, color_1, t, dt)
    new_ball(x_2, y_2, r_2, velocity_x_2, velocity_y_2, color_2, t, dt)
    new_ball(x_3, y_3, r_3, velocity_x_3, velocity_y_3, color_3, t, dt)
    t += dt
    if x_1 + r_1 >= 1200 or x_1 - r_1 <= 0:
        velocity_x_1 *= -1
    if y_1 - r_1 <= 0 or y_1 + r_1 >= 900:
        velocity_y_1 *= -1
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] - x)**2 + (event.pos[1] - y)**2 <= r**2:
            t = 0
            score += 1
pygame.quit()
