# PROJECT: (WK-08) Character Print
# Solution written by Darren Halpin

def calculate_addition(num_1, num_2):
    result = num_1 + num_2
    print("{} + {} = {}".format(num_1, num_2, result))


def calculate_subtraction(num_1, num_2):
    result = num_1 - num_2
    print("{} - {} = {}".format(num_1, num_2, result))


def calculate_multiplication(num_1, num_2):
    result = num_1 * num_2
    print("{} * {} = {}".format(num_1, num_2, result))


def calculate_division(num_1, num_2):
    result = num_1 / num_2
    print("{} / {} = {}".format(num_1, num_2, result))


def calculate_remainder(num_1, num_2):
    result = num_1 % num_2
    print("The remainder of {} / {} is {}".format(num_1, num_2, result))


print("SIMPLE CALCULATOR")
print("-" * 17)
print("Enter 2 integers, then choose an operation.")
int_first = int(input("ENTER INTEGER 1:\n> "))
int_second = int(input("ENTER INTEGER 2:\n> "))
print("Pick an operation (1-5):")
print("(1) Add, (2) Subtract, (3) Multiply, (4) Divide, (5) Remainder")
operation = int(input("ENTER OPERATION OPTION:\n> "))

if operation == 1:
    calculate_addition(int_first, int_second)
elif operation == 2:
    calculate_subtraction(int_first, int_second)
elif operation == 3:
    calculate_multiplication(int_first, int_second)
elif operation == 4:
    calculate_division(int_first, int_second)
elif operation == 5:
    calculate_remainder(int_first, int_second)
else:
    print("Invalid operation selected, choose 1-5.")
