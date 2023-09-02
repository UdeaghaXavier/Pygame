from variables import *

class Menu:
    def __init__(self):
        self.bg = pygame.image.load("Assets/Images/menu.png")
        self.size = 70
        self.font = pygame.font.SysFont("ARCADE", self.size, italic=True)
        self.title_text = "BRICK BREAKER"
        self.pos = WIDTH // 3 + 4, HEIGHT - HEIGHT // 2.5 + 4, 200 - 8, 64 - 16
        self.btn = pygame.Rect(self.pos)
        self.btn_img = "play_btn_normal.png"
        
        self.menu_music = pygame.mixer.Sound('Assets/Audio/Main Menu.mp3')
        pygame.mixer.Channel(1).play(self.menu_music)

    def background(self):
        WIN.blit(self.bg, (0, 0))
        self.title()
        self.play_btn()

    def close(self):
        pygame.mixer.Channel(1).stop()

    def title(self):
        title = self.font.render(self.title_text, True, DARK_GREEN)
        WIN.blit(title, (70, HEIGHT // 3.2))

    def play_btn(self):
        pygame.draw.rect(WIN, BLACK, self.btn)

        btn_n = pygame.image.load(f"Assets/Images/{self.btn_img}")
        WIN.blit(btn_n, (WIDTH // 3, HEIGHT - HEIGHT // 2.5, 200, 64))