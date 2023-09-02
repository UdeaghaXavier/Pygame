from variables import *

class Wall:
    def __init__(self) -> None:
        self.width = WIDTH // cols
        self.height = 50

    def create_wall(self):
        self.blocks = []

        for row in range(rows):

            block_row = []
            for col in range(cols):
                x = col * self.width
                y = (row * self.height) + 60
                rect = pygame.Rect(x, y, self.width, self.height)

                if row < rows // 3:
                    strength = 3
                elif row < (rows // 3) * 2:
                    strength = 2
                elif row < (rows // 3) * 3:
                    strength = 1

                indv_block = [rect, strength]
                block_row.append(indv_block)
            self.blocks.append(block_row)
        return self.blocks

    def draw_wall(self):
        space = 2
        for row in self.blocks:
            for block in row:
                if block[1] == 3:
                    block_col = BLUE
                elif block[1] == 2:
                    block_col = GREEN
                elif block[1] == 1:
                    block_col = RED
                
                if block[1] > 0:
                    pygame.draw.rect(WIN, block_col, block[0])
                    pygame.draw.rect(WIN, PEACH, block[0], 1)

    def is_empty(self):
        left = rows * cols

        for row in self.blocks:
            for x in row:
                left -= 1

        if left == (rows * cols):
            return True
        return False