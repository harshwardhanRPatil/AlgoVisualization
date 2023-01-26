import pygame
import random
from Messages import *


width = 850
Height = 700
white = (250, 250, 250)
red = (250, 0, 0)
blue = (0, 0, 250)
green=(0,250,0)
arr=[]
num=25
width1=30
space=3
arrange=[]
arrange1=[]
ans=[]

pygame.init()
icon = pygame.image.load("back..png")
# screen = pygame.display.set_mode((width, Height))
screen.fill((0, 0, 0))
clock = pygame.time.Clock()
pygame.display.update()


def draw():
    global arr,arrange
    for i in range(len(arr)):
        x=(i*width1)+(i*space)+15
        if i in arrange:
            pygame.draw.rect(screen,blue,(x,400,width1,20))
        elif i in arrange1:
            pygame.draw.rect(screen, red, (x, 400, width1, 20))
        elif i in ans:
            pygame.draw.rect(screen, green, (x, 400, width1, 20))
        else:
            pygame.draw.rect(screen, white, (x, 400, width1, 20))
        message(str(arr[i]),(x+(width1/2)),(400+(20/2)),20,(200,50,100))

def draw_box():
    global num ,arr
    for i in range(num):
        arr.append(random.randint(0,50))
    draw()
    print(arr)



def linear_search():
    find =22
    for i in range(len(arr)):
        if arr[i]==find:
            ans.append(i)
            break
        screen.fill((0,0,0))
        clock.tick(10000)
        draw()
        pygame.display.update()
    draw()
    pygame.display.update()

def Binary_Search():
    global arr,arrange,arrange1
    arr.sort()
    print(arr)
    find=22
    Start=0
    End=len(arr)-1
    while Start<End:
        arrange.clear()
        arrange1.clear()
        mid=(End+Start)
        if arr[mid]>find:
            End=mid-1
        elif arr[mid]<find:
            Start=mid
        else:
            ans.append(mid)
            break
        arrange1.append(Start)
        arrange1.append(End)
        arrange.append(mid)
        screen.fill((0,0,0))
        clock.tick(1)
        draw()
        pygame.display.update()
    draw()
    pygame.display.update()


def New_List():
    clear_all()
    draw_box()
    pygame.display.update()


def clear_all():
    arr.clear()
    arrange1.clear()
    arrange.clear()
    ans.clear()

def search_al():
    clear_all()
    screen.fill((0,0,0))
    draw_box()
    running = True
    while running:
        button("L_S", screen, (250, 250, 250), 50, 550, 70, 50, (0, 250, 50), (20,50,70), linear_search)
        button("B_S", screen, (250, 250, 250), 200, 550, 70, 50, (0, 250, 50), (0, 0, 120), Binary_Search)
        button("N_L", screen, (250, 250, 250), 400, 550, 70, 50, (0, 250, 50), (0, 0, 120), New_List)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == KEYDOWN:
                if event.key == K_q:
                    screen.blit(icon, (0, 0))
                    running = False

        pygame.display.update()
