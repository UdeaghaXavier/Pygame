from variables import *

class Display:
    def __init__(self):
        self.size = 100
        self.font = pygame.font.SysFont("Assets/Fonts/ARCADE.TTF", self.size)
        self.pos_lost = (WIDTH//2 - self.size * 2.3, HEIGHT//4 + self.size * 3)
        self.colour = BLACK
        self.now = 0

    def lost(self):
        png = pygame.image.load("Assets/Images/lost.png")
        WIN.blit(png, (0, 0))

        text = self.font.render("GAME OVER", True, (0, 0, 0))
        WIN.blit(text, self.pos_lost)