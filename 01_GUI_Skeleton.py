from tkinter import *
from functools import partial # to prevent unwanted windows

import random


class Start:
    def __init__(self, parent):

        # GUI to get number of rounds
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Math Quiz heading (row 0)
        self.maths_box_label = Label(self.start_frame,
                                       text="Maths Quiz",
                                       font="Arial 19 bold",
                                       # bg=background_color,
                                       padx=10, pady=10)
        self.maths_box_label.grid(row=1)

        # Entry box... (row 1)
        self.round_entry = Entry(self.start_frame, font="Arial 15 bold")
        self.round_entry.grid(row=2)

        # Play Button
        self.play_button = Button(text="Let's Play",
                                       command=lambda: self.to_play())
        self.play_button.grid(row=2, pady=10)

    def to_play(self):
        wanted_rounds = self.round_entry.get()
        Game(self, wanted_rounds)

class Game:
    def __init__(self, partner, wanted_rounds):
        print(wanted_rounds)


        partner.play_button.config(state=DISABLED)

        # initialise variable
        self.round = IntVar()

        # set rounds to the number entered by user at start of the game
        self.round.set(wanted_rounds)

        # GUI setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Game Time",
                                   font="Arial 24 bold", padx=10, pady=10)
        self.heading_label.grid(row=0)

        # Round Label
        self.round_frame = Frame(self.game_frame)
        self.round_frame.grid(row=1)

        self.rounds_label = Label(self.game_frame, text=" Number of Rounds...")
        self.rounds_label.grid(row=3)






# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Start(root)
    root.mainloop()
