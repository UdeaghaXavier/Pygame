from variables import *

class Opponent:
    def __init__(self):
        self.height: int = 200
        self.width: int = 20
        self.x = self.width * 2
        self.y = height // 2 -  self.height // 2
        
        self.direction = 0
        self.opponent = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw_opponent(self):
        pygame.draw.rect(screen, WHITE, self.opponent)
        
    def stay_within_screen(self):
        if self.opponent.y < 0:
            self.opponent.y = 0
        elif self.opponent.y > (height - self.height):
            self.opponent.y = height - self.height
        
    def follow(self, ball):
    
        if ball.x < width / 2:
            if self.opponent.top > ball.top:
                self.direction = -1
            else:
                self.direction = 1
        else:
            self.direction = 0
            
        self.opponent.y += speed * self.direction
        self.stay_within_screen()
        