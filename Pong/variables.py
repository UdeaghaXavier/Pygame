import pygame
import random

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

colours = (BLACK, WHITE, RED)
bg_color = BLACK

CLock = pygame.time.Clock()
FPS: int = 60

size = (width , height) = 1200, 600
screen = pygame.display.set_mode(size)

speed = 7