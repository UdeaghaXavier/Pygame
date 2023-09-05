import pygame
import random
import time
from Scripts.UI.UI_Start import Logic, rgb_former
from Scripts.Audio_Manager import AudioManager

pygame.init()

AudioManager = AudioManager()

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

if __name__ == "Scripts.variables":  # If pong.py instantiated this module
    logic = Logic()
    logic.main()

    board_color = rgb_former(logic.colour.board) if logic.colour.board else WHITE
    ball_color = rgb_former(logic.colour.ball) if logic.colour.ball else WHITE
    bg_color = rgb_former(logic.colour.bg_color) if logic.colour.bg_color else BLACK

colours = (BLACK, WHITE, RED)

CLock = pygame.time.Clock()
FPS: int = 60

size = (width, height) = 1500, 900
screen = pygame.display.set_mode(size)

default_speed = 7
