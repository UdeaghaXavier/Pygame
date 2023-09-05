from Scripts.variables import *


class Looks:
    def __init__(self):
        # Line
        self.line_width = 10
        self.line_height = height
        self.line_x = width // 2 + 5
        self.line_y = 0

        # Pause
        self.pause_img = pygame.image.load('Assets/Images/pause.png')
        self.pause_img_x = width // 2 - (40 / 2)  # The pause image has a dimension of 48x48
        self.pause_img_y = height // 2 - (48 / 2)

        # Font for texts
        self.font_size = 48
        self.font = pygame.font.SysFont('Courier new', self.font_size)
        self.font_colour = board_color

        # Score and multiplier
        self.player_score = 0
        self.player_score_pos = (width // 4 - self.font_size // 2, 0)
        self.opponent_score = 0
        self.opponent_score_pos = (width - (width // 4 - self.font_size // 2), 0)
        self.multiplier = 1
        self.multiplier_pos = (width // 2 - self.font_size // 2, 0)
        self.highest_multiplier = None

        self.is_paused = False

    def draw_center_line(self):
        start_pos = (self.line_x, self.line_y)
        end_pos = (self.line_x, self.line_height)
        pygame.draw.aaline(screen, board_color, start_pos, end_pos, 0)
        self.is_paused = False

    def pause(self):
        screen.blit(self.pause_img, (self.pause_img_x, self.pause_img_y))
        if self.is_paused == False:
            AudioManager.pause.play()
            self.is_paused = True
        print(self.is_paused)

    def display_HUD(self):
        player_score = self.font.render(str(self.player_score), True, self.font_colour)
        opponent_score = self.font.render(str(self.opponent_score), True, self.font_colour)
        multiplier = self.font.render("X" + str(self.multiplier), True, self.font_colour)

        screen.blit(player_score, self.player_score_pos)
        screen.blit(opponent_score, self.opponent_score_pos)
        screen.blit(multiplier, self.multiplier_pos)
