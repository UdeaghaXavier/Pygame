import tkinter as tk
from Scripts.UI.HighScoreManager import HighScoreManager

HSM = HighScoreManager()


class Username_Input:
    def __init__(self):
        self.entry = None
        self.screen = tk.Tk()
        self.player_score = None
        self.Opponent_Score = None
        self.Multiplier = None

    def prompt(self):
        tk.Label(
            self.screen,
            font='Courier 20',
            text="What is your name?",
            width=20,
            height=3,
        ).pack()

        self.entry = tk.Entry(
            self.screen,
            font='Courier 20'
        )
        self.entry.pack()

        tk.Button(
            self.screen,
            text='Proceed',
            command=self.handler,
            bg='light grey',
            font='Courier 15'
        ).pack()

        self.screen.mainloop()

    def handler(self):
        self.proceed()

    def proceed(self):

        HSM.save_data(self.entry.get(), self.player_score, self.Opponent_Score, self.Multiplier)
        self.screen.quit()
        UI_END_Logic().main()


class UI:
    def __init__(self):
        self.screen = tk.Tk()
        self.highscore = HSM.retrieve_data()
        self.LeaderBoard = tk.Frame(
            self.screen,
            relief='sunken',
            borderwidth=4,
            height=1
        )

    def display_LeaderBoard(self):
        self.display_title()
        titles = ('Name', 'Computer\'s points', 'Player\'s points', 'Heighest Multiplier')
        for title in titles:
            self.display_panel(title, titles.index(title), 1)
        self.LeaderBoard.pack()
        self.display_items()

    def display_panel(self, text, col, row):
        tk.Label(
            self.LeaderBoard,
            text=text,
            font='Courier 13 bold'
        ).grid(row=row, column=(col + 1), padx=10)

    def display_title(self):
        tk.Label(
            self.screen,
            text="Leader Board",
            font='Courier 20 bold',
            width=20,
        ).pack()

    def display_items(self):
        for index, line in enumerate(self.highscore):
            for i, text in enumerate(line):
                self.display_panel(text, i, index + 2)


class UI_END_Logic:
    def __init__(self):
        self.UI = UI()

    def main(self):
        self.UI.display_LeaderBoard()
        self.UI.screen.mainloop()

