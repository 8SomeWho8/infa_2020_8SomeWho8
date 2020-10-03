import pygame
from pygame.draw import *


def legs(screen: pygame.display, cord_x: int, cord_y: int, size: float,
         colour_body: tuple):
    pass


def eye(screen: pygame.display, cord_x: int, cord_y: int, size: float,
        colour_eye_1: tuple, colour_eye_2: tuple):
    pass


def body(screen: pygame.display, cord_x: int, cord_y: int, size: float,
         colour_body: tuple):
    ellipse(screen, colour_body,
            (cord_x - size * 68, cord_y - size * 32, size * 2*68, size * 2*32))
    ellipse(screen, colour_body,
            ((cord_x + size * 57) - size * 19, (cord_y - size * 64) - size * 52, size * 2*19, size * 2*52))
    ellipse(screen, colour_body,
            ((cord_x + size * 67) - size * 24, (cord_y - size * 124) - size * 16, size * 2*24, size * 2*16))


def ears(screen: pygame.display, cord_x: int, cord_y: int, size: float,
         colour_body: tuple):
    pass


def llama(screen: pygame.display, cord_x: int, cord_y: int, size: float,
          colour_body: tuple, colour_eye_1: tuple, colour_eye_2: tuple):
    body(screen, cord_x, cord_y, size, colour_body)
    legs(screen, cord_x, cord_y, size, colour_body)
    eye(screen, cord_x, cord_y, size, colour_eye_1, colour_eye_2)
    ears(screen, cord_x, cord_y, size, colour_body)


def main():
    pygame.init()

    pixels_x = 600  # Количество пикселей в картинке по горизонтали
    pixels_y = 900  # Количетво пикселей в картинке по вертикали
    FPS = 30
    screen = pygame.display.set_mode((pixels_x, pixels_y))

    # Задание цветовых кортежей, нужных в рисунке
    CYAN = (175, 221, 233)
    GREY = (179, 179, 179)
    GREEN = (170, 222, 135)
    BLACK = (0, 0, 0)
    VIOLET = (229, 128, 255)
    WHITE = (255, 255, 255)

    # Заполнение всего экрана зелёным цветом, чтобы потом на него наложить небо и горы
    screen.fill(GREEN)

    # Прорисовка неба
    rect(screen, CYAN, (0, 0, pixels_x, 450))

    # Захардкоженная прорисовка гор, высчитывал в пеинте нижнюю линию, затем рисование контура
    # Извините за множество чисел :)
    polygon(screen, GREY, [(-1, 280), (70, 89), (125, 220), (205, 120), (358, 361), (468, 111), (503, 156), (601, 34),
                           (601, 533), (351, 533), (339, 528), (336, 526), (336, 526), (336, 481), (333, 478),
                           (333, 462),
                           (327, 453), (322, 453), (315, 450), (132, 450), (75, 460), (56, 460), (29, 463), (0, 476)])
    polygon(screen, BLACK, [(-1, 280), (70, 89), (125, 220), (205, 120), (358, 361), (468, 111), (503, 156), (601, 34),
                            (601, 533), (351, 533), (339, 528), (336, 526), (336, 526), (336, 481), (333, 478),
                            (333, 462),
                            (327, 453), (322, 453), (315, 450), (132, 450), (75, 460), (56, 460), (29, 463), (0, 476)],
            1)

    # Рисование одной ламы в определённых координатах с определёнными линейными размерами (за единицу взяты размеры ламы
    # с боевого задания)
    llama(screen, 143, 593, 1, WHITE, BLACK, VIOLET)



    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()


main()
