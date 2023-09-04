from Scripts.variables import *


class Opponent:
    def __init__(self):
        self.height: int = 200
        self.width: int = 20
        self.x = self.width * 2
        self.y = height // 2 - self.height // 2
        self.speed = default_speed

        self.direction = 0
        self.opponent = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_opponent(self):
        pygame.draw.rect(screen, board_color, self.opponent)

    def stay_within_screen(self):
        if self.opponent.y < 0:
            self.opponent.y = 0
        elif self.opponent.y > (height - self.height):
            self.opponent.y = height - self.height

    def follow(self, ball):
        # Without this the opponent will be too fast and will never lose
        drag = (self.speed - 7) / 2

        if ball.x < width / 2:
            if self.opponent.top > ball.top:
                self.direction = -1
            else:
                self.direction = 1
        else:
            self.direction = 0

        self.opponent.y += (self.speed - drag) * self.direction
        print((self.speed - drag) * self.direction)
        self.stay_within_screen()
