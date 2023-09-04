class HighScoreManager:
    def __init__(self, opponent_score, player_score):
        self.directory = 'data/highscore.txt'
        self.opponent_score = opponent_score
        self.player_score = player_score
        
    def get_previous_score(self):
        with open(self.directory, "r") as file:
            data = file.read()
        return data
    
    def save_score(self, data = ''):
        with  open(self.directory, "w") as file:
            file.write(data)
    
    def clear(self):
        self.save_score()

    def main(self):
        score = f'{self.opponent_score} {self.player_score}'
        data = self.get_previous_score()
        if not data:
            self.save_score(score)
        else:
            data = data.split()
            if self.opponent_score < self.player_score:
                if int(data[1]) < self.player_score:
                    self.save_score(score)
                    
HSM = HighScoreManager(10, 11)
HSM.main()
                