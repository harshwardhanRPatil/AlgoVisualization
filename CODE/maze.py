import pygame
import random
from Messages import *

width = 600
Height = 600
pygame.init()
# screen = pygame.display.set_mode((width, Height))
# screen.fill((250, 250, 250))
w = 20

clock = pygame.time.Clock()


class Cube:
    def __init__(self, x, y):
        self.path_vist = True
        self.x = x
        self.y = y
        self.visit = False
        self.wall = [True, True, True, True]
        self.path_visit = False
        self.parent = self.x + self.y * col

    def draw_wall(self):
        i = self.x * w
        j = self.y * w

        if self.wall[0]:
            pygame.draw.line(screen, (0, 250, 250), (i, j + w), (i, j), 3)

        if self.wall[1]:
            pygame.draw.line(screen, (0, 250, 250), (i + w, j + w), (i, j + w), 3)

        if self.wall[2]:
            pygame.draw.line(screen, (0, 250, 250), (i + w, j + w), (i + w, j), 3)

        if self.wall[3]:
            pygame.draw.line(screen, (0, 250, 250), (i, j), (i + w, j), 3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()

    def next_cube(self, i, j):
        if i < 0 or j < 0 or j > col - 1 or i > col - 1:
            return -1
        print(1 + 0 * col)
        return i + j * col

    def wall1(self):
        return self.visit

    def next_cell(self):

        neb = []
        left = grid[self.next_cube(self.x, self.y - 1)]
        bottom = grid[self.next_cube(self.x + 1, self.y)]
        right = grid[self.next_cube(self.x, self.y + 1)]
        top = grid[self.next_cube(self.x - 1, self.y)]

        if self.next_cube(self.x - 1, self.y) != -1 and top.visit == False:
            neb.append(top)

        if self.next_cube(self.x, self.y + 1) and right.wall1() != True:
            neb.append(right)

        if self.next_cube(self.x + 1, self.y) != -1 and bottom.wall1() != True:
            neb.append(bottom)

        if self.next_cube(self.x, self.y - 1) != -1 and left.wall1() != True:
            neb.append(left)

        if len(neb) > 1:
            side = random.randint(0, len(neb) - 1)
            return neb[side]
        elif len(neb) == 1:
            return neb[0]
        else:
            return -1

    def path_exist(self):
        self.path_visit = True
        neb = []

        left = grid[self.next_cube(self.x, self.y - 1)]
        bottom = grid[self.next_cube(self.x + 1, self.y)]
        right = grid[self.next_cube(self.x, self.y + 1)]
        top = grid[self.next_cube(self.x - 1, self.y)]

        if self.next_cube(self.x - 1, self.y) != -1 and top.path_visit == False and self.wall[0] != True:
            pygame.draw.rect(screen, (250, 100, 100), ((top.x * w) + 5, (top.y * w) + 5, w - 10, w - 10))
            top.path_visit = True
            top.parent = self.x + self.y * col
            neb.append(top)

        if self.next_cube(self.x, self.y + 1) and right.path_visit == False and self.wall[1] != True:
            pygame.draw.rect(screen, (250, 100, 100), ((right.x * w) + 5, (right.y * w) + 5, w - 10, w - 10))
            right.path_visit = True
            right.parent = self.x + self.y * col
            neb.append(right)

        if self.next_cube(self.x + 1, self.y) != -1 and bottom.path_visit == False and self.wall[2] != True:
            pygame.draw.rect(screen, (250, 100, 100), ((bottom.x * w) + 5, (bottom.y * w) + 5, w - 10, w - 10))
            bottom.path_visit = True
            bottom.parent = self.x + self.y * col
            neb.append(bottom)

        if self.next_cube(self.x, self.y - 1) != -1 and left.path_visit != True and self.wall[3] != True:
            pygame.draw.rect(screen, (250, 100, 100), ((left.x * w) + 5, (left.y * w) + 5, w - 10, w - 10))
            left.path_visit = True
            left.parent = self.x + self.y * col
            neb.append(left)

        return neb

    def remove_wall(self, cube):

        position_X = self.x - cube.x
        position_Y = self.y - cube.y

        self.visit = True
        cube.visit = True

        if position_X == -1:
            self.wall[2] = False
            cube.wall[0] = False

        if position_X == 1:
            self.wall[0] = False
            cube.wall[2] = False

        if position_Y == -1:
            self.wall[1] = False
            cube.wall[3] = False

        if position_Y == 1:
            self.wall[3] = False
            cube.wall[1] = False


class BFS(Cube):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def b_f_s(self, start):
        draw_path = [grid[start]]
        draw_path[0].path_vist = True

        while draw_path:
            a = draw_path.pop(0)

            path = a.path_exist()
            clock.tick(30)

            for i in path:
                if i == grid[self.end]:
                    break
                else:
                    draw_path.append(i)
            if i == grid[self.end]:
                j = i
                while j != grid[self.start]:
                    pygame.draw.rect(screen, (0, 0, 250), ((j.x * w) + 5, (j.y * w) + 5, w - 10, w - 10))
                    clock.tick(15)
                    j = grid[j.parent]
                    print(j)
                    pygame.display.update()
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    exit()

            pygame.display.update()


class DFS:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def path_finder(self, start):
        v1 = [grid[start]]

        v1[0].path_vist = True

        while v:
            a = v1.pop(-1)

            path = a.path_exist()
            # clock.tick(1)

            for i in path:
                if i == grid[self.end]:
                    break
                else:
                    v1.append(i)
            if i == grid[self.end]:
                j = i
                while j != grid[self.start]:
                    pygame.draw.rect(screen, (0, 0, 250), ((j.x * w) + 5, (j.y * w) + 5, w - 10, w - 10))
                    clock.tick(15)
                    j = grid[j.parent]
                    print(j)
                    pygame.display.update()
                break
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    exit()


v = []
row = 600 // w
col = 600 // w
grid = []


def clean_path():
    for j, i in enumerate(grid):
        i.parent = j
        i.path_visit = False


def dfs():
    clean_path()
    start = (v[0][0] // w) + ((v[0][1] // w) * col)
    end = (v[1][0] // w) + ((v[1][1] // w) * col)
    print(f"{start} {end}")
    A = DFS(start, end)
    A.path_finder(start)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()


def bfs():
    clean_path()
    if len(v)==0:
        return
    start = (v[0][0] // w) + ((v[0][1] // w) * col)
    end = (v[1][0] // w) + ((v[1][1] // w) * col)
    print(f"{start} {end}")
    A = BFS(start, end)
    A.b_f_s(start)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

# def maze():
# grid.clear()
for j in range(row):
    for i in range(col):
        cell = Cube(i, j)
        grid.append(cell)


def draw_wall():
    screen.fill((0, 0, 0))
    for i in range(len(grid)):
        grid[i].draw_wall()
    # pygame.display.update()


def maze_genretor():
    # maze()
    for_recurtion = [grid[0]]

    while for_recurtion:

        # if len(next_list)>0:
        #     current = next_list.pop()
        current = for_recurtion[-1]

        side = current.next_cell()

        # print(for_recurtion)
        if side != -1:
            current.remove_wall(side)
            draw_wall()
            pygame.display.update()
            for_recurtion.append(side)


        else:
            current = for_recurtion.pop()

        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


def Start_pos():
    global v
    planet_color = (255, 0, 0)
    i = 0
    v.clear()
    while i < 2:
        circ = pygame.mouse.get_pos()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()

            if 610 < circ[0] < 700 or 610 < circ[1] < 700:
                continue


            elif event.type == pygame.MOUSEBUTTONDOWN:
                x = circ[0] // w
                y = circ[1] // w
                pygame.draw.rect(screen, planet_color, ((x * w) + 5, (y * w) + 5, w - 10, w - 10))
                v.append(circ)
                i += 1
                pygame.display.update()

def maze():
    running = True
    screen.fill((250, 250, 250))
    while running:

        button("MAZE", screen, (250, 250, 250), 380, 600, 90, 50, (0, 250, 0), (0, 0, 120), maze_genretor)
        button("Start", screen, (250, 250, 250), 240, 600, 90, 50, (0, 250, 0), (0, 0, 120), Start_pos)
        button("bfs", screen, (250, 250, 250), 100, 600, 90, 50, (0, 250, 0), (0, 0, 120), bfs)
        button("dfs", screen, (250, 250, 250), 520, 600, 90, 50, (0, 250, 0), (0, 0, 120), dfs)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
            if event.type == KEYDOWN:
                if event.key == K_q:
                    screen.blit(icon, (0, 0))
                    running = False
        pygame.display.update()
