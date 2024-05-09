from Global.variables import pygame, col, screen_res, sin, cos, degrees
from Global.functions import add_tuple

import math


class Ball:
    def __init__(self, player: pygame.Rect, win: pygame.Surface) -> None:
        self.WIN = win
        self.aiming = True
        self.aiming_line_lenght = (1 / 4) * screen_res[0]
        self.direction = [1, 1]
        self.bounce_relapse = 2

        self.theta = 88
        self.angle_range = 86.7, 89.3
        self.ref_angle = 88
        self.angle_diff = self.ref_angle - self.angle_range[0]

        self.inc = 0.13

        self.radius = 10
        self.speed = 5
        self.player = player
        self._follow_player = True

        self.hover_height = -30
        self.pos = [self.player.centerx, self.player.centery + self.hover_height]
        self.ball = pygame.Rect(self.pos[0], self.pos[1], self.radius, self.radius)

    def follow_player(self) -> None:
        self.pos = [self.player.centerx, self.player.centery + self.hover_height]

    def collision_bounce(self):
        if self.ball.colliderect(self.player):
            self.direction[0] *= -1
            self.direction[1] = -1

        elif self.pos[0] > screen_res[0] or self.pos[0] < 0:
            self.direction[0] *= -1
        elif self.pos[1] > screen_res[1] or self.pos[1] < 0:
            self.direction[1] *= -1

    def get_accel(self) -> tuple:
        rot = (self.theta - self.ref_angle) / self.angle_diff

        if rot > 0:
            accel = (rot + 0.05) * -1, (1 - (rot + 0.2)) * -1
        else:
            accel = (rot + 0.05) * -1, ((rot + 0.05) + 1)

        return accel

    def move(self) -> tuple:
        accel = self.get_accel()

        pos = self.pos
        speed = (accel[0] * self.speed, accel[1] * self.speed)

        pos[0] += speed[0] * self.direction[0]
        pos[1] += speed[1] * self.direction[1]

        return pos

    def draw_aim_system(self) -> None:
        x, y = degrees(sin(self.theta)), degrees(cos(self.theta))

        x /= 90
        y /= 90

        pygame.draw.line(
            self.WIN,
            col["black"],
            self.pos,
            (
                self.pos[0] - self.aiming_line_lenght * (x or 0),
                self.pos[1] - self.aiming_line_lenght * (y or 0),
            ),
        )

    def draw(self) -> None:
        pygame.draw.rect(
            self.WIN,
            col["black"],
            self.ball,
            border_bottom_left_radius=self.radius,
            border_bottom_right_radius=self.radius,
            border_top_left_radius=self.radius,
            border_top_right_radius=self.radius,
        )

        if self.aiming:
            self.draw_aim_system()

    def update(self) -> None:
        print(self.get_accel())
        if self._follow_player:
            self.follow_player()

        if not self.aiming:
            self.pos = self.move()
            self.collision_bounce()

        self.ball.center = self.pos

    def input(self, event: pygame.Event) -> None:
        if self.aiming:
            if event.type == pygame.KEYDOWN:
                if event.key != pygame.K_SPACE:
                    self.theta += (
                        ((event.key == pygame.K_RIGHT) - (event.key == pygame.K_LEFT))
                        * self.inc
                        * -1
                    )
                    if self.theta < self.angle_range[0]:
                        self.theta = self.angle_range[0]
                    if self.theta > self.angle_range[1]:
                        self.theta = self.angle_range[1]
                else:
                    self.aiming = False
                    self._follow_player = False
