# PROJECT: (WK-08) You sank my battleship!
# Solution written by Darren Halpin

import random


def draw_game_board():
    for row in range(0, 6, 1):
        for col in range(0, 6, 1):
            var = gameboard_show[row][col]
            print("{:^3}".format(var), end="")
        print()


def create_new_random_destroyer_position():
    # plot random first coordinate of destroyer piece 1
    first_position_row = random.randint(1, 5)
    first_position_col = random.randint(1, 5)

    # pick random horizontal or vertical placement of second piece
    h_or_v = random.randint(0, 1)
    if h_or_v == 0:  # horizontal placement
        second_position_row = first_position_row
        # pick left or right placement from first coordinate
        l_or_r = random.randint(0, 1)
        if l_or_r == 0:  # second position left of first
            # CHOSE LEFT PLACEMENT
            if first_position_col == 1:
                second_position_col = first_position_col + 1
            elif first_position_col == 5:
                second_position_col = first_position_col - 1
            else:  # place left
                second_position_col = first_position_col - 1

        else:
            # CHOSE RIGHT PLACEMENT
            if first_position_col == 1:
                second_position_col = first_position_col + 1
            elif first_position_col == 5:
                second_position_col = first_position_col - 1
            else:  # place right
                second_position_col = first_position_col + 1

    else:  # vertical placement
        second_position_col = first_position_col
        # pick up or down placement from first coordinate
        u_or_d = random.randint(0, 1)
        if u_or_d == 0:  # second position up from first
            # CHOSE UP PLACEMENT
            if first_position_row == 1:
                second_position_row = first_position_row + 1
            elif first_position_row == 5:
                second_position_row = first_position_row - 1
            else:  # place left
                second_position_row = first_position_row - 1

        else:  # second position down from first
            #  CHOSE D0WN PLACEMENT
            if first_position_row == 1:
                second_position_row = first_position_row + 1
            elif first_position_row == 5:
                second_position_row = first_position_row - 1
            else:  # place right
                second_position_row = first_position_row + 1

    gameboard_hidden[first_position_row][first_position_col] = "[D]"
    gameboard_hidden[second_position_row][second_position_col] = "[D]"


def check_shot(in_shot):
    shot_separated = shot.split()

    try:
        shot_row = int(shot_separated[0])
        shot_col = int(shot_separated[1])

        shot_position = gameboard_hidden[shot_row][shot_col]
        shot_taken = gameboard_show[shot_row][shot_col]

        if shot_row > 0 and shot_col > 0:

            if shot_position == "[D]":
                hit = True
                msg = "Well done you HIT!"
                gameboard_show[shot_row][shot_col] = "[H]"
            else:
                if shot_taken == "[ ]":
                    hit = False
                    msg = "Sorry you missed."
                    gameboard_show[shot_row][shot_col] = "[M]"
                else:
                    hit = False
                    msg = "You already tried this position!"

        else:
            msg = "Invalid coordinates entered, try again."
            hit = False

    except:
        hit = False
        msg = "Invalid coordinate characters entered, try again."

    return_values = [hit, msg]

    return return_values


gameboard_show = {
    0: {0: " ", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5"},
    1: {0: "1", 1: "[ ]", 2: "[ ]", 3: "[ ]", 4: "[ ]", 5: "[ ]"},
    2: {0: "2", 1: "[ ]", 2: "[ ]", 3: "[ ]", 4: "[ ]", 5: "[ ]"},
    3: {0: "3", 1: "[ ]", 2: "[ ]", 3: "[ ]", 4: "[ ]", 5: "[ ]"},
    4: {0: "4", 1: "[ ]", 2: "[ ]", 3: "[ ]", 4: "[ ]", 5: "[ ]"},
    5: {0: "5", 1: "[ ]", 2: "[ ]", 3: "[ ]", 4: "[ ]", 5: "[ ]"}
    }

gameboard_hidden = {
    0: {0: " ", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5"},
    1: {0: "1", 1: "[ ]", 2: "[ ]", 3: "[ ]", 4: "[ ]", 5: "[ ]"},
    2: {0: "2", 1: "[ ]", 2: "[ ]", 3: "[ ]", 4: "[ ]", 5: "[ ]"},
    3: {0: "3", 1: "[ ]", 2: "[ ]", 3: "[ ]", 4: "[ ]", 5: "[ ]"},
    4: {0: "4", 1: "[ ]", 2: "[ ]", 3: "[ ]", 4: "[ ]", 5: "[ ]"},
    5: {0: "5", 1: "[ ]", 2: "[ ]", 3: "[ ]", 4: "[ ]", 5: "[ ]"}
}

hit_counter = 0
create_new_random_destroyer_position()

print("Sink the battleship!")
print("-" * 20)
print("Select a row (1-5) and column (1-5) to rake a shot\n")
draw_game_board()

while hit_counter != 2:

    shot = input("\nEnter a shot (r c): ")
    print()

    # quick exit option
    if shot == "x":
        exit()

    shot_result = check_shot(shot)

    draw_game_board()

    if shot_result[0]:

        print(shot_result[1])
        hit_counter += 1
    else:
        # msg = "Sorry you missed."
        print(shot_result[1])

    if hit_counter == 2:
        print("Glug, glug, glug...you won.")
        exit()
