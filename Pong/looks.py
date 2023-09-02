from pygame import draw
from variables import *

class Looks:
    def __init__(self):
        # Screen
        self.bg_color = BLACK
        
        # Line
        self.line_width = 10
        self.line_height = height
        self.line_x = width // 2 - self.line_width
        self.line_y = 0
        
    def draw_center_line(self):
        start_pos = (self.line_x, self.line_y)
        end_pos = (self.line_x, self.line_height)
        draw.aaline(screen, WHITE, start_pos, end_pos, 0)