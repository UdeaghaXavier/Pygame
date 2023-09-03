# My modules
from variables import *  # Contains the needed global variables
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
PLAY = pygame.K_SPACE

def adjust_speed(vel):
    player.speed = vel
    opponent.speed = vel
    ball.speed = vel

class Pong:
    def __init__(self):
        self.player = player.player
        self.opponent = opponent.opponent
        self.ball = ball.ball
        self.speed = default_speed
        
        self.direction = 0
        self.running = True
        
        self.starting_time = time.time()
        self.paused = False
        self.secs = [0]
    
    def handle_input_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key in UP:
                    self.direction -= 1
                if event.key in DOWN:
                    self.direction += 1
                # Paused the game when the space bar is pressed
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused # This will return False if it's True and vise-versa in short pausing and unpausing it each time

            if event.type == pygame.KEYUP:
                if event.key in UP:
                    self.direction += 1
                if event.key in DOWN:
                    self.direction -= 1       

    def play(self):
        screen.fill(bg_color)
        
        self.increase_speed()
        adjust_speed(self.speed)

        looks.draw_center_line()

        player.draw_player()
        player.move(self.direction)

        opponent.draw_opponent()
        opponent.follow(self.ball)

        ball.draw_ball()
        ball.move()
        self.reset_ball()
        
        ball.detect_collision(self.player, self.opponent)
    
    def reset_ball(self):
        if self.ball.x < 0 or self.ball.x > width:
            ball.ball.x = ball.x
            ball.ball.y = ball.y
            self.starting_time = time.time()
            self.speed = default_speed
            self.secs = [0]

    def loop(self):
        while self.running:
            self.handle_input_events()
            if not self.paused:
                self.play()
            else:
                looks.pause() # Puts the pause image in the screen

            CLock.tick(FPS)
            pygame.display.update()

    def increase_speed(self):
        # Im increasing the speed based on how long you play
        # But the speed will reset (back to 7) each time the ball exits the screen
        # Relationship: for every 5s the speed increases by 1
        current = time.time()

        time_passed = current - self.starting_time
        time_passed = round(time_passed)

        if time_passed % 5 == 0 and time_passed not in self.secs: # or it its equal to 0 (a multiple of 5)
            self.speed += 1
            self.secs.append(time_passed)

pong = Pong()
pong.loop()
pygame.quit()
