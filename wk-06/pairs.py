# PROJECT: (WK-06) A blast from the past
# Solution written by Darren Halpin

import random

# DEFINE CARDS IN THE DECK
cards = {
    0: "Jack",
    1: "Queen",
    2: "King",
    3: "Ace"
}

# MAKE RANDOM DECK FROM 4 OF EACH cards
# Define main deck list and container lists to count up to 4
deck = []
card_counter_0 = []
card_counter_1 = []
card_counter_2 = []
card_counter_3 = []

# Populate deck list with random cards, 4 of each type
while len(deck) < 16:
    new_card = random.randint(0, 3)
    if new_card == 0:
        if len(card_counter_0) < 4:
            card_counter_0.append(new_card)
            deck.append(new_card)
        else:
            new_card = random.randint(0, 3)
    elif new_card == 1:
        if len(card_counter_1) < 4:
            card_counter_1.append(new_card)
            deck.append(new_card)
        else:
            new_card = random.randint(0, 3)
    elif new_card == 2:
        if len(card_counter_2) < 4:
            card_counter_2.append(new_card)
            deck.append(new_card)
        else:
            new_card = random.randint(0, 3)
    else:
        if len(card_counter_3) < 4:
            card_counter_3.append(new_card)
            deck.append(new_card)
        else:
            new_card = random.randint(0, 3)

# CREATE GRIDS
# Deal cards deck into card grid
grid = [[deck.pop() for x in range(1, 5)] for y in range(1, 5)]
# Make grid display mask to mark off paired cards
grid_mask = [["*" for x in range(1, 5)] for y in range(1, 5)]

# SET PRE GAME CONDITIONS
grid_complete = False
pairs_found = 0
guess_counter = 0
card1_paired = True
card2_paired = True
ask_for_second_card = False

# START GAME
print("=" * 14)
print("FIND THE PAIRS")
print("=" * 14)
print("Instructions:")
print("Enter the row and column numbers that correspond to a card position.")
print("Try and find all the pairs to win.\n")

while pairs_found < 8:

    # Draw game grid
    print("\n  0 1 2 3")
    for row in range(4):
        print(str(row) + " ", end="")
        for col in range(4):
            var = grid_mask[row][col]
            print("{} ".format(var), end="")
        print()

    # Get user input

    # Ask for card 1 (reject and repeat if input invalid)
    while card1_paired:
        print("\nSELECT THE POSITION OF CARD 1")
        pos_x_card1 = int(input("Enter card 1 column number (0-3): "))
        pos_y_card1 = int(input("Enter card 1 row number (0-3): "))

        # check the input is in grid range
        if pos_x_card1 > 3 or pos_y_card1 > 3:
            print("ERROR: Out of range row/column, try again.")

        # check the input against the mask grid for an already paired position
        elif grid_mask[pos_y_card1][pos_x_card1] == "X":
            print("ERROR: This card has already been paired, choose a different card.")

        else:
            card_1 = grid[pos_y_card1][pos_x_card1]
            card_val1 = cards[card_1]
            card1_paired = False
            ask_for_second_card = True
            print("CARD VALUE: {}".format(card_val1))

    # Ask for card 2 (reject and repeat if input invalid)
    if ask_for_second_card:
        while card2_paired:
            print("SELECT THE POSITION OF CARD 2")
            pos_x_card2 = int(input("Enter card 2 column number (0-3): "))
            pos_y_card2 = int(input("Enter card 2 row number (0-3): "))

            # check the card 2 selection is not the same as card 1
            if pos_y_card2 == pos_y_card1 and pos_x_card1 == pos_x_card2:
                print("ERROR: You just chose that card, pick another!")

            # check the input is in grid range
            elif pos_x_card2 > 3 or pos_y_card2 > 3:
                print("ERROR: Out of range row/column, try again.")

            # check the input against the mask grid for an already paired position
            elif grid_mask[pos_y_card2][pos_x_card2] == "X":
                print("This card has already been paired")

            else:
                card_2 = grid[pos_y_card2][pos_x_card2]
                card_val2 = cards[card_2]
                card2_paired = False
                print("CARD VALUE: {}".format(card_val2))

    # CHECK RESULT
    print("-" * 35)

    # check for a pair
    if card_1 == card_2:
        print("Well done, that's a pair!\n")
        grid_mask[pos_y_card1][pos_x_card1] = "X"
        grid_mask[pos_y_card2][pos_x_card2] = "X"
        pairs_found += 1
        guess_counter += 1

        # check for end game
        if pairs_found == 8:
            print("CONGRATULATIONS, YOU COMPLETED THE GAME!")
            print("You guessed {} pairs in total.".format(guess_counter))

        else:
            # set loop restart conditions
            card1_paired = True
            card2_paired = True
            ask_for_second_card = False

    # if not a pair
    else:
        print("No match, try again.\n")
        guess_counter += 1

        # set loop restart conditions
        card1_paired = True
        card2_paired = True
        ask_for_second_card = False

