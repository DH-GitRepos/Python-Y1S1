# PROJECT: (WK-05) Match the dice
# Solution written by Darren Halpin

import random

dice = ["1", "2", "3", "4", "5", "6"]
throw_counter = 0

double_throw = False

while not double_throw:
    dice_1_throw = random.randint(0, 5)
    dice_2_throw = random.randint(0, 5)
    throw_counter = throw_counter + 1
    if dice_1_throw == dice_2_throw:
        double_throw = True
        print("Throw " + str(throw_counter) + ": DICE 1: (" + str(dice_1_throw + 1) + "), DICE 2: ("
              + str(dice_2_throw + 1) + ")")
        print("\nNUMBER OF THROWS TO GET DOUBLE: " + str(throw_counter))
    else:
        print("Throw " + str(throw_counter) + ": DICE 1: (" + str(dice_1_throw + 1) + "), DICE 2: ("
              + str(dice_2_throw + 1) + ")")
        double_throw = False
