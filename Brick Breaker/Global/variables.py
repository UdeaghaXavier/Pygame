import pygame
from random import randint
from math import sin, cos, degrees


pygame.init()
pygame.display.set_caption("Brick Breaker")

screen_res = (640, 640)
bricks_region = (screen_res[0], screen_res[0] * 2 / 4)

clock = pygame.Clock()
FPS = 60

col = {"black": (0, 0, 0), "dark-greyish-brown": (70, 70, 70)}
