# PROJECT: (WK-04) Nothing for a Pair (not in this game)
# Solution written by Darren Halpin

import random

deck = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
draw_a = random.randint(1, 13)

# PART 1
print("PART 1\n" + "=" * 6)
print("Random number generated: " + str(draw_a))
print("Card value: " + str(deck[draw_a - 1]))

# PART 2
print("\nPART 2\n" + "=" * 6)

# draw a card and display value
draw_b = random.randint(1, 13)
print("Card drawn: " + str(deck[draw_b - 1]))

# get user guess
print("\nGuess whether the next card will be higher or lower:")
guess = input("Input \'higher\' or \'lower\': ")

# draw another card and show user
draw_c = random.randint(1, 13)
print("\nNext card: " + str(deck[draw_c - 1]))

# compare user guess
if guess.casefold() == "higher":
    if draw_c > draw_b:
        print("You WIN!")
    else:
        print("You lose.")
elif guess.casefold() == "lower":
    if draw_c < draw_b:
        print("You WIN!")
    else:
        print("You lose.")

