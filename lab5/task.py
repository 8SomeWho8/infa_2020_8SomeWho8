import pygame
import math as m
from pygame.draw import *
from random import *

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


def ballz(screen: pygame.surface, dt: float, n: int, x: list, y: list, velocity_x: list, velocity_y: list, r: list,
          color: list, hit: list):
    """
    This function creates targets shaped as circles and updates their position on the screen
    Circles are moving with constant velocity and bouncing off the edges of the screen
    :param screen: Object of class pygame.surface on which balls will be drawn
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


def ringz(screen: pygame.surface, t: list, n: int, x: list, y: list, x_0: list, y_0: list, a_x: list, a_y: list,
          r: list,
          freq: list, color: list, hit: list):
    """
    This function draws ring at coordinates (x, y) and updates its coordinates for the next frame.
    Rings are moving about the Lissajous figure with frequency ratio of 2:1.
    To hit a ring user must click on the colourful part.
    :param screen: Object of class pygame.surface on which rings will be drawn
    :param t: List of parameters of the current state of ring on the Lissajous figure
    :param x: List of horizontal coordinates of the rings
    :param y: List of vertical coordinates of the rings
    :param n: Number of rings created
    :param r: List of radii of rings
    :param x_0: List of starting horizontal coordinates of Lissajous figures
    :param y_0: List of starting vertical coordinates of Lissajous figures
    :param a_x: List of horizontal amplitudes of Lissajous figures
    :param a_y: List of vertical amplitudes of Lissajous figures
    :param hit: List of bool variables for each ring that is True if user has clicked on the ring
                and False if ring hasn't been clicked on.
                If this is True, function updates all variables of current ring.
    :param color: List of colours of rings
    :param freq: List of angular frequencies in formulas of Lissajous figures
    :return:
    """
    for i in range(n):
        # Recreating variables of ring randomly if it was clicked on
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
            t[i] = 0  # Updating the variable of state of each ring
        # Drawing a ring at current coordinates
        circle(screen, color[i], (round(x[i]), round(y[i])), r[i])
        circle(screen, BLACK, (round(x[i]), round(y[i])), r[i] - 7)
        # Updating coordinates of ring
        x[i] = x_0[i] + a_x[i] * m.cos(freq[i] * t[i])
        y[i] = y_0[i] + a_y[i] * m.sin(2 * freq[i] * t[i])


print("Enter your nickname, please:")
nickname = input()

pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 900))
n_1 = 5  # Number of circles created
# Creating lists of variables of circles with random values
r_1 = [randint(10, 100) for i in range(n_1)]  # List of radii of circles
x_1 = [randint(r_1[i], 1200 - r_1[i]) for i in range(n_1)]  # List of current horizontal coordinates of circles
y_1 = [randint(r_1[i], 900 - r_1[i]) for i in range(n_1)]  # List of current vertical coordinates of circles
velocity_x_1 = [randint(-100, 100) for i in range(n_1)]  # List of current horizontal velocities of circles
velocity_y_1 = [randint(-100, 100) for i in range(n_1)]  # List of current vertical velocities of circles
color_1 = [COLORS[randint(0, 11)] for i in range(n_1)]  # List of colours of circles
hit_1 = [False for i in
         range(n_1)]  # List of bool variables for each circle that is True if user has clicked on the circle
# and False if circle hasn't been clicked on.
dt = 0.1  # Step of time in drawing circles

n_2 = 5  # Number of rings created
# Creating lists of variables of rings with random values
a_x = [randint(50, 200) for i in range(n_2)]  # List of horizontal amplitudes of rings
a_y = [randint(50, 200) for i in range(n_2)]  # List of vertical amplitudes of rings
r_2 = [randint(10, 20) for i in range(n_2)]  # List of radii of rings
x_0 = [randint(a_x[i] + r_2[i], 1200 - a_x[i] - r_2[i]) for i in
       range(n_2)]  # List of starting horizontal coordinates of rings
y_0 = [randint(a_y[i] + r_2[i], 900 - a_y[i] - r_2[i]) for i in
       range(n_2)]  # List of starting vertical coordinates of rings
x_2 = [x_0[i] for i in range(n_2)]  # List of current horizontal coordinates of rings
y_2 = [y_0[i] for i in range(n_2)]  # List of current vertical coordinates of rings
color_2 = [COLORS[randint(0, 11)] for i in range(n_2)]  # List of colours of rings
hit_2 = [False for i in range(n_2)]  # List of bool variables for each ring that is True if user has clicked on the ring
# and False if ring hasn't been clicked on.
t = [randint(0, 1) for i in range(n_2)]  # List of states of time for each ring
freq = [random() * 0.4 + 0.3 for i in range(n_2)]  # List of angular frequencies for each ring

score = 0  # Score of the game
c_score = pygame.font.Font(None, 32)  # Preparing for displaying the score during game
length_of_round = 20  # Length of a game in seconds

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    screen.fill(BLACK)  # Filling the screen with black to redraw all picture
    # Drawing circles on current positions
    ballz(screen, dt, n_1, x_1, y_1, velocity_x_1, velocity_y_1, r_1, color_1, hit_1)
    # Drawing rings on current positions
    ringz(screen, t, n_2, x_2, y_2, x_0, y_0, a_x, a_y, r_2, freq, color_2, hit_2)
    length_of_round -= 1 / 60  # Reducing the variable of the length of the round to stop the round after needed seconds
    # Displaying current score and remaining time
    text = c_score.render("Score: " + str(score) +
                          "  Time left: " + '{:.2f}'.format(round(length_of_round, 2)) + "s", 1, AMBER)
    screen.blit(text, (0, 0))
    # Updating the variable of state for each ring
    for i in range(n_2):
        t[i] += dt
    # Checking the position of circles relative to edges in order to change the sign of horizontal or vertical velocity
    # if circle is going out of borders of the screen.
    for i in range(n_1):
        if x_1[i] + r_1[i] >= 1200 or x_1[i] - r_1[i] <= 0:
            velocity_x_1[i] *= -1
        if y_1[i] - r_1[i] <= 0 or y_1[i] + r_1[i] >= 900:
            velocity_y_1[i] *= -1
    pygame.display.update()
    # Checking if there is no time left and finishing the game if there is no left
    if length_of_round <= 0:
        finished = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Checking if user has clicked on a circle and changing the value of hit_1[i] of clicked circle
            for i in range(n_1):
                if (event.pos[0] - x_1[i]) ** 2 + (event.pos[1] - y_1[i]) ** 2 <= r_1[i] ** 2:
                    hit_1[i] = True
                    score += 1  # Adding a point for one clicked circle
            # Checking if user has clicked on a ring and changing the value of hit_2[i] of clicked ring
            for i in range(n_2):
                if r_2[i] ** 2 >= (event.pos[0] - x_2[i]) ** 2 + (event.pos[1] - y_2[i]) ** 2 >= (r_2[i] - 7) ** 2:
                    hit_2[i] = True
                    score += 10  # Adding ten points for each clicked ring

# Displaying result of the fame
screen.fill(LILAC)
f_score = pygame.font.Font(None, 100)
text2 = f_score.render("Your score is: " + str(score), 1, AMBER)
screen.blit(text2, (350, 400))
pygame.display.update()
finished = False
# Waiting for player to close the window of game
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()

# Saving the result of the player if his result is in top 10 results of all players
top10_r = open('top10.txt', 'r')
s = top10_r.readlines() # Saving the state of top10.txt file
top10_r.close()
top10_w = open('top10.txt', 'w')
if len(s) == 0:  # If top10.txt is empty writing a new result
    print('1. ' + nickname + ' ' + str(score), file=top10_w)
else:
    list_of_scores = []
    for i in range(len(s)):  # Reading scores from the file to create list of scores of all 10 players
        score_r = s[i][len(s[i]) - 2]
        j = len(s[i]) - 3
        while s[i][j] != ' ':
            score_r += s[i][j]
            j -= 1
        list_of_scores.append(int(score_r[::-1]))
    if score >= list_of_scores[0]:  # If player has achieved top 1 result number of a player "above" him is -1
        i_sup = -1
    else:  # Finding the supremum for player's score in list_of_scores
        i_sup = 0
        for i in range(len(list_of_scores)):
            if score < list_of_scores[i]:
                i_sup = i
    for i in range(len(s)):  # Deleting old positions for every player in top 10, for example "4. "
        s[i] = s[i][3:]
    s.insert(i_sup + 1, nickname + ' ' + str(score) + '\n')  # Adding player's result to top10 massive
    for i in range(len(s)):  # Adding new positions for every player in top 10
        s[i] = str(i + 1) + '. ' + s[i]
    # Writing top 10(or less) players in the file
    if len(s) > 10:
        top10_w.writelines(s[:len(s) - 1])
    else:
        top10_w.writelines(s)
top10_w.close()
