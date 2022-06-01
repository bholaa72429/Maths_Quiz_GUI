# generate two random number
# put them together in an equation (n + n = )
# get users input
# check if it's right or wrong

import random

# generating two random
num_one = random.randint(1,10)
num_two = random.randint(1,10)
# putting it in an equation
equation = int(input("Question: {} + {} = ".format(num_one,num_two)))