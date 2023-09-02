import pygame

# My modules
from variables import *
from looks import Looks

pygame.init()

class Pong:
    def __init__(self):
        self.looks = Looks()
    
    def loop(self):
        running = True
        while running:
            screen.fill(self.looks.bg_color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.looks.draw_center_line()   
            pygame.display.update()     
        pygame.quit()
    
pong = Pong()
pong.loop()