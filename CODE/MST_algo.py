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
    screen.fill((0,0,0))
    v.clear()

def prim_algo():
    unreached.clear()
    reached.clear()
    for i in range(len(v)):
        unreached.append(v[i])

    start = v[0]
    reached.append(start)
    unreached.pop(0)

    while unreached:
        distance = 1000000
        print(f"{v}  {unreached}  {reached}")

        for i in range(len(reached)):
            for j in range(len(unreached)):
                v1 = reached[i]
                v2 = unreached[j]
                x1 = v1[0]
                y1 = v1[1]
                x2 = v2[0]
                y2 = v2[1]
                d = math.hypot(x1 - x2, y1 - y2)

                print(f"{d}")

                if d < distance:
                    distance = d
                    rIndex = i
                    uIndex = j

        pygame.display.update()
        clock.tick(30)
        print(f"{distance}")
        pygame.draw.line(screen, (0, 0, 250), (reached[rIndex]), (unreached[uIndex]),5)
        clock.tick(30)
        reached.append(unreached[uIndex])
        unreached.pop(uIndex)


parent = []
rank = []


def make_set(vertice):
    parent.insert(vertice,vertice)
    rank.insert(vertice, 0)


def find(v1):
    root = v1
    while root != parent[root]:
        root = parent[root]

    while v1 != root:
        side = parent[v1]
        parent[v1] = root
        v1 = side
    return root

def union(vertice1,vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


def K_algo():
    global v
    array = []
    unreached1 = v.copy()
    n = unreached1.pop(0)
    index1 = 0
    m = 1
    while unreached1:

        for j,c in enumerate(unreached1):
            d = math.hypot((n[0] - c[0])**2+(n[1] - c[1])**2)
            array.append((index1,j+m,d))
        n = unreached1.pop(0)
        index1 = index1+1
        m+=1
    array.sort(key=lambda x:x[2])

    print(array)

    for vertice in range(len(v)):
        print(vertice)
        make_set(vertice)
        minimum_spanning_tree = set()

        # print edges
    for edge in array:
        v01, v02, weight = edge
        if find(v01) != find(v02):
            union(v01, v02)
            minimum_spanning_tree.add(edge)
            pygame.display.update()
            clock.tick(10)
            pygame.draw.line(screen,(250,0,0),(v[v01]),(v[v02]),3)


def TSP():
    global v
    unsolved = v.copy()
    solution = []
    n = unsolved[0]
    solution.append(n)

    while unsolved:
        min_l = None
        min_c = None

        for i,c in enumerate(unsolved):
            d = math.hypot(n[0]-c[0],n[1]-c[1])
            if min_l is None:
                min_c = c
                min_l = d
                index = i
            elif d < min_l:
                min_l = d
                min_c = c
                index = i

        pygame.display.update()
        clock.tick(40)
        pygame.draw.line(screen, (0, 0, 250), (n),(min_c))

        solution.append(unsolved[index])
        unsolved.pop(index)
        n = min_c

    pygame.display.update()
    pygame.draw.line(screen, (0, 0, 250), (n), (solution[0]))


def MST():

    global v
    v.clear()
    screen.fill((0, 0, 0))
    running = True
    while running:

        planet_color = (255, 0, 0)
        planet_radius = 10
        circ = pygame.mouse.get_pos()

        try:
            button("K_Ago", screen, (250, 250, 250), 600, 600, 170, 50, (0, 250, 0), (0, 0, 120), K_algo)
            button("prime", screen, (250, 250, 250), 200, 600, 170, 50, (0, 250, 0), (0, 0, 120),prim_algo)
            button("CLEAR", screen, (250, 250, 250), 400, 600, 170, 50, (0, 250, 0), (0, 0, 120), clear_screen)
            # button("TSP", screen, (250, 250, 250), 300, 650, 70, 50, (0, 250, 0), (0, 0, 120),TSP)
        except:
            print("no")
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
