class HighScoreManager:
    def __init__(self):
        self.directory = 'data/highscore.txt'

    def retrieve_data(self):
        with open(self.directory, "r") as file:
            data = file.read()
        if data:
            data = data.split('\n')
            data = [x.split() for x in data]
            while [] in data:
                data.remove([])
        return data

    def save_data(self, *data):
        prev_data = self.retrieve_data()
        if prev_data:
            prev_data.append(list(data))
            prev_data.sort()

        with open(self.directory, "w") as file:
            if prev_data:
                for i in prev_data:
                    file.writelines(' '.join(i) + '\n')
            else:
                file.write(' '.join(data))

    def clear_file(self):
        self.save_data()
