# PROJECT: (WK-10) Built in errors
# Solution written by Darren Halpin

# ZeroDivisionError
a = 0
b = 3

try:
    c = b / a
except ZeroDivisionError:
    print("Do something nice: ZeroDivisionError")

# IndexError
my_name = ["darren", "halpin"]
try:
    print(my_name[2])
except IndexError:
    print("Do something nice: IndexError")

# KeyError
my_name = {"first": "darren", "last": "halpin"}
try:
    print(my_name["middle"])
except KeyError:
    print("Do something nice: KeyError")

# FileNotFoundError
try:
    file = open("some_file.txt")
except FileNotFoundError:
    print("Do something nice: FileNotFoundError")

# TypeError
a = 3
b = "two"
try:
    c = a + b
except TypeError:
    print("Do something nice: TypeError")

# ValueError
number = "nine"
try:
    int(number)
except ValueError:
    print("Do something nice: ValueError")
