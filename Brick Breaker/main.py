from Global.variables import *
from Script.brickManager import BrickManager
from Script.board import Pad
from Script.ball import Ball


class Main:
    def __init__(self) -> None:
        self.WIN = pygame.display.set_mode(screen_res)
        self.brick_manager = BrickManager(self.WIN)
        self.pad = Pad(self.WIN)
        self.ball = Ball(self.pad.board, self.WIN)

        self.running = True

    def input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.brick_manager.input(event)
            self.pad.input(event)
            self.ball.input(event)

    def update(self) -> None:
        self.input()
        self.brick_manager.update()
        self.pad.update()

        self.ball.player = self.pad.board
        self.pad.can_move = not self.ball.aiming
        self.ball.update()

        clock.tick(FPS)
        pygame.display.update()

    def draw(self) -> None:
        self.WIN.fill(col["dark-greyish-brown"])

        self.brick_manager.draw()
        self.pad.draw()
        self.ball.draw()

    def run(self) -> None:
        while self.running:
            self.draw()
            self.update()


if __name__ == "__main__":
    Main().run()
    pygame.quit()
