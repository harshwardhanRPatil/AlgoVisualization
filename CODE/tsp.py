import pygame
import random
import math
from Messages import *

light_Green = (100, 250, 0)
Red = (250, 0, 0)
width = 850
Height = 700
v = []
reached = []
unreached = []

pygame.init()
icon = pygame.image.load("back..png")


clock = pygame.time.Clock()


def clear_screen():
    screen.fill((0, 0, 0))
    v.clear()


def TSP1():
    global v
    unsolved = v.copy()
    solution = []
    n = unsolved[0]
    solution.append(n)

    while unsolved:
        min_l = None
        min_c = None

        for i, c in enumerate(unsolved):
            d = math.hypot(n[0] - c[0], n[1] - c[1])
            if min_l is None:
                min_c = c
                min_l = d
                index = i
            elif d < min_l:
                min_l = d
                min_c = c
                index = i

        pygame.display.update()
        clock.tick(1)
        pygame.draw.line(screen, (0, 0, 250), (n), (min_c))

        solution.append(unsolved[index])
        unsolved.pop(index)
        n = min_c

    pygame.display.update()
    pygame.draw.line(screen, (0, 0, 250), (n), (solution[0]))


def TSP():
    global v
    v.clear()
    screen.fill((0, 0, 0))
    running = True
    while running:

        planet_color = (255, 0, 0)
        planet_radius = 10
        circ = pygame.mouse.get_pos()
        try:
            button("CLEAR", screen, (250, 250, 250), 100, 620, 300, 50, (0, 250, 0), (0, 0, 120), clear_screen)
            button("Traveling Salesman Problem", screen, (250, 250, 250), 550, 620, 300, 50, (0, 250, 0), (0, 0, 120), TSP1)
        except:
            print("no input")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(v)
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 0 < circ[0] < 800 and 600 < circ[1] < 730:
                    continue
                else:
                    pygame.draw.circle(screen, planet_color, (circ), planet_radius)
                    v.append(list(circ))

            elif event.type == KEYDOWN:
                if event.key == K_q:
                    screen.blit(icon, (0, 0))
                running = False

    pygame.display.update()
