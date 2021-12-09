# PROJECT: (WK-05) Sum of positive and negative integers
# Solution written by Darren Halpin

# set placeholder variables
integer_input_list = []

counter_positive = 0
output_str_positive = ""

counter_negative = 0
output_str_negative = ""

# get input values and assign to input list
print("Please enter 10 integers, positive or negative:")

for num in range(1, 11):
    user_input = int(input("Enter integer " + str(num) + ": "))
    integer_input_list.append(user_input)
    if user_input < 0:
        counter_negative = counter_negative + user_input
        output_str_negative = output_str_negative + str(user_input)
        if num < 11:
            output_str_negative = output_str_negative + " "
    else:
        counter_positive = counter_positive + user_input
        output_str_positive = output_str_positive + str(user_input)
        if num < 11:
            output_str_positive = output_str_positive + " "

print("\nSum of positive integers: " + str(counter_positive) + " - ( " + output_str_positive + ")")
print("Sum of negative integers: " + str(counter_negative) + " - ( " + output_str_negative + ")")
