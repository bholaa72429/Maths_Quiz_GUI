from tkinter import *
from functools import partial # to prevent unwanted windows

import random

class Start:
    def __init__(self, parent):

        # formatting variable
        background_color = "light yellow"

        # GUI - number of rounds
        self.start_frame = Frame(bg=background_color,pady=10)
        self.start_frame.grid()

        # Math Quiz heading (row 0)
        self.maths_box_label = Label(self.start_frame,
                                       text="Maths Quiz",
                                       font="Arial 19 bold",
                                        bg=background_color,
                                       padx=10, pady=10)
        self.maths_box_label.grid(row=0)

        # Initial instructions (row 1)
        self.quiz_instructions = Label(self.start_frame, font="Arial 10 italic",
                                          text="Welcome to basic maths quiz! " \
                                          "Please enter a the number of question you wish to play." \
                                          "Note: The number of rounds refers to the number of questions "
                                          "you wish to play.",
                                          wrap=275, justify=LEFT,
                                          bg=background_color, padx=10, pady=10)
        self.quiz_instructions.grid(row=1)


        # Entry box... (row 2)
        self.round_entry = Entry(self.start_frame, font="Arial 15 bold")
        self.round_entry.grid(row=2)

        self.round_error_label = Label(self.start_frame, font="Arial 10 bold",
                                       fg="red", text="",bg=background_color,pady=10,)
        self.round_error_label.grid(row=3)

        # Play Button
        self.play_button = Button(text="Continue",
                                       command=lambda: self.to_play(),
                                       font="arial 10",width=30, bg="#00FA9A")
        self.play_button.grid(row=4)

    def to_play(self):
        wanted_rounds = self.round_entry.get()

        # set error bg colours (and assume that there are no
        # errors at the start
        error_back = "#ffafaf"
        has_errors = "no"

        # change bg to white (for testing purposes)
        self.round_entry.config(bg="white")
        self.round_error_label.config(text="")

        try:
            wanted_rounds = int(wanted_rounds)

            if wanted_rounds < 1:
                has_errors = "yes"
                error_feedback = "Sorry, the least you" \
                                 "can play with is 1 question"
            elif wanted_rounds > 10:
                has_errors = "yes"
                error_feedback = "Too high! The most rounds " \
                                 "you can play is 10"

        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a number of rounds wished to ply (no text / decimals)"

        if has_errors == "yes":
            self.round_entry.config(bg=error_back)
            self.round_error_label.config(text=error_feedback)

        else:
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

        # Entry box... (row 2)
        self.answer_entry = Entry(self.game_frame, font="Arial 15 bold")
        self.answer_entry.grid(row=2)

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
