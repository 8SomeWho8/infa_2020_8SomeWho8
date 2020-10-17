import pygame
from pygame.draw import *
from random import randint

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
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, LILAC, AMBER, VINOUS]


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
            color[i] = (COLORS[randint(0, 8)])
            hit[i] = False
        # Drawing a circle at current state
        circle(screen, color[i], (round(x[i]), round(y[i])), r[i])
        # Updating coordinates of circles
        x[i] += velocity_x[i] * dt
        y[i] += velocity_y[i] * dt


clock = pygame.time.Clock()
finished = False

n = 10  # Number of circles created
r = []  # List of radii of circles
x = []  # List of current horizontal coordinates of circles
y = []  # List of current vertical coordinates of circles
velocity_x = []  # List of current horizontal velocities of circles
velocity_y = []  # List of current vertical velocities of circles
color = []  # List of colours of circles
hit = []  # List of bool variables for each circle that is True if user has clicked on the circle
# and False if circle hasn't been clicked.

# Creating lists of variables of circles with random values
for i in range(n):
    r.append(randint(10, 100))
    x.append(randint(r[i], 1200 - r[i]))
    y.append(randint(r[i], 900 - r[i]))
    velocity_x.append(randint(-100, 100))
    velocity_y.append(randint(-100, 100))
    color.append(COLORS[randint(0, 8)])
    hit.append(False)

# Score of the game
score = 0
# Step of time in drawing circles
dt = 0.1
while not finished:
    clock.tick(FPS)
    screen.fill(BLACK)  # Filling the screen with black to redraw all picture
    ballz(dt, n, x, y, velocity_x, velocity_y, r, color, hit)  # Drawing circles on current positions
    # Checking the position of circles relative to edges in order to change sign of horizontal or vertical velocity
    # if circle is going out of them.
    for i in range(n):
        if x[i] + r[i] >= 1200 or x[i] - r[i] <= 0:
            velocity_x[i] *= -1
        if y[i] - r[i] <= 0 or y[i] + r[i] >= 900:
            velocity_y[i] *= -1
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        # Checking if user has clicked on a circle and changing the value of hit[] of clicked circle
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(n):
                if (event.pos[0] - x[i]) ** 2 + (event.pos[1] - y[i]) ** 2 <= r[i] ** 2:
                    hit[i] = True
                    score += 1  # Adding one point for one clicked circle
print(score)
pygame.quit()
