
from variables import *

class Ball:
    def __init__(self):
        self.radius = 32
        self.x = (width / 2) - self.radius * .73
        self.y = (height // 2) - self.radius / 2
        self.speed = default_speed
        
        self.ball = pygame.Rect(self.x, self.y, self.radius, self.radius)
        
        # Make it go toward a random direction each time the game is initialized
        self.direction_x = random.choice((-1, 1))
        self.direction_y = random.choice((-1, 1))    
    
    def draw_ball(self):
      pygame.draw.rect(screen, WHITE, self.ball, border_radius=self.radius)
      
    def move(self):
        # Keep the ball within the screen
        if self.ball.y < 0:
            self.direction_y *= -1
        if self.ball.y > (height - self.radius):
            self.direction_y *= -1
        
        self.ball.x += self.speed * self.direction_x
        self.ball.y += self.speed * self.direction_y
    
    def detect_collision(self, *bodies): # The * beside the bodies allows me to recieve as a parameter an unlimited number of rectangles(player or opponent in our case)
        for body in bodies:
            if self.ball.colliderect(body):
                self.direction_x *= -1
                break
