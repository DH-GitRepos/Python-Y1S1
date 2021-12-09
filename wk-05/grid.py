# PROJECT: (WK-05) Grid
# Solution written by Darren Halpin

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

for row in range(rows):
    for col in range(columns):
        print("*", end="")
    print()
