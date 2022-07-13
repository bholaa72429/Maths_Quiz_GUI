# Combine rounds gui with current work
# generate questions
from tkinter import *

from functools import partial # to prevent unwanted windows

import random
import xlrd

class Start:
      def __init__(self, parent):

          # formatting variable
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

      # Question goes here
      # Entry box...
      # play button goes here (row 3)
      self.play_button = Button(self.game_frame, text="Start",
                                bg="#FFFF33", font="Arial 15 bold", width=10,
                                pady=10, padx=10, command=self.try_again)
      self.play_button.grid(row=3)

      self.answer_entry = Entry(self.game_frame, font="Arial 15 bold",width=10)
      self.answer_entry.grid(row=5)

      # Submit Button
      self.submit_button = Button(self.game_frame, text="Submit", font="Arial 15 bold", bg="#00FA9A", width=10,
                                  command=lambda: self.check_ans(self.answer_entry_label))
      self.submit_button.grid(row=8, pady=10, padx=10)


      self.answer_entry_label = Label(self.game_frame,font="Arial 15 bold",fg="red", text="",pady=10)
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
      self.help_button.grid(row=0, column=0 , padx=10)

      self.stats_button = Button(self.help_export_frame, text= "Game Stats...",
                                 font="Arial 15 bold", bg="#003366", fg="white")
      self.stats_button.grid(row=0, column=2, padx=10)

  def reveal_questions(self):
      current_round = self.round.get()

      # For testing purposes, just add 10
      current_round += 10

      # set rounds to adjust rounds
      self.round.set(current_round)

      # Edit label so user can see their balance
      self.rounds_label.configure(text="Rounds: {}".format(current_round))

  def try_again(self):
      data = ("C:\Users\anshi\OneDrive - Massey High School\Desktop\SCHOOL_WORK\Trial.xlsx")
      wb = xlrd.open_workbook(data)
      sheet = wb.sheet_by_index(0)
      value = (sheet.cell_value(0,0))
      self.question_label= Label(self.game_frame,text=f"{value}",font="Arial 15 bold", )
      self.question_label.grid(row=3, pady=10, padx=10)
      d=eval(value)
      return d


  def check_ans(self,answer_entry):
      correct_ans = int(self.try_again())

      # get user answer
      #user_ans = self.answer_entry.get()
      user_ans= int(self.answer_entry.get())
      print(user_ans,correct_ans)
      # set error bg colours (and assume that there are no
      # errors at the start
      #error_back = "#ffafaf"
      #has_errors = "no"

      # change bg to white (for testing purposes)
      self.answer_entry.config(bg="white")
      self.answer_entry_label.config(text="")


      if user_ans == correct_ans:
          result_feedback = "RIGHT"
          self.answer_entry_label.config(text=result_feedback)
          self.answer_entry.destroy()
      else:
          result_feedback = "Wrong"
          self.answer_entry_label.config(text=result_feedback)


# main routine
if __name__ == "__main__":
  root = Tk()
  root.title("Math Quiz")
  something = Start(root)
  root.mainloop()



