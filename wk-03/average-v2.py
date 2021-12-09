# PROJECT: (WK-03) Average
# Solution written by Darren Halpin

total = 0

for i in range(1,5):
    num = int(input("Enter integer #{}: ".format(i)))
    total += num

avg = total / 4
print("\nAverage is: " + str(avg))
