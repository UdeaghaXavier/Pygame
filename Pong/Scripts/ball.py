from Scripts.variables import *


class Ball:
    def __init__(self):
        self.radius = 32
        self.x = (width / 2) - self.radius * 0.73
        self.y = (height // 2) - self.radius / 2
        self.speed = default_speed

        self.ball = pygame.Rect(self.x, self.y, self.radius, self.radius)

        # Make it go toward a random direction each time the game is initialized
        self.direction_x = random.choice((-1, 1))
        self.direction_y = random.choice((-1, 1))

        self.bounces = 0

    def draw_ball(self):
        pygame.draw.rect(screen, ball_color, self.ball, border_radius=self.radius)

    def move(self, direction_y=None):
        # Keep the ball within the screen
        if self.ball.y < 0:
            self.direction_y *= -1
            self.bounces += 1
            AudioManager.bounce_off_wall.play()
        if self.ball.y > (height - self.radius):
            self.direction_y *= -1
            self.bounces += 1
            AudioManager.bounce_off_wall.play()
        if direction_y:
            self.direction_y = direction_y

        self.ball.x += self.speed * self.direction_x
        self.ball.y += self.speed * self.direction_y

    def detect_collision(
        self, *bodies
    ):  # The * beside the bodies allows me to receive as a parameter an unlimited number of rectangles, player or
        # opponent, in our case
        for body in bodies:
            if self.ball.colliderect(body):
                self.direction_x *= -1
                self.bounces += 1
                AudioManager.hit_board.play()
                return self.smart_bouncing(body)

    def smart_bouncing(self, body):
        if self.ball.centery > body.centery:
            return 1
        else:
            return -1
