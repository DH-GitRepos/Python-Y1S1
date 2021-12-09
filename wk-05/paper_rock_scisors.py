# PROJECT: (WK-05) Child's Play
# Solution written by Darren Halpin

import random

# set game variables
score_computer = 0
score_player = 0
points_to_win_comp = 3
points_to_win_player = 3
options = ["rock", "paper", "scissors"]
msg_draw = "It was a draw"
msg_comp_win = "The computer won."
msg_player_win = "Congratulations, you win."

# output game start message
print("=" * 26)
print("ROCK, PAPER, SCISSORS GAME")
print("=" * 26)
print("Choose from \"rock\", \"paper\", or \"scissors\".")
print("First to 3 wins!")
print("*" * 20)

# run game
while score_computer < 4 or score_computer < 4:

    # players turn
    player_val = input("Enter your selection: ")
    print("You chose: " + str(player_val.capitalize()))

    # computers turn
    go_computer = random.randint(0, 2)
    computer_val = options[go_computer]
    print("The computer chose: " + str(computer_val.capitalize()))

    # decide winner and update scores
    if player_val.casefold() == computer_val.casefold():
        print(msg_draw)
    elif player_val.casefold() == "rock" and computer_val.casefold() == "paper":
        score_computer += 1
        points_to_win_comp -= 1
        print(msg_comp_win)
    elif player_val.casefold() == "rock" and computer_val.casefold() == "scissors":
        score_player += 1
        points_to_win_player -= 1
        print(msg_player_win)
    elif player_val.casefold() == "paper" and computer_val.casefold() == "rock":
        score_player += 1
        points_to_win_player -= 1
        print(msg_player_win)
    elif player_val.casefold() == "paper" and computer_val.casefold() == "scissors":
        score_computer += 1
        points_to_win_comp -= 1
        print(msg_comp_win)
    elif player_val.casefold() == "scissors" and computer_val.casefold() == "rock":
        score_computer += 1
        points_to_win_comp -= 1
        print(msg_comp_win)
    elif player_val.casefold() == "scissors" and computer_val.casefold() == "paper":
        score_player += 1
        points_to_win_player -= 1
        print(msg_player_win)

    # output round end message
    print("You need : {} to complete the game.".format(points_to_win_player))
    print("The computer needs : {} to complete the game.".format(points_to_win_comp))
    print("*" * 20)

    # output end game message if a player reaches 3 points, then quit
    if score_computer == 3:
        print("Commiserations the computer won...")
        print("Game over...")
        exit()
    elif score_player == 3:
        print("Congratulations, you win!")
        print("Game over...")
        exit()
