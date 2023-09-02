from variables import *
from pygame import Rect, draw

class Player:
    def __init__(self):
        self.height: int = 200
        self.width: int = 20
        self.x = width - (self.width * 2)
        self.y = height // 2
        
    def create_player(self):
        self.player = Rect(self.x, self.y, self.width, self.height)
        
    def draw_player(self):
        draw.rect(screen, WHITE, self.player)
        
    def move(self, direction:int):
        # Make sure the player-board is always within the screen
        if self.player.y < 0:
            self.player.y = 0
        elif self.player.y > (height - self.height):
            self.player.y = (height - self.height)
        else:
            self.player.y += speed * direction

        print(direction)