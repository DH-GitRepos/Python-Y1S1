# PROJECT: (WK-09) Insertion Sort
# Solution written by Darren Halpin


def sort_ascending(input_list):

    for i in range(1, len(input_list)):
        value = input_list[i]
        j = i - 1

        while j >= 0 and input_list[j] > value:
            input_list[j + 1] = input_list[j]
            j = j - 1

        input_list[j + 1] = value


def sort_descending(input_list):

    for i in range(1, len(input_list)):
        value = input_list[i]
        j = i - 1

        while j >= 0 and input_list[j] < value:
            input_list[j + 1] = input_list[j]
            j = j - 1

        input_list[j + 1] = value


input_values = [3, 7, 9, 5, 1]

#for num in range(5):
#    input_values.append(int(input("Enter integer {}> ".format(num))))

sort_descending(input_values)

print(input_values)

sort_ascending(input_values)

print(input_values)
