from variables import *

class Audio:
    def __init__(self):
        self.hit_wall = pygame.mixer.Sound('Assets/Audio/pickupCoin.wav')
        self.destroy_block = pygame.mixer.Sound('Assets/Audio/powerUp.wav')
        self.hit_player = pygame.mixer.Sound('Assets/Audio/ball.ogv')
        self.exit_screen = pygame.mixer.Sound('Assets/Audio/wrong-47985.mp3')
        self.bg_music = pygame.mixer.Sound('Assets/Audio/Stage 1.mp3')
        pygame.mixer.Channel(0).play(self.bg_music)

    def Destroy_block(self):
        pygame.mixer.Channel(1).play(self.destroy_block)

    def Hit_wall(self):
        pygame.mixer.Channel(1).play(self.hit_wall)

    def Player(self):
        pygame.mixer.Channel(1).play(self.hit_player)
    
    def Exit_screen(self):
        pygame.mixer.Channel(1).play(self.exit_screen)
    
    def bg(self):
        pygame.mixer.Channel(1).play(self.bg_music)