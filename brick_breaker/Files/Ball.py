from globals import *

class Ball:
    def __init__(self):
        self.radius = 10
        self.direction_x = random.choice((1, -1))
        self.direction_y = -1
        self.bounce_dir = 5

        self.speed_x = random.randint(5, 10)
        self.speed_y = random.randint(5, 10)

    def create_ball(self):
        x = player.x + self.radius * 4.5
        y = player.y - self.radius * 1.5

        self.ball = pygame.Rect(x, y, self.radius, self.radius)

    def draw_ball(self):
        pygame.draw.ellipse(WIN, LIGHT_BROWN, self.ball)     

    def follow_player(self):
        self.ball.x = player.x + self.radius * 4.5
        if self.ball.y > player.y:
            self.ball.y = player.y - self.radius * 4.5

        self.bounce_on_board()

    def bounce_on_board(self):
        max_height = HEIGHT - HEIGHT // 8
        speed = 2

        if self.ball.y < max_height:
            self.bounce_dir = speed
        if self.ball.colliderect(player):
            self.bounce_dir = -1 * speed
            audio.Player()
        
        self.ball.y += self.bounce_dir

    def detect_collision(self):
        global wall
        for row in walls:
            for x in row:
                if self.ball.colliderect(x[0]):
                    x[1] -= 1
                    audio.Destroy_block()
                    self.direction_y *= -1
                if x[1] <= 0:
                    row.remove(x)

        if self.ball.colliderect(player):
            center = player.centerx
            left = center - (board.width / 2)
            left_centre = (center + left) // 2
            right = center + (board.width / 2)
            right_center = (center + right) // 2

            # Algortithm that determines how much fast the ball will move
            # Left
            if self.ball.centerx < center:
                
                if self.ball.centerx < left_centre:
                    direction = 1 - abs((self.ball.centerx - center) / center)
                    direction = -1 * direction

                elif self.ball.centerx > left_centre:
                    direction = (self.ball.centerx - center) / center

                else:
                    direction = -0.5

                self.direction_x = direction
            # Right
            elif self.ball.centerx > center:

                if self.ball.centerx < right_center:
                    direction = (self.ball.centerx - center) / center

                elif self.ball.centerx > right_center:
                    direction = 1 - abs((self.ball.centerx - center) / center)
                
                else:
                    direction = 0.5

                self.direction_x = direction
            
            else:
                self.direction_x = 0
            self.direction_y *= -1

            audio.Player()

    def move(self):
        global bouncing, lives
        if self.ball.x >= WIDTH - self.radius // 2:
            self.direction_x = -1 * self.direction_x
            audio.Hit_wall()

        if self.ball.x <= 0:
            self.direction_x = abs(self.direction_x)
            audio.Hit_wall()

        if self.ball.y >= HEIGHT:
            bouncing = False
            lives -= 1
            audio.Exit_screen()

            self.direction_y = -1
            return False , lives

        if self.ball.y <= 60:
            self.direction_y = 1 
        
        self.detect_collision()

        self.ball.x += self.speed_x * self.direction_x
        self.ball.y += self.speed_y * self.direction_y
        
        return True, lives