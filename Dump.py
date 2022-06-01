# adding instructions

import random

# function to print statements with special character
def h1_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))

# int-check function for the rounds
def intcheck(question,low,high):
    valid = False
    error = "Whoops! Please enter an number "
    while not valid:
        try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print("Please Enter a Number between 1 and 10")
                print()

        except ValueError:
            print(error)

# function to check the answer
def check(num_one, sign, num_two):
    # For addiction
    if sign == '+':
        ans_add = num_one + num_two
        return ans_add
    # For subtraction
    elif sign == '-':
        ans_minus = num_one - num_two
        return ans_minus
    # For multiplication
    else:
        ans_multiply = num_one * num_two
        return ans_multiply

# Main routine

# Instruction
h1_statement("*** Welcome to the Great Maths Quiz ***", "*")
print("--> There are addition, multiplication and subtraction questions in this quiz. \n"
        "--> Basic Math Quiz is a great way to check math skills! \n"
      "--> There are a range of questions with easy and a bit difficult level which can be challenging. \n"
       "--> After each quiz is completed,you can view and print your very own score report.\n"
      "    Which includes game stats and a history/summary of your quiz. \n"
       "--> At that point you can either pay again ( press <enter> when prompted)\n"
      "    or quit by pressing any key.\n"
      "--> Please Note: You can choose between 1-10 question in each game at the start.\n"
      "----------------------------------------------------------------------------------")

keep_going = ""
while keep_going == "":
    rounds = intcheck("How many questions would you like to play with ? ", 1, 10)
    rounds_played = 0
    correct_round = 0

    # defining the following terms
    question = ""
    answer = ""
    comment = ""
    equation = ""

    # empty list to store the question therefore hold the history
    game_history = []

    # question counter
    while rounds_played < rounds:
        print()
        print("--> Question {} of {}  ".format(rounds_played+1,rounds))
        rounds_played += 1

        # generating two random number
        symbol = ['+', '-', '*']
        # variety of feedback
        good_comm = ["Good job!", "Well done!", "Keep it up! ", "Prefect!","Excellent Work!"]
        bad_comm = ["Wrong Answer","Not Right","Try Again","Oops...","Incorrect",]

        # randomly generating two numbers and symbol to form a equation
        num_one = random.randint(1, 15)
        num_two = random.randint(1, 10)
        sign = random.choice(symbol)


        valid = False
        while not valid:
            try:
                # putting it in an equation
                equation = int(input(" Please Answer The Question {} {} {} = ".format(num_one, sign, num_two)))
                # made to display question in end history
                question = ("{} {} {} = {} ".format(num_one, sign, num_two,equation))
                answer = check(num_one, sign, num_two)
                # check if it right/wrong and give feedback
                if equation == answer:
                    comment = "Correct"
                    h1_statement(random.choice(good_comm),"#!")
                    # to calculate percentage
                    correct_round += 1
                    break
                else:
                    comment = "Incorrect"
                    h1_statement(random.choice(bad_comm),"~-")
                    h1_statement('The Correct Answer is : {}'.format(answer),"-~")
                    break
            # if user enters invalid
            except ValueError:
                h1_statement("Whoops! Please enter an number ","~")
        # end game history
        if comment == "Correct":
            rounds_result = "Question {}: {} |  Result: {} " .format(rounds_played,question,comment)
            game_history.append(rounds_result)
        # If users guess is wrong then display this
        else:
            rounds_result = "Question {}: {} |  Result: {} | Correct Answer = {} " .format(rounds_played,question,comment,answer)
            game_history.append(rounds_result)
    # to calculate percentage
    percentage = int(correct_round/rounds*100)

    # to print game stats
    print()
    print("****Game Statistics****")
    print("Your Accuracy Rate is : {} % ".format(percentage))
    print("Total Correct answer : {}  ".format(correct_round))
    print("Total Incorrect answer : {}  ".format(rounds-correct_round))

    # to print end game summary
    print()
    print("******** Game Summary ********")

    for item in game_history:
        print(item)

    print()
    keep_going = input("Press <enter> to play again or any key to quit: ")
    print()
#Farewell the user
h1_statement("THANK YOU FOR PLAYING","*")