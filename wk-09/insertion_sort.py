# PROJECT: (WK-09) Insertion Sort
# Solution written by Darren Halpin


def sort_descending(input_list):

    for i in range(1, len(input_list)):
        value = input_list[i]
        j = i - 1

        while j >= 0 and input_list[j] < value:
            input_list[j + 1] = input_list[j]
            j = j - 1

        input_list[j + 1] = value


def output_list(input_list, message):

    print("\n{}".format(message), end='')

    for x in range(len(input_list)):
        print("{}".format(input_list[x]), end='')
        if x < len(input_list) - 1:
            print(", ", end='')
        else:
            print(".")


input_values = []

print("\nPlease input 5 integers:\n")

for num in range(5):
    input_values.append(int(input("Enter integer {}> ".format(num+1))))

output_list(input_values, "Your entered: ")

sort_descending(input_values)

output_list(input_values, "Sorted in descending order: ")
