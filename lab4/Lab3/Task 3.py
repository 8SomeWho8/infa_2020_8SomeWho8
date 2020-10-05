import pygame
from pygame.draw import *


def eli(screen: pygame.Surface, x: tuple, y: tuple):
    ellipse(screen, x, y)


def rec(screen: pygame.Surface, x: tuple, y: tuple):
    rect(screen, x, y)


def circ(screen: pygame.Surface, x: tuple, y: tuple, radius: int):
    circle(screen, x, y, radius)


def house(screen: pygame.Surface, x, y, size: float):
    # Base
    rec(screen, (51, 38, 0), (x, y, round(size * 200), round(size * 250)))
    # Lower windows
    for i in range(2):
        rec(screen, (51, 18, 0), (x + round(size * 20) + round(size * i * 60),
                                  y + round(size * 150), round(size * 40), round(size * 60)))
    rec(screen, (255, 204, 0), (x + round(size * 20) + round(size*2 * 60), y + round(size * 150),
                                round(size * 40), round(size * 60)))
    # Upper windows
    for i in range(4):
        rec(screen, (89, 89, 89), (x + round(size * 16) + round(size * i * 46),
                                   y, round(size * 30), round(size * 120)))
    # Fence
    rec(screen, (26, 26, 26), (x - round(size * 10), y + round(size * 105),
                               round(size * 220), round(size * 20)))
    rec(screen, (26, 26, 26), (x - round(size * 5), y + round(size * 80),
                               round(size * 210), round(size * 10)))
    # Bars of the fence
    for i in range(2):
        rec(screen, (26, 26, 26), (x - round(size * 10) + round(size * i * 215), y + round(size * 90),
                                   round(size * 5), round(size * 15)))
    for i in range(5):
        rec(screen, (26, 26, 26), (x + round(size * 20) + round(size * i * 37), y + round(size * 90),
                                   round(size * 12), round(size * 15)))
    # Pipes
    rec(screen, (26, 26, 26), (x + round(size * 133), y - round(size * 40), round(size * 5), round(size * 30)))
    # Roof
    polygon(screen, (0, 0, 0), [[x + round(size * 16), y - round(size * 20)],
                                [x - round(size * 10), y], [x + round(size * 210), y], [x + round(size * 184),
                                                                                        y - round(size * 20)]])
    # Pipes
    rec(screen, (26, 26, 26), (x + round(size * 41), y - round(size * 40), round(size * 5), round(size * 30)))
    rec(screen, (26, 26, 26), (x + round(size * 52), y - round(size * 60), round(size * 10), round(size * 50)))
    rec(screen, (26, 26, 26), (x + round(size * 179), y - round(size * 45), round(size * 5), round(size * 35)))


def ghost(screen: pygame.Surface, x: int, y: int, size: float):
    """
    This function draws a ghost
    :param screen: - object with type pygame.Surface on which we draw a ghost
    :param x: - horizontal coordinate of the center of its head
    :param y: - vertical coordinate of the center of its head
    :param size: - coefficient of linear size of the ghost. If size == 1, draws a "standart" ghost
    :return:
    """
    # Ghost's head
    circ(screen, (191, 191, 191), (x, y), round(size * 20))

    # Ghost's body
    grey = (191, 191, 191)

    # Here we draw rectangular of the main shape of ghost's body
    polygon(screen, grey, [[x - round(size * 10), y], [x - round(size * 60), y + round(size * 100)],
                           [x + round(size * 80), y + round(size * 60)], [x + round(size * 20), y - round(size * 5)]])

    # Here we draw ellipses that make the body of ghost more smooth

    # top grey ellipse on the left side of ghost
    eli(screen, grey, (x - round(size * 35), y + round(size * 30), round(size * 20), round(size * 60)))
    # down grey ellipse on the left side of ghost
    eli(screen, grey, (x - round(size * 50), y + round(size * 60), round(size * 20), round(size * 30)))
    # left black ellipse on the bottom of ghost
    eli(screen, (0, 0, 0), (x - round(size * 65), y + round(size * 85), round(size * 50), round(size * 20)))
    # left grey ellipse on the bottom of ghost
    eli(screen, grey, (x - round(size * 30), y + round(size * 60), round(size * 50), round(size * 30)))
    # right black ellipse on the bottom of ghost
    eli(screen, (0, 0, 0), (x + round(size * 20), y + round(size * 65), round(size * 60), round(size * 20)))
    # right grey ellipse on the bottom of ghost
    eli(screen, grey, (x + round(size * 50), y + round(size * 50), round(size * 30), round(size * 20)))
    # down grey ellipse on left side of ghost
    eli(screen, grey, (x + round(size * 25), y + round(size * 15), round(size * 30), round(size * 40)))
    # top grey ellipse on left side of ghost
    eli(screen, grey, (x + round(size * 5), y - round(size * 10), round(size * 23), round(size * 40)))

    # Ghost's eyes
    circ(screen, (102, 194, 255), (x - round(size * 10), y), round(size * 5))
    circ(screen, (102, 194, 255), (x + round(size * 10), y - round(size * 5)), round(size * 5))
    circ(screen, (0, 0, 0), (x - round(size * 12), y), round(size * 2))
    circ(screen, (0, 0, 0), (x + round(size * 8), y - round(size * 5)), round(size * 2))


def transparent_house(surface_house: pygame.Surface, x, y, size: float):
    surface_house.fill((0, 0, 255))
    house(surface_house, 480, 150, size)
    surface_house.set_alpha(150)
    surface_house.set_colorkey((0, 0, 255))
    screen.blit(surface_house, [0, 0])


pygame.init()

FPS = 30
screen = pygame.display.set_mode((700, 800))

# Sky
rec(screen, (171, 171, 171), (0, 0, 700, 300))

# Moon
circ(screen, (255, 255, 255), (630, 70), 50)

# Clouds
eli(screen, (135, 135, 135), (400, 115, 600, 45))
eli(screen, (51, 51, 51), (320, 170, 500, 50))
eli(screen, (102, 102, 102), (30, 60, 550, 58))
eli(screen, (127, 127, 127), (300, 40, 400, 50))

# Houses
house(screen, 10, 350, 1)
house(screen, 240, 270, 1)

# Transparent house
surface_house = pygame.Surface((700, 800))
transparent_house(surface_house, 480, 150, 1)

# ghosts on the right
surface_ghost = pygame.Surface((700, 800))
surface_ghost.fill((0, 0, 255))
surface_ghost.set_alpha(150)
surface_ghost.set_colorkey((0, 0, 255))
ghost(surface_ghost, 600, 500, 1)
ghost(surface_ghost, 660, 590, 1)
ghost(surface_ghost, 450, 570, 1.5)
ghost(surface_ghost, 600, 700, 1)
screen.blit(surface_ghost, [0, 0])


# reversed ghost on the left
surface_ghost_reversed = pygame.Surface((700, 800))
surface_ghost_reversed.fill((0, 0, 255))
surface_ghost_reversed.set_alpha(150)
ghost(surface_ghost_reversed, 600, 650, 1)
surface_ghost_reversed.set_colorkey((0, 0, 255))
surface_ghost_reversed = pygame.transform.flip(surface_ghost_reversed, True, False)
screen.blit(surface_ghost_reversed, [0, 0])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
