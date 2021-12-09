def sort(data):
    for this_index in range(len(data) - 1):
        swap_index = find_smallest(data, this_index)
        if swap_index != this_index:
            swap(data, swap_index, this_index)


def find_smallest(sort_data, start_index):
    swap_index = start_index
    for index in range(start_index + 1, len(sort_data)):
        if sort_data[index] < sort_data[swap_index]:
            swap_index = index
    return swap_index


def swap(swap_data, from_index, to_index):
    swap_data[from_index], swap_data[to_index] =\
        swap_data[to_index], swap_data[from_index]


results = [5, 8, 1, 3, 10]

sort(results)

for result in results:
    print(result, end=' ')
