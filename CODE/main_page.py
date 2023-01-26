import pygame
from sort_algo import *
from MST_algo import *
from search_algo import *
from Messages import *
from tsp import *
from BFS_DFS import *
from maze import *

light_Green = (100, 250, 0)
Red = (250, 0, 0)
width = 1000
Height = 700

pygame.init()
screen = pygame.display.set_mode((width, Height))
screen.fill((0, 0, 0))
icon = pygame.image.load("back..png")
screen.blit(icon, (0, 0))
running = True
while running:



    # message("Algo Visulation", (100 + (width / 2)), (100 + (Height / 10)), 70, (100, 100, 150), True, False)
    # pygame.draw.line(screen, Red, (0, 10), (width, 10), 5)
    # pygame.draw.line(screen, (0, 100, 0), (0, 130), (width, 130), 5)

    button("Sorting", screen, (250, 100, 250),  80, 600, 150, 40, (0, 250, 50), (0, 0, 120), sort_algo)
    button("Search", screen, (250, 100, 250),  5+250, 600, 150, 40, (0, 250, 50), (0, 0, 120), search_al)
    button("M_S_T", screen, (250, 100, 250), 50+550, 600, 150, 40, (0, 250, 50), (0, 0, 120), MST)
    button("T_S_P", screen, (250, 100, 250), 30+400, 600, 150, 40, (0, 250, 50), (0, 0, 120), TSP)
    button("Travel", screen, (250, 100, 250), 70 + 700, 600, 150, 40, (0, 250, 50), (0, 0, 120), Travel)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

    pygame.display.update()
