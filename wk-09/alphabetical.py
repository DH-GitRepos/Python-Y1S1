# PROJECT: (WK-09) Alphabetical
# Solution written by Darren Halpin


def sort(data_list):
    for i in range(len(data_list) - 1):
        smallest = find_smallest(data_list, i)
        if smallest != i:
            swap(data_list, smallest, i)


def find_smallest(data_list, start):
    swap_index = start
    for i in range(start + 1, len(data_list)):
        if data_list[i] < data_list[swap_index]:
            swap_index = i
    return swap_index


def swap(data_list, index_a, index_b):
    data_list[index_a], data_list[index_b] = data_list[index_b], data_list[index_a]


def output_data(data_list, message):
    print("\n{}".format(message))
    for item in range(len(data_list)):
        print(data_list[item], end='')
        if item != len(data_list) - 1:
            print(", ", end='')
    print()


strings_arr = []

print("Please input 5 strings:")

for x in range(5):
    strings_arr.append(input("Input a string> "))

output_data(strings_arr, "You entered: ")

sort(strings_arr)

output_data(strings_arr, "Output sorted:")


