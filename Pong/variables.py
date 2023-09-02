import pygame
import random

# Colours
BLACK: tuple = (0, 0, 0)
WHITE: tuple = (255, 255, 255)
bg_color = BLACK

CLock = pygame.time.Clock()
FPS: int = 60

size = (width , height) = 1200, 600
screen = pygame.display.set_mode(size)

speed = 7
direction = 0