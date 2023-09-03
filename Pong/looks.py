from pygame import draw
from variables import *

class Looks:
    def __init__(self):
        # Line
        self.line_width = 10
        self.line_height = height
        self.line_x = width // 2
        self.line_y = 0

        # Pause
        self.pause_img = pygame.image.load('Assets/Images/pause.png')
        self.pause_img_x = width // 2 - (48 / 2) # The pause image has a dimension of 48x48
        self.pause_img_y = height // 2 - (48 / 2)
        
    def draw_center_line(self):
        start_pos = (self.line_x, self.line_y)
        end_pos = (self.line_x, self.line_height)
        draw.aaline(screen, WHITE, start_pos, end_pos, 0)

    def pause(self):
        screen.blit(self.pause_img, (self.pause_img_x, self.pause_img_y))