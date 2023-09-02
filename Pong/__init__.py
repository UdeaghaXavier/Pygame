import pygame

# My modules
from variables import *
from looks import Looks

pygame.init()
pygame.display.set_mode(size)

class Pong:
    def __init__(self):
        self.looks = Looks()
    
    def loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
        pygame.quit()
    
pong = Pong()
pong.loop()