import pygame
from pygame.draw import *


def eli(screen: pygame.Surface, x: tuple, y: tuple):
    """
    This function draws an ellipse like ellipse in pygame
    :param screen: object with type pygame.Surface on which we draw an ellipse
    :param x: horizontal coordinate of top left corner of rectangular in which ellipse is centred
    :param y: vertical coordinate of top left corner of rectangular in which ellipse is centred
    :return:
    """
    ellipse(screen, x, y)


def rec(screen: pygame.Surface, x: tuple, y: tuple):
    """
    This function draws an rectangular like rectangular in pygame
    :param screen: object with type pygame.Surface on which we draw a rectangular
    :param x: horizontal coordinate of top left corner of rectangular
    :param y: vertical coordinate of top left corner of rectangular
    :return:
    """
    rect(screen, x, y)


def circ(screen: pygame.Surface, x: tuple, y: tuple, radius: int):
    """
    This function draws an circle like circle in pygame
    :param screen: object with type pygame.Surface on which we draw a circle
    :param x: horizontal coordinate of top left corner of square where circle is centred
    :param y: vertical coordinate of top left corner of square where circle is centred
    :return:
    """
    circle(screen, x, y, radius)


def house(screen: pygame.Surface, x, y, size: float, alpha: int):
    """
    This function draws a house
    :param screen: - object with type pygame.Surface on which we draw a house
    :param x: - horizontal coordinate of top left corner of house (without roof)
    :param y: - vertical coordinate of top left corner of house (without roof)
    :param size: - coefficient of linear size of the house. If size == 1, draws a "standart" house
    :param alpha: - coefficient of transparency which maximum is 255 - most opaque and minimum is 0 - most transparent
    :return:
    """

    # Creating surface on which a house will be drawn
    surface_house = pygame.Surface((700, 800))
    surface_house.set_alpha(alpha)  # this command makes our house transparent or opaque
    surface_house.fill((0, 0, 255))
    surface_house.set_colorkey((0, 0, 255))

    # Base
    rec(surface_house, (51, 38, 0), (x, y, round(size * 200), round(size * 250)))

    # Lower windows
    for i in range(2):
        rec(surface_house, (51, 18, 0), (x + round(size * 20) + round(size * i * 60),
                                         y + round(size * 150), round(size * 40), round(size * 60)))
    rec(surface_house, (255, 204, 0), (x + round(size * 20) + round(size * 2 * 60), y + round(size * 150),
                                       round(size * 40), round(size * 60)))

    # Upper windows
    for i in range(4):
        rec(surface_house, (89, 89, 89), (x + round(size * 16) + round(size * i * 46),
                                          y, round(size * 30), round(size * 120)))
    # Fence
    rec(surface_house, (26, 26, 26), (x - round(size * 10), y + round(size * 105),
                                      round(size * 220), round(size * 20)))
    rec(surface_house, (26, 26, 26), (x - round(size * 5), y + round(size * 80),
                                      round(size * 210), round(size * 10)))

    # Bars of the fence
    for i in range(2):
        rec(surface_house, (26, 26, 26), (x - round(size * 10) + round(size * i * 215), y + round(size * 90),
                                          round(size * 5), round(size * 15)))
    for i in range(5):
        rec(surface_house, (26, 26, 26), (x + round(size * 20) + round(size * i * 37), y + round(size * 90),
                                          round(size * 12), round(size * 15)))

    # Pipes
    rec(surface_house, (26, 26, 26), (x + round(size * 133), y - round(size * 40), round(size * 5), round(size * 30)))

    # Roof
    polygon(surface_house, (0, 0, 0), [[x + round(size * 16), y - round(size * 20)],
                                       [x - round(size * 10), y], [x + round(size * 210), y], [x + round(size * 184),
                                                                                               y - round(size * 20)]])
    # Pipes
    rec(surface_house, (26, 26, 26), (x + round(size * 41), y - round(size * 40), round(size * 5), round(size * 30)))
    rec(surface_house, (26, 26, 26), (x + round(size * 52), y - round(size * 60), round(size * 10), round(size * 50)))
    rec(surface_house, (26, 26, 26), (x + round(size * 179), y - round(size * 45), round(size * 5), round(size * 35)))
    screen.blit(surface_house, [0, 0])


def ghost(screen: pygame.Surface, x: int, y: int, size: float, orientation: bool):
    """
    This function draws a ghost
    :param screen: - object with type pygame.Surface on which we draw a ghost
    :param x: - horizontal coordinate of the center of its head
    :param y: - vertical coordinate of the center of its head
    :param orientation - True if ghost is turned on the left False if it is turned on the right
    :param size: - coefficient of linear size of the ghost. If size == 1, draws a "standart" ghost
    :return:
    """

    # Creating surface on which ghost will be drawn
    surface_ghost = pygame.Surface((700, 800))
    surface_ghost.fill((0, 0, 255))
    surface_ghost.set_colorkey((0, 0, 255))
    surface_ghost.set_alpha(150)

    # Ghost's head
    circ(surface_ghost, (191, 191, 191), (x, y), round(size * 20))

    # Ghost's body
    grey = (191, 191, 191)

    # Here we draw rectangular of the main shape of ghost's body
    polygon(surface_ghost, grey, [[x - round(size * 10), y], [x - round(size * 60), y + round(size * 100)],
                                  [x + round(size * 80), y + round(size * 60)],
                                  [x + round(size * 20), y - round(size * 5)]])

    # Here we draw ellipses that make the body of ghost more smooth

    # top grey ellipse on the left side of ghost
    eli(surface_ghost, grey, (x - round(size * 35), y + round(size * 30), round(size * 20), round(size * 60)))
    # down grey ellipse on the left side of ghost
    eli(surface_ghost, grey, (x - round(size * 50), y + round(size * 60), round(size * 20), round(size * 30)))
    # left black ellipse on the bottom of ghost
    eli(surface_ghost, (0, 0, 0), (x - round(size * 65), y + round(size * 85), round(size * 50), round(size * 20)))
    # left grey ellipse on the bottom of ghost
    eli(surface_ghost, grey, (x - round(size * 30), y + round(size * 60), round(size * 50), round(size * 30)))
    # right black ellipse on the bottom of ghost
    eli(surface_ghost, (0, 0, 0), (x + round(size * 20), y + round(size * 65), round(size * 60), round(size * 20)))
    # right grey ellipse on the bottom of ghost
    eli(surface_ghost, grey, (x + round(size * 50), y + round(size * 50), round(size * 30), round(size * 20)))
    # down grey ellipse on left side of ghost
    eli(surface_ghost, grey, (x + round(size * 25), y + round(size * 15), round(size * 30), round(size * 40)))
    # top grey ellipse on left side of ghost
    eli(surface_ghost, grey, (x + round(size * 5), y - round(size * 10), round(size * 23), round(size * 40)))

    # Ghost's eyes
    circ(surface_ghost, (102, 194, 255), (x - round(size * 10), y), round(size * 5))
    circ(surface_ghost, (102, 194, 255), (x + round(size * 10), y - round(size * 5)), round(size * 5))
    circ(surface_ghost, (0, 0, 0), (x - round(size * 12), y), round(size * 2))
    circ(surface_ghost, (0, 0, 0), (x + round(size * 8), y - round(size * 5)), round(size * 2))

    if not orientation:
        surface_ghost = pygame.transform.flip(surface_ghost, True, False)

    screen.blit(surface_ghost, [0, 0])


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
house(screen, 10, 350, 1, 255)
house(screen, 240, 270, 1, 255)

# Transparent house
house(screen, 480, 150, 1, 150)

# ghosts on the right
ghost(screen, 600, 500, 1, True)
ghost(screen, 660, 590, 1, True)
ghost(screen, 450, 570, 1.5, True)
ghost(screen, 470, 670, 1, True)

# reversed ghost on the left
ghost(screen, 600, 650, 1, False)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
