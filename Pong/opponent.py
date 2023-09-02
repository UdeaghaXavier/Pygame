from variables import *
from pygame import Rect, draw

class Opponent:
    def __init__(self):
        self.height: int = 200
        self.width: int = 20
        self.x = self.width * 2
        self.y = height // 2
        
    def create_opponent(self):
        self.player = Rect(self.x, self.y, self.width, self.height)
        
    def draw_opponent(self):
        draw.rect(screen, WHITE, self.player)
        