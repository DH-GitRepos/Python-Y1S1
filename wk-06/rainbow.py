# PROJECT: (WK-06) Colourful
# Solution written by Darren Halpin

rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

program_end = False

while not program_end:
    in_val = int(input("Enter and integer (1-7) or -1 to quit: "))
    if in_val == -1:
        print("Program end.")
        program_end = True
    else:
        print(str(in_val) + ": " + rainbow[in_val - 1])
