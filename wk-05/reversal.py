# PROJECT: (WK-05) Reversing an integer
# Solution written by Darren Halpin

exit_value = False

while not exit_value:

    try:
        # get input integer
        input_value = int(input("Enter an integer of at least 2 digits or -1 to quit: "))

        # check for exit value
        if input_value == -1:
            print("Program end.")
            exit_value = True

        # if not exit value, continue
        else:
            # get length of integer digits
            count = 0
            number = input_value
            while number > 0:
                number = number // 10
                count = count + 1

            # check if number is less than 2 digits, or more than 11
            if count < 2 or count > 11:
                # check if number is negative
                if input_value < 0:
                    print("ERROR:(NEG): The number should be a positive integer. Please try again.")
                else:
                    print("ERROR:(LEN): The number should be between 2 and 11 digits. Please try again.")

            # if all ok, reverse number and output
            else:
                next_num = input_value
                reversed_num = 0

                while next_num != 0:
                    remainder = int(next_num % 10)
                    reversed_num = reversed_num * 10 + remainder
                    next_num = int(next_num / 10)

                print("Your integer reversed is: " + str(reversed_num))

    # if the input value is not a number, throw error
    except:
        print("ERROR(NaN): Input value is not a number, please try again.")

