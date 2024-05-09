from Global.variables import pygame, screen_res, col


class Pad:
    def __init__(self, win: pygame.Surface) -> None:
        self.WIN = win
        self.width = 75
        self.corner_radius = 5
        self.can_move = False

        self.speed = 10
        self.direction = 0
        self.pos = [screen_res[0] / 2, screen_res[1] * 90 / 100]

        self.board = pygame.Rect(self.pos[0], self.pos[1], self.width, 10)

    def draw(self) -> None:
        pygame.draw.rect(
            self.WIN,
            col["black"],
            self.board,
            border_bottom_left_radius=self.corner_radius,
            border_bottom_right_radius=self.corner_radius,
            border_top_left_radius=self.corner_radius,
            border_top_right_radius=self.corner_radius,
        )

    def input(self, event: pygame.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if self.can_move:
                if event.key != pygame.K_RETURN:
                    self.direction = int(event.key == pygame.K_RIGHT) - int(
                        event.key == pygame.K_LEFT
                    )
        if event.type == pygame.KEYUP:
            if self.can_move:
                self.direction = 0

    def update(self) -> None:
        self.pos[0] += self.speed * self.direction
        if self.pos[0] < (-1 * self.width / 4):
            self.pos[0] = screen_res[0]
        elif self.pos[0] > (screen_res[1] + self.width / 4):
            self.pos[0] = 0
        self.board.center = self.pos
