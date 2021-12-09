# PROJECT: (WK-08) Multiple Initials
# Solution written by Darren Halpin

name = input("Please enter your full name\n> ")

name_list = name.split()
name_list_len = len(name_list)

initials_list = []

# PROCESS NAMES ARRAY INTO INITIALS ARRAY
for item in range(name_list_len):
    name_list[item - 1] = name_list[item - 1].strip()

    # check string item for hyphen
    hyphenated = name_list[item].find("-")

    if hyphenated != -1:
        initial_first = name_list[item][0].upper()
        initial_second = name_list[item][hyphenated + 1].upper() + "."
        initial_str = initial_first + "-" + initial_second
        initials_list.append(initial_str)
    else:
        initial_first = name_list[item][0].upper() + "."
        initials_list.append(initial_first)

# OUTPUT INITIALS
output_string = "Initials output: "
initials_list_len = len(initials_list)

for item in range(initials_list_len):
    output_string += initials_list[item]

print(output_string)
