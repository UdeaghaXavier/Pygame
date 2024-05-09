from Global.variables import pygame, screen_res, bricks_region, randint


class BrickManager:
    def __init__(self, win: pygame.Surface) -> None:
        self.WIN = win

        self.drop = False
        self.bricks = []
        self.color_grades = [
            (150, 0, 0),
            (150, 50, 0),
            (150, 150, 0),
            (50, 150, 0),
            (0, 150, 50),
            (0, 150, 150),
        ]

        self.n_row = 6
        self.n_col = 7
        self.spacing = 8
        self.corner_radius = 5
        self.brick_height = bricks_region[1] / (self.n_row * 150 / 100)

        self.brick_width = (
            (screen_res[0] - ((self.spacing) * (self.n_col + 1)))
        ) / self.n_col

        self.init()

    def init(self) -> None:
        x = y = self.spacing
        for _ in range(self.n_row):
            self.bricks.append(self.create_brick_row(y))
            y += self.spacing + self.brick_height

    def create_brick_row(self, y: int | float) -> list[dict[str, int]]:
        row = []
        x = self.spacing

        for _ in range(self.n_col):
            rect = pygame.Rect(x, y, self.brick_width, self.brick_height)

            x += self.spacing + self.brick_width

            data = {"rect": rect, "hp": randint(0, len(self.color_grades) - 1)}
            row.append(data)

        return row

    def draw_bricks(self) -> None:
        for row in self.bricks:
            for brick in row:
                pygame.draw.rect(
                    self.WIN,
                    self.color_grades[brick["hp"]],
                    brick["rect"],
                    border_bottom_left_radius=self.corner_radius,
                    border_bottom_right_radius=self.corner_radius,
                    border_top_left_radius=self.corner_radius,
                    border_top_right_radius=self.corner_radius,
                )

    def draw(self) -> None:
        self.draw_bricks()

    def update(self) -> None:
        pass

    def input(self, event: pygame.Event) -> None:
        pass
