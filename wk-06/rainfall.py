# PROJECT: (WK-06) It never rains but it pours
# Solution written by Darren Halpin

# set up data list
rainfall_list = {
    "Jan": 0, "Feb": 0, "Mar": 0, "Apr": 0, "May": 0, "Jun": 0,
    "Jul": 0, "Aug": 0, "Sep": 0, "Oct": 0, "Nov": 0, "Dec": 0
}

most_rainfall = 0

# get user input and populate data list
for month in rainfall_list:
    invalid_response = True
    while invalid_response:
        try:
            rainfall_list[month] = int(input("Enter the rainfall for {} (mm): ".format(month)))
        except ValueError:
            print("Input must be a number, please try again.")
        else:
            invalid_response = False

    # set highest data point
    if most_rainfall < rainfall_list[month]:
        most_rainfall = rainfall_list[month]

# OUTPUT ROWS OF DATA
print("\n")

for row in range(most_rainfall, 0, -1):
    for month, value in rainfall_list.items():
        if value >= row:
            print("  X  ", end='')
        else:
            print("     ", end='')
    print()

for month in rainfall_list.keys():
    print(" {} ".format(month), end='')

print("\n")
