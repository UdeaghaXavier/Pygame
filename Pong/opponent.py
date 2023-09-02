from variables import *

class Opponent:
    def __init__(self):
        self.height: int = 200
        self.width: int = 20
        self.x = self.width * 2
        self.y = height // 2 -  self.height // 2
        
        self.opponent = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw_opponent(self):
        pygame.draw.rect(screen, WHITE, self.opponent)
        