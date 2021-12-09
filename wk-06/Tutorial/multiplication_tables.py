# Times tables

for x in range(1, 11):
    print("{:>3} times table ".format(x), end="")
    for y in range(1, 11):
        print(" {:>4} ".format(x * y), end="")
    print()
