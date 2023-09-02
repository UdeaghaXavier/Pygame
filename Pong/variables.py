from pygame import display, time

# Colours
BLACK: tuple = (0, 0, 0)
WHITE: tuple = (255, 255, 255)
bg_color = BLACK

CLock = time.Clock()
FPS: int = 60

size = (width , height) = 1200, 600
screen = display.set_mode(size)

speed = 7
direction = 0