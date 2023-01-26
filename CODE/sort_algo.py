import pygame
import random
from Messages import *

width = 100
Height = 700
white = (250, 250, 250)
red = (250, 0, 0)
blue = (0, 0, 250)
green = (0, 250, 0)
arrange = []
arr = []

num = 230
space = 1

pygame.init()
icon = pygame.image.load("back..png")
clock = pygame.time.Clock()


def draw(colour):
    global arr, Height, num, arrange, space

    for i in range(num):
        x = (i * 3) + (i * space) + 50
        if i in arrange:
            pygame.draw.rect(screen, green, (x, 0, 3, arr[i]))
        else:
            pygame.draw.rect(screen, colour, (x, 0, 3, arr[i]))
        # pygame.draw.rect(screen, (139, 250, 212), (0, 0, 60, 700))
        # pygame.draw.rect(screen, (139, 250, 212), (790, 0, 100, 700))


def draw_line():
    global arr, num
    arr.clear()
    arrange.clear()
    for i in range(num):
        x = random.randint(50, 500)
        arr.append(x)
        random.shuffle(arr)
    draw((250, 250, 250))


def merge():
    global arr
    merge_sort(arr, 0, len(arr))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


def merge_sort(alist, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(alist, start, mid)
        merge_sort(alist, mid, end)

        screen.fill((150, 10, 150))
        draw((250, 250, 250))

        # button(None, screen, (0, 150, 200), 0, 0, 60, 700, (0, 150, 200), (0, 150, 200), None)
        # button(None, screen, (0, 150, 200), 760, 0, 100, 700, (0, 150, 200), (0, 150, 200), None)
        pygame.display.update()

        merge_list(alist, start, mid, end)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


def merge_list(alist, start, mid, end):
    left = alist[start:mid]
    right = alist[mid:end]
    k = start
    i = 0
    j = 0
    arrange.clear()
    while start + i < mid and mid + j < end:
        if left[i] <= right[j]:
            alist[k] = left[i]
            i = i + 1
        else:
            alist[k] = right[j]
            j = j + 1
        k = k + 1
        arrange.append(k)

    if start + i < mid:
        while k < end:
            alist[k] = left[i]
            i = i + 1
            k = k + 1
            arrange.append(k)
    else:
        while k < end:
            alist[k] = right[j]
            j = j + 1
            k = k + 1
        arrange.append(k)
    screen.fill((150, 10, 150))
    # clock.tick(10)
    draw((250, 250, 250))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


# bubble sort
def bubble_sort():
    global arr

    for i in range(len(arr)):
        sorted1 = 0
        for j in range(len(arr) - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted1 = 1

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
        arrange.append(j + 1)
        if sorted1 == 0:
            arrange.extend(range[0:j+1])
            break
        else:
            screen.fill((150, 10, 150))
            draw((250, 250, 0))
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


# seletion sort algo
def selection_sort():
    global arr
    for i in range(len(arr)):
        min = arr[i]
        index = i
        for j in range(i, len(arr) - 1):
            screen.fill((150, 10, 150))
            draw((250, 250, 250))
            if min > arr[j + 1]:
                min = arr[j + 1]
                index = j + 1
                arr[i], arr[index] = arr[index], arr[i]
            arrange.append(i)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    draw((0, 250, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.update()


# quick sort algo
# and in algo for it

def quick():
    global arr
    quickSort(arr, 0, len(arr) - 1)


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        arrange.append(pi)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]  # pivot

    for j in range(low, high):

        screen.fill((150, 10, 150))
        draw((250, 250, 250))
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
        pygame.display.update()

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    draw((0, 250, 0))
    clock.tick(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    return (i + 1)


# algo for heap  sort



def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2

def max_heapify(alist, index, size):
    l = left(index)
    r = right(index)
    if l < size and alist[l] > alist[index]:
        largest = l
    else:
        largest = index
    if r < size and alist[r] > alist[largest]:
        largest = r
    if largest != index:
        alist[largest], alist[index] = alist[index], alist[largest]
        max_heapify(alist, largest, size)
    screen.fill((150, 10, 150))
    draw((250, 250, 250))
    pygame.display.update()



def build_max_heap(alist):
    length = len(alist)-1
    start = parent(length - 1)
    # while start >= -1:
    for i in range(length//2 , -1, -1):
        max_heapify(alist, index=i, size=length)
        # start = start - 1
    screen.fill((150, 10, 150))
    draw((250, 250, 250))
    pygame.display.update()


def heapsort():
    global arr
    build_max_heap(arr)
    for i in range(len(arr) - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, index=0, size=i)
        pygame.display.update()






# button for the main screen
# and for other sort


# button for sort
# and main method for algo

def sort_algo():
    screen.fill((150, 10, 150))
    draw_line()
    running = True
    while running:

        button("Buuble Sort", screen, (250, 250, 250), 10, 650, 150, 30, (0, 250, 50), (0, 0, 120), bubble_sort)
        button("Selection Sort", screen, (250, 250, 250), 175, 650, 150, 30, (0, 250, 50), (0, 0, 120), selection_sort)
        button("New Array", screen, (250, 250, 250), 335, 650, 150, 30, (0, 250, 50), (0, 0, 120), swap)
        button("Merge Sort", screen, (250, 250, 250), 500, 650, 150, 30, (0, 250, 50), (0, 0, 120), merge)
        button("Quick Sort", screen, (250, 250, 250), 670, 650, 150, 30, (0, 250, 50), (0, 0, 120), quick)
        button("Heap Sort", screen, (250, 250, 250), 840, 650, 150, 30, (0, 250, 50), (0, 0, 120), heapsort)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == KEYDOWN:
                if event.key == K_q:
                    screen.blit(icon, (0, 0))
                    running = False

        pygame.display.update()


def swap():
    global arr
    screen.fill((0, 0, 0))
    draw_line()
    pygame.display.update()
