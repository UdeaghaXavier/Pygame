from variables import *

class Heart:
    def __init__(self):
        self.img = pygame.image.load("Assets/Images/heart.png")
    
    def draw_heart(self, lives):
        gap = 40
        x = 3
        y = 10
        for i in range(lives):
            WIN.blit(self.img, (x, y))
            x += gap