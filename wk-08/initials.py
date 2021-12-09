# PROJECT: (WK-08) Initials
# Solution written by Darren Halpin

name = input("Please enter your name (first name and family name)\n> ")

name_separated = name.split()

print("First name: {} \nFamily name: {}".format(name_separated[0], name_separated[1]))
