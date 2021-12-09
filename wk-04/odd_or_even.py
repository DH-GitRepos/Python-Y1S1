# PROJECT: (WK-04) Odd or Even
# Solution written by Darren Halpin

# get input integer
number_in = int(input("Please input an integer: "))

# modulus returns boolean value
if number_in % 2 == 0:
    print("You entered an EVEN number (" + str(number_in) + ")")
else:
    print("You entered an ODD number (" + str(number_in) + ")")

