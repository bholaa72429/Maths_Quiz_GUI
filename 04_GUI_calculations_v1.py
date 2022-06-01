from tkinter import *
from functools import partial # to prevent unwanted windows

import random

class Start:
    def __init__(self, parent):

        # GUI to get rounds
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.push_me_button = Button(text="Push Me", command=self.to_play)
        self.push_me_button.grid(row=0, pady=10)


    def to_play(self):

        # for testing purposes
        wanted_rounds = 5

        Game(self, wanted_rounds)


class Game:
    def __init__(self, partner, wanted_rounds):
        print(wanted_rounds)

        #partner.play_button.config(state=DISABLED)

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

        # Entry box...
        self.answer_entry = Entry(self.game_frame, font="Arial 15 bold",width=10)
        self.answer_entry.grid(row=3)

        # Submit Button
        self.submit_button = Button(self.game_frame,text="Submit",font="arial 10", width=5, bg="#00FA9A")
        self.submit_button.grid(row=5)

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
