# PROJECT: (WK-08) Swap
# Solution written by Darren Halpin

def swap(list_to_swap):
    out_list = list(reversed(list_to_swap))
    return out_list


def print_int_list(list_of_ints):
    swap_ints = swap(list_of_ints)
    print("You entered: {} {}. Your entries swapped: {} {}."
          .format(list_of_ints[0], list_of_ints[1], swap_ints[0], swap_ints[1]))


int_list = []
print("NUMBER SWAPPER")
print("-" * 14)
print("Enter 2 integers:")
for i in range(2):
    int_input = int(input("ENTER AN INTEGER :\n> "))
    int_list.append(int_input)

print_int_list(int_list)
