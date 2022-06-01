from tkinter import *
from functools import partial # to prevent unwanted windows

import random
import decimal

# function to check the answer
def check(num_one,sign,num_two):
    # For addiction
    if sign == '+':
        ans_add = num_one + num_two
        return ans_add
    # For subtraction
    elif sign == '-':
        ans_minus = num_one - num_two
        return ans_minus
    # For division
    elif sign == '/':
        ans_final = num_one/num_two
        # remainder = num_two * ans_divide
        # return remainder
        return ans_final
    # For multiplication
    else:
        ans_multiply = num_one * num_two
        return ans_multiply


# symbol sign for the question
symbol = ['+','-','*','/']
for item in range(5):
    # generating two random number
    num_one = random.randint(10,20)
    num_two = random.randint(1,10)
    sign = random.choice(symbol)
    valid = False
    while not valid:
        try:
            # putting it in an equation
           if sign == '/':
               clean_num = num_one * num_two
               num_one=clean_num
           answer = check(num_one,sign,num_two)
           equation = float(input("Please answer the question {} {} {} = ".format(num_one, sign, num_two)))
           # check if it right/wrong and give feedback
           if equation == answer:
             print("Correct")
             break
           else:
             print("Incorrect")
             print("The correct answer is: {}".format(answer))
             break
            # if user enters invalid
        except ValueError:
            print("oops! Please enter an number ")