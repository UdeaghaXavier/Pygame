import random
import time

from variables import *
from Audio import Audio
from Wall import Wall

audio = Audio()
wall = Wall()
walls = wall.create_wall()

from Board import Board
# from _time import _time

board = Board()
player = board.create_board()

from Ball import Ball
from Heart import Heart
from Menu import Menu
from Display import Display

ball = Ball()
heart = Heart()
menu = Menu()
display = Display()
# Time = _time()