import pygame
from pygame.locals import *

width = 850
Height = 700

pygame.init()
screen = pygame.display.set_mode((width, Height))
screen.fill((100, 100, 100))


def text_obj(text, font, c):
    textSurface = font.render(text, True, c)
    return textSurface, textSurface.get_rect()


def message(text, x, y, size, c, b=False, i=True):
    Large_text = pygame.font.SysFont("Arial", size, bold=b, italic=i)
    TextSurf, TextRect = text_obj(text, Large_text, c)
    TextRect.center = ((x), (y))
    screen.blit(TextSurf, TextRect)


def button(Text, windows, col, x, y, w, h, ac, ic, Action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and h + y > mouse[1] > y:
        pygame.draw.rect(windows, ac, (x, y, w, h))
        if click[0] == 1 and Action is not None:
            Action()
    else:
        pygame.draw.rect(windows, col, (x, y, w, h))
    message(Text, (x + (w / 2)), (y + (h / 2)), 20, (0,0,0))
    pygame.display.update()
