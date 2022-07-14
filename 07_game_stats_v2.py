from tkinter import *
from functools import partial # to prevent unwanted windows
import re
import random
from time import strftime

class Start:
    def __init__(self, parent):

        # bg colour
        background_color = "#C8D5EC"

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
                                          "you wish to play." ,
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
                                       font="arial 10",width=30, bg="#C8ECDD",padx=10)
        self.play_button.grid(row=4,pady=10,)

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
                                 "can play with is 1 rounds"
            elif wanted_rounds > 10:
                has_errors = "yes"
                error_feedback = "Too high! The most rounds " \
                                 "you can play is 10"

        except ValueError:
            has_errors = "yes"
            error_feedback = "Enter rounds wished to ply (no text / decimals)"

        if has_errors == "yes":
            self.round_entry.config(bg=error_back)
            self.round_error_label.config(text=error_feedback)

        else:
            Game(self, wanted_rounds)

            # hide starts up window
            root.withdraw()


class Game:
    def __init__(self, partner, wanted_rounds):


        # initialise variable
        self.total_round = wanted_rounds
        self.current_round = wanted_rounds
        self.num_one = IntVar()
        self.num_two = IntVar()
        self.sign = IntVar()
        self.ans_calc = IntVar()
        self.user_ans = IntVar()
        self.points = 0


        # GUI setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Game Time",
                                   font="Arial 24 bold", padx=10, pady=10)
        self.heading_label.grid(row=0)


        # play button goes here (row 3)
        self.play_button = Button(self.game_frame, text="Start",
                                  bg="#FFFF33", font="Arial 15 bold", width=10,
                                  pady=10, padx=10, command=self.try_again)
        self.play_button.grid(row=3)
        # Entry box...
        self.answer_entry = Entry(self.game_frame, font="Arial 15 bold",width=10)
        self.answer_entry.grid(row=5)

        # Submit Button
        self.submit_button = Button(self.game_frame, text="Submit", font="Arial 15 bold", bg="#00FA9A", width=10,
                                    command=self.check_ans)
        self.submit_button.grid(column=0,row=8, pady=10, padx=10)

        # Next Button
        self.next_button = Button(self.game_frame, text="Next", font="Arial 15 bold", bg="#00FA9A", width=10,
                                  command=self.try_again)
        self.next_button.grid(column=2,row=8, pady=10, padx=10)

        self.answer_entry_label = Label(self.game_frame, font="Arial 15 bold", fg="red", text="", pady=10)
        self.answer_entry_label.grid(row=6)

        # Round Label
        self.round_frame = Frame(self.game_frame)
        self.round_frame.grid(row=1)

        self.rounds_label = Label(self.game_frame, text=" Number of Rounds left...")
        self.rounds_label.grid(row=9)

        # help and game stats button (row 5)
        self.help_export_frame = Frame(self.game_frame)
        self.help_export_frame.grid(row=10, pady=10)

        self.help_button = Button(self.help_export_frame, text="Help / Rules",
                                  font="Arial 15 bold", bg="#808080", fg="white")
        self.help_button.grid(row=0, column=0, padx=10)

        self.stats_button = Button(self.help_export_frame, text= "Game Stats...",
                                   font="Arial 15 bold", bg="#003366", fg="white",
                                   command= lambda: self.to_stats(self.points, self.current_round, self.total_round))
        self.stats_button.grid(row=0, column=2, padx=10)
        # disabled both submit and next in starting
        self.next_button.config(state=DISABLED)
        self.submit_button.config(state=DISABLED)


    def try_again(self):
        # destroy the start button
        self.play_button.destroy()

        # generating random signs and numbers
        symbol = ['+', '-', '*', '/']
        self.num_one = random.randint(10, 20)
        self.num_two = random.randint(1, 10)
        self.sign = random.choice(symbol)

        # put the values in equation format
        value = str((self.num_one)) +''+ self.sign +''+ str((self.num_two ))
        # calculate the answer
        self.ans_calc = eval(value)
        # reset the entry box value / color
        self.answer_entry.config(bg="white")
        self.answer_entry.delete(0,8)
        # setting of the buttons
        self.next_button.config(state=DISABLED)
        self.submit_button.config(state=NORMAL)
        # question
        self.question_label = Label(self.game_frame, text=value,
                                    font="Arial 15 bold", )
        self.question_label.grid(row=4, pady=10, padx=10)
        # running the counter for the rounds
        round = self.current_round

        # checking rounds
        if self.current_round < 1:
            self.question_label.destroy()
            self.next_button.config(state=DISABLED)
            self.submit_button.config(state=DISABLED)
            self.answer_entry_label.config(text="GAME OVER")
            self.game_box.focus()
        else:
            self.current_round -= 1


        self.rounds_label.configure(text="Rounds: {}".format(round))


    def check_ans(self):

        # set error bg colours (and assume that there are no
        # errors at the start
        error_back = "#ffafaf"
        has_errors = "no"

        # change bg to white (for testing purposes)
        self.answer_entry.config(bg="white")
        self.answer_entry_label.config(text="")

        try:
            # get user answer
            user_ans = int(self.answer_entry.get())
            ans = int(self.ans_calc)


            # check user answer and give feedback accordingly
            if user_ans == ans:
                self.points += 1
                print('Correct!\nPoints: ', self.points)
                result_feedback = "RIGHT"
                self.answer_entry_label.config(text=result_feedback)
                self.answer_entry.config(bg="green")
                # settings of the button
                self.next_button.config(state=NORMAL)
                self.submit_button.config(state=DISABLED)

            else:
                #points -= 1
                #print('Wrong!\nSolution: ' + str(ans) + '\nPoints: ', points)
                result_feedback = "WRONG"
                self.answer_entry_label.config(text=result_feedback)
                self.answer_entry.config(bg="red")
                # settings of the button
                self.next_button.config(state=NORMAL)
                self.submit_button.config(state=DISABLED)

        except ValueError:
            has_errors = "yes"
            error_feedback = "Enter a valid number (no text)"

        if has_errors == "yes":
            self.answer_entry.config(bg=error_back)
            self.answer_entry_label.config(text=error_feedback)


    def to_stats(self, points, current_rounds, total_rounds):
        GameStats(self,points,current_rounds,total_rounds )

class GameStats:
    def __init__(self, partner,points,current_rounds,total_rounds):

        print(points,current_rounds,total_rounds)

        # disable help button
        partner.stats_button.config(state=DISABLED)

        heading = "Arial 12 bold"
        content = "Arial 12"

        # Sets up child window (ie: help box)
        self.stats_box = Toplevel()

        # if user press cross at the top, closes help and 'releases' help button
        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats,partner))

        # set up GUI
        self.stats_frame = Frame(self.stats_box)
        self.stats_frame.grid()

        # Heading (row 0)
        self.stats_heading_label = Label(self.stats_frame, text="Game Statistics", font="arial 19 bold")

        self.stats_heading_label.grid(row=0)

        # To export <instruction> (row 1)
        self.export_instructions = Label(self.stats_frame,
                                         text="Here are you Game Statistics."
                                               "Please use the Export button to"
                                               "access the result of each"
                                               "round that you played",
                                         wrap=250,
                                         font="arial 10 italic",
                                         justify=LEFT, fg="green",
                                         padx=10,pady=10)
        self.export_instructions.grid(row=1)

        # Start Rounds (row 2)
        self.details_frame = Frame(self.stats_frame)
        self.details_frame.grid(row=2)
        # total rounds played (row 2.5)
        self.game_played_label = Label(self.details_frame, text="Total Round", font=heading, anchor="e")

        self.game_played_label.grid(row=2, column=0, padx=0)

        self.game_played_value_label = Label(self.details_frame, font=content, text=total_rounds, anchor="w")

        self.game_played_value_label.grid(row=2, column=1, padx=0)

        # round played (row 2.4)
        self.game_played_label = Label(self.details_frame, text="Current Round Played", font=heading,anchor="e")

        self.game_played_label.grid(row=3, column= 0, padx = 0)
        rounds_played = total_rounds-current_rounds
        self.game_played_value_label = Label(self.details_frame, font=content, text=rounds_played, anchor="w")

        self.game_played_value_label.grid(row=3, column=1, padx=0)


        # Total Right / Wrong (row 2.3)
        self.total_right_wrong_label = Label(self.details_frame, text="Correct Ans", font=heading, anchor="e")

        self.total_right_wrong_label.grid(row=4, column=0, padx=0)

        self.total_right_wrong_value_label = Label(self.details_frame, font=content,
                                           text=points, anchor="w")
        self.total_right_wrong_value_label.grid(row=4, column=1, padx=0)


        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.details_frame, text="Dismiss",
                                  width=10, bg="#660000", fg="white", font="arial 14 bold",
                                  command=partial(self.close_stats, partner))

        self.dismiss_btn.grid(row=5)
        self.export_btn = Button(self.details_frame, text="Export",
                                  width=10, bg="#660000", fg="white", font="arial 14 bold",
                                  command=lambda: self.export(points, rounds_played, total_rounds))

        self.export_btn.grid(row=9)

    def close_stats(self, partner):
        # put help button back to normal...
        partner.stats_button.config(state=NORMAL)
        self.stats_box.destroy()

    def export(self, points, current_round, total_round):
        Export(self, points, current_round, total_round)

class Export:
    def __init__(self,partner, points, current_round, total_round):



        # disable help button
        partner.export_btn.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.export_box = Toplevel()

        # if user press cross at the top, closes help and 'releases' help button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # Set up GUI frame
        self.export_frame = Frame(self.export_box, width=300)
        self.export_frame.grid()

        # set yp export heading row 0
        self.how_heading = Label(self.export_frame, text="Export/ Instruction", font="arial 14 bold")
        self.how_heading.grid(row=0)

        # history text (label, row 1 )
        self.export_text = Label(self.export_frame,
                                 text="Enter a filename "
                                      "in the box below"
                                      "and press the SAVE "
                                      "button to save your "
                                      "calculation history"
                                      "to the text file",
                                 wrap=250, font="arial 10 italic",
                                 justify=LEFT, width=40)
        self.export_text.grid(row=1)

        # Warning text (label, row 2)
        self.export_text = Label(self.export_frame, text="If the filename you "
                                                         "entered below"
                                                         "already exists,"
                                                         "its content will be "
                                                         "replaced with your calculation history",
                                 justify=LEFT, bg='#ffafaf', fg='maroon',
                                 font="Arial 10 italic", wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        # Filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error Message Labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg='maroon')
        self.save_error_label.grid(row=4)

        # Save \ Cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save \ Cancel BUTTON (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  font="Arial 15 bold", bg="#003366", fg="white",
                                  command=lambda: self.save_history(partner, points, current_round, total_round))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    font="Arial 15 bold", bg="#660000", fg="white",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, points, current_round, total_round):

        # Regular expression to check filename is valid
        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        # timestamp
        time_string = strftime("%H:%M:%S %p \n Day: %A  \n Date: %x")
        date_display = "Time: {}".format(time_string)
        # print(date_display)

        filename = self.filename_entry.get()
        print(filename)

        # filename = input("Enter a filename: ")
        # print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"
            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            # Display error message
            self.save_error_label.config(text="invalid filename - {}".format(problem))
            # Change entry box background to pick
            self.filename_entry.config(bg="#ffafaf")
            print()

        else:
            # if there are no error, generate text file and then close dialouge
            filename = filename + ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # Heading for Stats
            f.write(date_display)
            f.write("\n\n")
            f.write("Total Rounds\n\n")

            f.write(str(total_round) + "\n")

            f.write("\n\n")
            f.write("Rounds Played\n\n")

            f.write(str(current_round) + "\n")
            # Heading for Rounds
            f.write("\nCorrect Answer\n\n")
            f.write(str(points) + "\n")
            # add new line at the end of each item


            # close file
            f.close()

            # close dialogue
            self.close_export(partner)

    def close_export(self, partner):
        # Put export button back
        partner.export_btn.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Start(root)
    root.mainloop()
