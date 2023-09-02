from globals import *

class Board:
    def __init__(self) -> None:
        self.width = 100
        self.height = 10
    
    def create_board(self):
        x = WIDTH // 2 - self.width // 2
        y = HEIGHT - self.height * 4
        self.board = pygame.Rect(x, y, self.width, self.height)
        return self.board

    def draw_board(self):
        pygame.draw.rect(WIN, LIGHT_BROWN, self.board, border_radius=5)

    def move(self, speed):
        self.board.x += speed
        if self.board.centerx >= WIDTH:
            self.board.centerx = 0
        if self.board.centerx < 0:
            self.board.centerx = WIDTH
