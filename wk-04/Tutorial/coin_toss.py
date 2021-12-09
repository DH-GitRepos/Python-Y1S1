# PROJECT: (WK-04) Heads or tails
# Solution written by Darren Halpin

import random

coin_toss = random.randint(0, 1)

if coin_toss == 0:
    result_check = "h"
    result_msg = "heads"
else:
    result_check = "t"
    result_msg = "tails"

guess = input("Heads (h) or tails (t)? ")

user_guess_correct = guess.casefold() == result_check

if user_guess_correct:
    print("You guessed correct, the result was " + result_msg + "!")
else:
    print("You guessed wrong, the result was " + result_msg + "!")



