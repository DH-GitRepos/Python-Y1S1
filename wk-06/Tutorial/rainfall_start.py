# display yearly rainfall as a histogram

rainfall = {
    'Jan': 0, 'Feb': 0, 'Mar': 0, 'Apr': 0, 'May': 0, 'Jun': 0,
    'Jul': 0, 'Aug': 0, 'Sep': 0, 'Oct': 0, 'Nov': 0, 'Dec': 0
}

highest = 0

for month in rainfall:
    invalid_response = True
    while invalid_response:
        try:
            rainfall[month] = int(input("Please enter the rainfall for {} (in mm): ".format(month)))
        except ValueError:
            print("Must be a number. Please try again.")
        else:
            invalid_response = False
            
    if highest < rainfall[month]:
        highest = rainfall[month]

for row in range(highest, 0, -1):
    for month, value in rainfall.items():
        if value >= row:
            print("  X  ", end='')
        else:
            print("     ", end='')
    print()

print("".join(map(lambda month: " {} ".format(month), rainfall)))

# https://realpython.com/python-lambda/
# https://realpython.com/python-map-function/