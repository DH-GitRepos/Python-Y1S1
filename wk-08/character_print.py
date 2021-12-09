# PROJECT: (WK-08) Character Print
# Solution written by Darren Halpin

def character_print(char, num):
    print("\n" + char * num)


character = input("Enter a text character:\n> ")
num_of_times = int(input("Enter number of times to print:\n> "))

character_print(character, num_of_times)
