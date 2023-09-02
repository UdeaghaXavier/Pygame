# My modules
from variables import * # Contains the needed global variables
from looks import Looks # Everything that is'nt related to the ball, player and opponent is in here
from player import Player 
from opponent import Opponent
from ball import Ball

pygame.init()

looks = Looks()
player = Player()
opponent = Opponent()
ball = Ball()

UP = (pygame.K_UP, pygame.K_w)
DOWN = (pygame.K_DOWN, pygame.K_s)
PLAY = (pygame.K_SPACE)

class Pong:
    def __init__(self):
        self.player = player.player
        self.opponent = opponent.opponent
        self.ball = ball.ball
        
        self.direction = 0
        self.running = True
    
    def handle_input_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
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
   
    
    def loop(self):
        while self.running:
            screen.fill(bg_color)
            
            self.handle_input_events()
            looks.draw_center_line() 
            player.draw_player()
            opponent.draw_opponent()
            opponent.follow(self.ball)
            player.move(self.direction)
            ball.draw_ball()
            ball.move()
            ball.detect_collision(self.player, self.opponent)
            
            CLock.tick(FPS) 
            pygame.display.update()     


pong = Pong()
pong.loop()
pygame.quit()
