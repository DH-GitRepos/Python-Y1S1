# PROJECT: (WK-07) A Simple Calculator
# Solution written by Darren Halpin

# write intro info
print("Simple calculator")
print("-" * 17)
print("Input 2 integers and an operator > ")

# get user input
int_1 = int(input("\nEnter integer 1: "))
int_2 = int(input("Enter integer 2: "))
operator = input("Enter operator ( - + * / ): ")

# check operator input and output result
if operator == "+":
    sum_total = int_1 + int_2
    print("\nYour sum is {} + {} and the answer is {}".format(int_1, int_2, sum_total))

elif operator == "-":
    sum_total = int_1 - int_2
    print("\nYour sum is {} - {} and the answer is {}".format(int_1, int_2, sum_total))

elif operator == "*":
    sum_total = int_1 * int_2
    print("\nYour sum is {} * {} and the answer is {}".format(int_1, int_2, sum_total))

elif operator == "/":
    sum_total = float(int_1 / int_2)
    print("\nYour sum is {} / {} and the answer is {}".format(int_1, int_2, sum_total))

else:
    print("\nInvalid operator selected")

