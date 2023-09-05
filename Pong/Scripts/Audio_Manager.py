from pygame import mixer, init

mixer.init()

class AudioManager:
    def __init__(self):
        self.bounce_off_wall = mixer.Sound('Assets/Audio/bounce_off_wall.wav')
        self.hit_board = mixer.Sound('Assets/Audio/Hit_board.wav')
        self.lose = mixer.Sound('Assets/Audio/lose.wav')
        self.score = mixer.Sound('Assets/Audio/score.wav')
        self.speed_increased = mixer.Sound('Assets/Audio/speed increased.wav')
        self.pause = mixer.Sound('Assets/Audio/pause.wav')



