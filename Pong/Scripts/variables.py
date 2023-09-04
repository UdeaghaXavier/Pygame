import pygame
import random
import time
from Scripts.UI import Logic

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

print(__name__)
if __name__ == "Scripts.variables":
	logic = Logic()
	logic.main()

	board_color = logic.colour.rgb_former(logic.colour.board) if logic.colour.board else WHITE
	ball_color = logic.colour.rgb_former(logic.colour.ball) if logic.colour.ball else WHITE
	bg_color = logic.colour.rgb_former(logic.colour.bgcolor) if logic.colour.bgcolor else BLACK
colours = (BLACK, WHITE, RED)

CLock = pygame.time.Clock()
FPS: int = 60

size = (width, height) = 1500, 900
screen = pygame.display.set_mode(size)

default_speed = 7
