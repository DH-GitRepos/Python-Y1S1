# PROJECT: (WK-05) Diamond
# Solution written by Darren Halpin

width = int(input("Enter the width of the diamond (2-40): "))

if width < 2 or width > 40:
    print("The number you entered was out of range.")
    exit()

# for centering output
max_string_length = width + width - 1
working_str_len = (width - 1) + width
current_line = "*"
# list to hold generated strings so I dont have to generate them again...
string_list = []

# GENERATE TOP OF DIAMOND
for num in range(1, width+1, 1):
    # number of characters in current string
    line_len = len(current_line)

    # last character in the string
    last_char = current_line[line_len - 1]

    # current working string length
    current_str_len = (num - 1) + num

    if num == line_len:
        output_line = current_line.strip()
        string_list.append(output_line)
        print("{0:^{i}}".format(output_line, i=max_string_length))

    elif line_len < current_str_len:

        while line_len < current_str_len + 1:

            if last_char == "*":
                current_line = current_line + " "
                line_len = len(current_line)
                last_char = current_line[line_len - 1]

            elif last_char == " ":
                current_line = current_line + "*"
                line_len = len(current_line)
                last_char = current_line[line_len - 1]

        output_line = current_line.strip()
        string_list.append(output_line)
        print("{0:^{i}}".format(output_line, i=max_string_length))

# GENERATE BOTTOM OF DIAMOND
str_list_len = len(string_list)

# remove last item in list to avoid widest line repetition
del string_list[str_list_len - 1]

list_end_position = len(string_list) - 1

# output bottom of diamond
for num in range(list_end_position, -1, -1):
    print("{0:^{i}}".format(string_list[num], i=max_string_length))
