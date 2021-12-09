# calculate the average of four numbers

num_name = ['first', 'second', 'third', 'fourth']

running_total = 0

for name in num_name:
    running_total += int(input("Enter {} integer: ".format(name)))

avg = running_total / 4

print("Average is: " + str(avg))
