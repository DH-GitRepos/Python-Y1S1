# simulate the toss of a coin

import random

coin_toss = random.randint(0, 1)

coin_toss_result = ('heads', 'tails')

guess = input("Please enter heads or tails: ").lower()

if coin_toss_result[coin_toss] == guess:
    print("You guessed correctly")
else:
    print("You guessed incorrectly")
