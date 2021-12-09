# time flies program

import re

age = input("Please enter your age: ")

# input validation
rx_pattern = "^\d{1,3}$"
match = re.match(rx_pattern, age)

if match:
    age_calc = int(age)
    print("Current age is: " + str(age_calc) + "\nAge before last birthday was: " + str(age_calc - 1) +
          "\nAge after next birthday will be: " + str(age_calc + 1))

else:
    print("Please enter a valid age (integer).")
    exit()


