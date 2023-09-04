import tkinter as tk

screen = tk.Tk()

class UI:
    def display_title(self):
        tk.Label(
            screen,
            text="Pong",
            width=13,
            height=3,
            borderwidth=5,
            font="Courier 50 bold",
        ).pack()

    def create_Interface(self):
        self.main = tk.Frame(screen, borderwidth=5)

        texts = (
            "Boards (Player & Opponent) colour: ",
            "Ball colour:",
            "Background colour",
        )
        entries = []

        for text in texts:
            frame, entry, label = self.create_input_parts(text)
            entries.append(entry)

            label.grid(row=1, column=1)
            entry.grid(row=1, column=2)
            frame.pack()

        self.main.pack()

        return entries

    def create_start_button(self, func):
        button = tk.Button(
            screen,
            text="Start",
            font="Courier 13 bold",
            width=15,
            bg="grey",
            fg="white",
            command=func,
        )
        button.pack(pady=10)

    def create_input_parts(self, text):
        frame = tk.Frame(
            self.main,
            borderwidth=5,
            width=60,
        )

        entry = tk.Entry(frame, font="Courier 20 bold", width=11)

        label = tk.Label(
            frame,
            text=text,
            font="Courier 11 bold",
        )

        return frame, entry, label

    def display_hint(self):
        tk.Label(
            screen,
            text="In the spaces provides input the colour in a RGB format but with spaces seperating the colour values e.g 0 0 0, that is black. NOTE: If left blank or the colour format used is wrong it'll be set to the default color",
            width=52,
            height=7,
            wraplength=525,
            font="Courier 12 bold",
            fg="dark red",
            bg="light grey",
            relief="sunken",
            borderwidth=5,
        ).pack(pady=20)


class Logic:
    def __init__(self):
        self.UI = UI()
        self.colour = Colour()

    def start_btn(self):
        for index, entry in enumerate(self.entries):
            entry_str = entry.get()
            if entry_str:
                entry_list = entry_str.split()
                if len(entry_list) == 3:
                    for i in entry_list:
                        if not i.isdigit():
                            break

                        if int(i) > 255:
                            break
                    else:
                        match index:
                            case 0:
                                self.colour.board = tuple(entry_list)
                            case 1:
                                self.colour.ball = tuple(entry_list)
                            case 2:
                                self.colour.bgcolor = tuple(entry_list)

        screen.quit()

    def display_manager(self):
        self.UI.display_title()
        self.UI.display_hint()
        self.entries = self.UI.create_Interface()
        self.UI.create_start_button(self.start_btn)

    def main(self):
        self.display_manager()
        screen.mainloop()


class Colour:
    def __init__(self):
        self.board = None
        self.ball = None
        self.bgcolor = None

    def rgb_former(self, colour:tuple):
        colour_list = []
        for i in colour:
            colour_list.append(int(i))
        return tuple(colour_list)
