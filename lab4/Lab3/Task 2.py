import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((700, 800))

def eli(x, y):
    ellipse(screen, x, y)
def rec(x, y):
    rect(screen, x, y)
def circ(x, y, z):
    circle(screen, x, y, z)
    
#Sky
rec((171, 171, 171), (0, 0, 700, 300))
#Moon
circ((255, 255, 255), (630, 70), 50)
#Clouds
eli((135, 135, 135), (400, 115, 600, 45))
eli((51, 51, 51), (320, 170, 500, 50))

#House

#Base
rec((51, 38, 0), (30, 170, 350, 400))
#Lower windows
for i in range(2):
    rec((51, 18, 0), (65+i*105, 440, 70, 80))
rec((255, 204, 0), (275, 440, 70, 80))
#Upper windows
for i in range(4):
    rec((89, 89, 89), (72+i*77, 170, 40, 128))
#Fance
rec((26, 26, 26), (0, 300, 410, 40))
rec((26, 26, 26), (20, 250, 370, 20))
#Bars of the fence
for i in range(2):
    rec((26, 26, 26), (10+i*380, 270, 10, 30))
for i in range(5):
    rec((26, 26, 26), (65+i*65, 270, 20, 30))
#Pipes
rec((26, 26, 26), (256, 100, 10, 60))
#Roof
polygon(screen, (0, 0, 0), [[72, 130], [0, 170], [410, 170], [338, 130]])
#Pipes
rec((26, 26, 26), (114, 100, 10, 55))
#Clouds
eli((102, 102, 102), (30, 60, 550, 58))
eli((127, 127, 127), (300, 40, 400, 50))
#Pipes
rec((26, 26, 26), (129, 60, 20, 100))
rec((26, 26, 26), (333, 100, 10, 60))

#Ghost

#Ghost's head 
circ((191, 191, 191), (550, 570), 30)
#Ghost's body
a = (191, 191, 191)
polygon(screen, a, [[530, 570], [460, 720], [680, 670], [590, 560]])
eli(a, (500, 600, 30, 100))
eli(a, (480, 650, 30, 50))
eli((0, 0, 0), (455, 700, 80, 30))
eli(a, (510, 650, 70, 60))
eli((0, 0, 0), (580, 680, 80, 30))
eli(a, (630, 660, 50, 30))
eli(a, (605, 610, 50, 60))
eli(a, (555, 553, 43, 60))
#Ghost's eyes
circ((102, 194, 255), (535, 570), 8)
circ((102, 194, 255), (560, 565), 8)
circ((0, 0, 0), (532, 570), 2)
circ((0, 0, 0), (558, 565), 2)
polygon(screen, (255, 255, 255), [[558, 562], [560, 564], [564, 560], [562, 558]])
polygon(screen, (255, 255, 255), [[532, 567], [534, 569], [538, 565], [536, 563]])


pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
