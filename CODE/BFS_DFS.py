from tkinter import *
from tkinter import messagebox as mbox
import math
import random
from Messages import *
import pygame
from maze import *

red = (255, 0, 0)
width = 1000
height = 800
circle_num = 10
tick = 2
speed = 5

pygame.init()
icon = pygame.image.load("back..png")

clock = pygame.time.Clock()



class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Graph:
    def __init__(self, v):
        self.v = v
        self.adj = [None] * self.v

    def insert(self, scr, val):
        node = Node(val)
        node.next = self.adj[scr]
        self.adj[scr] = node

        # Adding the source node to the destination as
        # it is the undirected graph
        node = Node(scr)
        node.next = self.adj[val]
        self.adj[val] = node

    def draw(self):
        global c
        for i in range(self.v):
            temp = self.adj[i]
            while temp:
                pygame.draw.line(screen, (250, 0, 100), c[i], c[temp.val])
                temp = temp.next

    def bfs(self, val):
        visit = [0] * self.v
        order = []
        order.append(val)
        visit[val] = 1

        while order:
            print(order)
            a = order.pop(0)
            # pygame.draw.circle(screen, (150, 200, 10),a, 10)
            #print(f"{a}->", end=" ")
            i = self.adj[a]

            while i:
                if visit[i.val] == 0:
                    order.append(i.val)
                    visit[i.val] = 1

                i = i.next
            if len(order) > 0:
                pygame.draw.line(screen, (250, 0, 0), c[a], c[order[0]], 5)
                pygame.display.update()
                clock.tick(1)

    def dfs(self, val1, visit):
        if visit[val1] == 0:
            visit[val1] = 1
            print(f"{val1}->", end=" ")
            temp = self.adj[val1]
            while temp:
                if visit[temp.val] == 0:
                    pygame.draw.line(screen, (250, 20, 0), c[val1], c[temp.val], 5)
                    pygame.display.update()
                    clock.tick(1)
                    self.dfs(temp.val, visit)
                temp = temp.next


g = Graph(10)
g.insert(0, 7)
g.insert(0, 1)
g.insert(0, 2)
g.insert(0, 3)
g.insert(0, 4)
g.insert(0, 5)
g.insert(0, 6)

g.insert(1, 2)
g.insert(1, 3)
g.insert(1, 4)
g.insert(2, 0)
g.insert(2, 4)
g.insert(3, 0)
g.insert(5, 1)
g.insert(5, 0)
g.insert(4, 3)
g.insert(6, 5)
g.insert(6, 7)
g.insert(7, 5)
g.insert(8, 5)
g.insert(8, 2)
g.insert(9, 0)
g.insert(9, 4)
g.insert(9, 7)

c = []


def draw():
    global g
    c.clear()
    screen.fill((250, 250, 250))
    for i in range(10):

        m = [random.randint(10, width - 100), random.randint(1, 600)]
        # print(m)
        pygame.draw.circle(screen, (150, 200, 10), m, 10)
        # button(i, screen, (250, 100, 250), m[0],m[1], 5,5,(0, 250, 50), (0, 0, 120), draw)

        c.append(m)
    g.draw()

    pygame.display.update()


def BFS():
    g.bfs(0)


def dfs():
    visit = [0] * 10
    g.dfs(5, visit)


def Travel():
    screen.fill((250, 250, 250))
    draw()

    running = True
    while running:
        button("NEW GRAPH ", screen, (250, 100, 250), 550, 630, 150, 50, (0, 250, 50), (0, 0, 120), draw)
        button("BFS ", screen, (250, 100, 250), 150, 630, 150, 50, (0, 250, 50), (0, 0, 120), BFS)
        button("DFS ", screen, (250, 100, 250), 350, 630, 150, 50, (0, 250, 50), (0, 0, 120), dfs)
        button("maze ", screen, (250, 100, 250), 750, 630, 150, 50, (0, 250, 50), (0, 0, 120), maze)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == KEYDOWN:
                if event.key == K_q:
                    c.clear()
                    screen.blit(icon, (0, 0))
                    running = False

        pygame.display.update()
