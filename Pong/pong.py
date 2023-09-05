# My modules
from Scripts.variables import *  # Contains the needed global variables
from Scripts.looks import (
    Looks,
)  # Everything that isn't related to the ball, player and opponent is in here
from Scripts.player import Player
from Scripts.opponent import Opponent
from Scripts.ball import Ball
from Scripts.UI.UI_End import Username_Input

looks = Looks()
player = Player()
opponent = Opponent()
ball = Ball()

UP = (pygame.K_UP, pygame.K_w)
DOWN = (pygame.K_DOWN, pygame.K_s)
PLAY = (pygame.K_SPACE,)


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
        self.sec_passed = [0]

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
                if event.key in PLAY:
                    self.paused = (
                        not self.paused
                    )  # This will return False if it's True and vise-versa in short pausing and un-pausing it each time

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
        ball.move(ball.detect_collision(self.player, self.opponent))

        looks.display_HUD()
        self.reset_ball()

    def reset_ball(self):
        if (
            self.ball.x < 0
            or self.ball.x > width
            or self.ball.center == self.opponent.center
        ):
            # Score related
            if self.ball.x > width:
                looks.player_score += looks.multiplier
                AudioManager.lose.play()
            elif self.ball.x < 0:
                looks.opponent_score += looks.multiplier
                AudioManager.score.play()
            looks.multiplier = 1

            # Ball related
            ball.ball.x = ball.x
            ball.ball.y = ball.y
            ball.direction_x = random.choice((1, -1))
            ball.direction_y = random.choice((1, -1))
            ball.bounces = 0
            self.starting_time = time.time()
            self.speed = default_speed
            self.sec_passed = [0]

    def loop(self):
        while self.running:
            self.handle_input_events()
            if not self.paused:
                self.play()
            else:
                looks.pause()  # Puts the pause image in the screen

            CLock.tick(FPS)
            pygame.display.update()

    def increase_speed(self):
        # I'm increasing the speed based on how long you play
        # But the speed will reset (back to 7) each time the ball exits the screen
        # Relationship: for every 5s the speed increases by 1
        current = time.time()

        time_passed = current - self.starting_time
        time_passed = round(time_passed)

        if time_passed >= 5:  # or it its equal to 0 (a multiple of 5)
            self.speed = round(time_passed / 5) + default_speed
            if self.speed not in self.sec_passed:
                AudioManager.speed_increased.play()
                self.sec_passed.append(self.speed)

        # The multiplier works like this, for every 10 bounces it increases by 1
        if ball.bounces >= 10:
            looks.multiplier = round(ball.bounces / 10)
            if looks.highest_multiplier:
                if looks.multiplier > int(looks.highest_multiplier):
                    looks.highest_multiplier = looks.multiplier
            else:
                looks.highest_multiplier = looks.multiplier


pong = Pong()
pong.loop()
pygame.quit()

UI_END = Username_Input()
UI_END.player_score = str(looks.player_score)
UI_END.Opponent_Score = str(looks.opponent_score)
UI_END.Multiplier = str(looks.highest_multiplier)
UI_END.prompt()
