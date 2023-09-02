import pygame

# My modules
from variables import * # Contains the needed global variables
from looks import Looks # Everything that is'nt related to the ball, player and opponent is in here
from player import Player 
from opponent import Opponent

pygame.init()

looks = Looks()
player = Player()
player.create_player()
opponent = Opponent()
opponent.create_opponent()

UP = (pygame.K_UP, pygame.K_w)
DOWN = (pygame.K_DOWN, pygame.K_s)

class Pong:
    def __init__(self):
        self.player = player.player
        self.direction = 0
        
    def loop(self):
        running = True
        while running:
            screen.fill(bg_color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key in UP:
                        self.direction -= 1
                    if event.key in DOWN:
                        self.direction += 1

                if event.type == pygame.KEYUP:
                    if event.key in UP:
                        self.direction += 1
                    if event.key in DOWN:
                        self.direction -= 1

            
            looks.draw_center_line() 
            player.draw_player()
            opponent.draw_opponent()
            player.move(self.direction)
            
            CLock.tick(FPS) 
            pygame.display.update()     


pong = Pong()
pong.loop()
pygame.quit()