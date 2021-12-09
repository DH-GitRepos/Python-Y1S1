# get integer input of two numbers and swap them using functions

def print_int_list(data):
    print(data[0], data[1])


def swap(data):
    data[0], data[1] = data[1], data [0]


numbers = list(map(int, input("Enter two integers: ").split()))

print("You entered: ", end='')

# print (strings)
# numbers = list(map(int(strings)))

print_int_list(numbers)

swap(numbers)

print("Your entries swapped: ", end='')

print_int_list(numbers)

