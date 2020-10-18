import pygame
import math as m
from pygame.draw import *
from random import *

pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 900))

# Lists of colours used in program
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
LILAC = (182, 102, 210)
AMBER = (255, 191, 0)
VINOUS = (113, 25, 25)
RED_CORAL = (255, 127, 80)
BLUE_STEEL = (80, 127, 255)
LIME = (204, 255, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, LILAC, AMBER, VINOUS, RED_CORAL, BLUE_STEEL, LIME]


def ballz(dt: float, n: int, x: list, y: list, velocity_x: list, velocity_y: list, r: list, color: list, hit: list):
    """
    This function creates targets shaped as circles and updates their position on the screen
    Circles are moving with constant velocity and bouncing off the edges of the screen
    :param dt: Step of time in movement of circles
    :param n: Number of circles
    :param x: List of current horizontal coordinates of circles
    :param y: List of current vertical coordinates of circles
    :param velocity_x: List of current horizontal velocities of circles
    :param velocity_y: List of current vertical velocities of circles
    :param r: List of radii of circles
    :param color: List of colours of circles
    :param hit: List of bool variables for each circle that is True if user has clicked on the circle
                and False if circle hasn't been clicked on.
                If this is True, function updates all variables of current circle.
    :return:
    """
    for i in range(n):
        # Recreating variables of circle randomly if it was clicked on
        if hit[i]:
            r[i] = (randint(10, 100))
            x[i] = (randint(r[i], 1200 - r[i]))
            y[i] = (randint(r[i], 900 - r[i]))
            velocity_x[i] = (randint(-100, 100))
            velocity_y[i] = (randint(-100, 100))
            color[i] = (COLORS[randint(0, 11)])
            hit[i] = False
        # Drawing a circle at current state
        circle(screen, color[i], (round(x[i]), round(y[i])), r[i])
        # Updating coordinates of circles
        x[i] += velocity_x[i] * dt
        y[i] += velocity_y[i] * dt


def ringz(t: list, x: list, y: list, n: int, r: list, x_0: list, y_0: list, a_x: list, a_y: list, hit: list,
          color: list, freq: list):
    for i in range(n):
        if hit[i]:
            a_x[i] = (randint(50, 200))
            a_y[i] = (randint(50, 200))
            r_2[i] = (randint(10, 20))
            x_0[i] = (randint(a_x[i] + r_2[i], 1200 - a_x[i] - r_2[i]))
            y_0[i] = (randint(a_y[i] + r_2[i], 900 - a_y[i] - r_2[i]))
            x_2[i] = (x_0[i])
            y_2[i] = (y_0[i])
            color_2[i] = (COLORS[randint(0, 11)])
            freq[i] = random() * 0.4 + 0.3
            hit_2[i] = False
            t[i] = 0
        circle(screen, color[i], (round(x[i]), round(y[i])), r[i])
        circle(screen, BLACK, (round(x[i]), round(y[i])), r[i] - 7)
        x[i] = x_0[i] + a_x[i] * m.cos(freq[i] * t[i])
        y[i] = y_0[i] + a_y[i] * m.sin(2 * freq[i] * t[i])


clock = pygame.time.Clock()
finished = False
n_1 = 0  # Number of circles created
r_1 = []  # List of radii of circles
x_1 = []  # List of current horizontal coordinates of circles
y_1 = []  # List of current vertical coordinates of circles
velocity_x_1 = []  # List of current horizontal velocities of circles
velocity_y_1 = []  # List of current vertical velocities of circles
color_1 = []  # List of colours of circles
hit_1 = []  # List of bool variables for each circle that is True if user has clicked on the circle
# and False if circle hasn't been clicked on.

# Creating lists of variables of circles with random values
for i in range(n_1):
    r_1.append(randint(10, 100))
    x_1.append(randint(r_1[i], 1200 - r_1[i]))
    y_1.append(randint(r_1[i], 900 - r_1[i]))
    velocity_x_1.append(randint(-100, 100))
    velocity_y_1.append(randint(-100, 100))
    color_1.append(COLORS[randint(0, 11)])
    hit_1.append(False)

n_2 = 5  # Number of rings created
r_2 = []  # List of radii of rings
x_2 = []  # List of current horizontal coordinates of rings
y_2 = []  # List of current vertical coordinates of rings
a_x = []  # List of horizontal amplitudes of rings
a_y = []  # List of vertical amplitudes of rings
x_0 = []  # List of starting horizontal coordinates of rings
y_0 = []  # List of starting vertical coordinates of rings
color_2 = []  # List of colours of rings
hit_2 = []  # List of bool variables for each ring that is True if user has clicked on the ring'
t = []  # List of states of time for each ring
# and False if ring hasn't been clicked on.
freq = []
for i in range(n_2):
    a_x.append(randint(50, 200))
    a_y.append(randint(50, 200))
    r_2.append(randint(10, 20))
    x_0.append(randint(a_x[i] + r_2[i], 1200 - a_x[i] - r_2[i]))
    y_0.append(randint(a_y[i] + r_2[i], 900 - a_y[i] - r_2[i]))
    x_2.append(x_0[i])
    y_2.append(y_0[i])
    freq.append(random() * 0.4 + 0.3)
    color_2.append(COLORS[randint(0, 11)])
    hit_2.append(False)
    t.append(randint(0, 1))

# Score of the game
score = 0
# Step of time in drawing circles
dt = 0.1
while not finished:
    clock.tick(FPS)
    screen.fill(BLACK)  # Filling the screen with black to redraw all picture
    ballz(dt, n_1, x_1, y_1, velocity_x_1, velocity_y_1, r_1, color_1, hit_1)  # Drawing circles on current positions
    ringz(t, x_2, y_2, n_2, r_2, x_0, y_0, a_x, a_y, hit_2, color_2, freq)
    for i in range(n_2):
        t[i] += dt
    # Checking the position of circles relative to edges in order to change sign of horizontal or vertical velocity
    # if circle is going out of them.
    for i in range(n_1):
        if x_1[i] + r_1[i] >= 1200 or x_1[i] - r_1[i] <= 0:
            velocity_x_1[i] *= -1
        if y_1[i] - r_1[i] <= 0 or y_1[i] + r_1[i] >= 900:
            velocity_y_1[i] *= -1
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        # Checking if user has clicked on a circle and changing the value of hit[] of clicked circle
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i in range(n_1):
                if (event.pos[0] - x_1[i]) ** 2 + (event.pos[1] - y_1[i]) ** 2 <= r_1[i] ** 2:
                    hit_1[i] = True
                    score += 1  # Adding one point for one clicked circle
            for i in range(n_2):
                if r_2[i] ** 2 >= (event.pos[0] - x_2[i]) ** 2 + (event.pos[1] - y_2[i]) ** 2 >= (r_2[i] - 7) ** 2:
                    hit_2[i] = True
                    score += 10


print(score)
pygame.quit()
