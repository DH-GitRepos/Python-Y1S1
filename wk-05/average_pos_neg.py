# PROJECT: (WK-05) Average of positive and negative integers
# Solution written by Darren Halpin

# set placeholder variables
integer_input_list = []

counter_positive = 0
total_positive = 0
num_of_pos_ints = 0
output_str_positive = ""

counter_negative = 0
total_negative = 0
num_of_neg_ints = 0
output_str_negative = ""

# get input values and assign to input list
print("Please enter 10 integers, positive or negative:")

for num in range(1, 11):
    user_input = int(input("Enter integer " + str(num) + ": "))
    integer_input_list.append(user_input)
    if user_input < 0:
        counter_negative = counter_negative + 1
        total_negative = total_negative + user_input
        output_str_negative = output_str_negative + str(user_input)
        if num < 11:
            output_str_negative = output_str_negative + " "
    else:
        counter_positive = counter_positive + 1
        total_positive = total_positive + user_input
        output_str_positive = output_str_positive + str(user_input)
        if num < 11:
            output_str_positive = output_str_positive + " "

if counter_positive > 0:
    positive_average = total_positive / counter_positive
    print("\nNumber of positive integers: " + str(counter_positive) + " - ( " + output_str_positive + ")")
    print("Average of positive integers: " + str(positive_average))
else:
    print("\nNo positive integers recorded.")

if counter_negative > 0:
    negative_average = total_negative / counter_negative
    print("\nNumber of negative integers: " + str(counter_negative) + " - ( " + output_str_negative + ")")
    print("Average of negative integers: " + str(negative_average))
else:
    print("\nNo negative integers recorded.")
