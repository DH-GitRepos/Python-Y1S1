# PROJECT: (WK-06) Reversal
# Solution written by Darren Halpin

num_list = []

print("Please enter 5 integers:")

for num in range(5):
    num_list.append(int(input("Enter integer {}: ".format(str(num + 1)))))

print("\nReversed output:")
num_list_len = len(num_list)

for num in range(num_list_len, 0, -1):
    print(str(num_list[num - 1]) + " ", end="")
