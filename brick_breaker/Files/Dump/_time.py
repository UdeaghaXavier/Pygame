from variables import *
import time

class _time:
    def __init__(self):
        self.start = time.time()
        self.size = 50
        self.font = pygame.font.SysFont("Assets/Fonts/ARCADE.TTF", self.size)
        self.secs = 0

    def time(self):
        current = time.time()
        self.secs = round(current - self.start)
        secs = self.secs

        mins, secs = self.secs_to_min(secs)

        passed = f"{mins}:{secs}"

        text = self.font.render(passed, True, GREY)
        WIN.blit(text, (WIDTH - WIDTH // 5, 10))

    def secs_to_min(self, secs):
        mins = int(secs / 60)
        sec = round(((secs / 60) - mins) * 60)

        if len(str(sec)) > 1:
            sec = str(sec)
        else:
            sec = "0" + str(sec)
        
        if len(str(mins)) > 1:
            mins = str(mins)
        else:
            mins = "0" + str(mins)
        
        return mins, sec
    
    def min_to_secs(self, min, sec):
        mins = int(mins)
        sec = int(sec)

        return mins + round(sec / 60)