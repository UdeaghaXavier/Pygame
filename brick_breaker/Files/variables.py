import pygame

pygame.init()
SIZE = (WIDTH, HEIGHT) = 600, 800
WIN = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# Colours
BLACK = (0, 0, 0)
PEACH = (234, 218, 184)
RED = (242, 85, 96)
GREEN = (86, 174, 87)
GREY = (150, 150, 150)
DARK_GREEN = (0, 37, 16)
BLUE = (69, 177, 232)
LIGHT_BROWN = (77, 52, 6)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 50

running = True
lives = 4
can_draw = True
displayed = False
started = False
stop = False

cols = 6
rows = 6
speed = 0
increment = 5
bouncing = False

top = pygame.Rect(0, 0, WIDTH, 60)

LEFT = (pygame.K_a, pygame.K_LEFT)
RIGHT = (pygame.K_d, pygame.K_RIGHT)