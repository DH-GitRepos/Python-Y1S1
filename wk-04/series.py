# PROJECT: (WK-04) Numbers in a series
# Solution written by Darren Halpin

# set placeholder variables
int_positive = 0
int_negative = 0
int_input = []

# get input values and assign to input list
print("Please enter 5 integers, positive or negative:")
int_input.append(int(input("Number 1: ")))
int_input.append(int(input("Number 2: ")))
int_input.append(int(input("Number 3: ")))
int_input.append(int(input("Number 4: ")))
int_input.append(int(input("Number 5: ")))

# loop through input list and add positive and negative totals
for x in int_input:
    if x < 0:
        int_negative = int_negative + x
    else:
        int_positive = int_positive + x

# output totals
print("Sum of positive integers: " + str(int_positive))
print("Sum of negative integers: " + str(int_negative))

