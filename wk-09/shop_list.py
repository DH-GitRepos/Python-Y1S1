# PROJECT: (WK-09) Shop list
# Solution written by Darren Halpin

def split_string(string_in):
    string_index_end = 0
    pair = []

    for character in string_in:
        if character.isdigit():
            substring_description = string_in[0:string_index_end]
            substring_price = string_in[string_index_end - 1:len(string_in)]
            pair = [substring_description.strip(), format(float(substring_price.strip()), '.2f')]
            break
        else:
            string_index_end += 1

    return pair


def process_input_list(raw_list):
    shop_list = {}
    for item in range(len(raw_list)):
        dict_values = split_string(raw_list[item])
        returned_key = dict_values[0]
        returned_value = dict_values[1]
        shop_list[returned_key] = returned_value

    return shop_list


def output_shopping_list(input_list):
    for key, value in input_list.items():
        print("{} {}".format(key, value))


def reorder(data_list):

    temp_list = []
    new_ordered_list = {}

    # Get values from input data
    for key, value in data_list.items():
        temp_list.append(value)

    # sort the values
    sort(temp_list)

    # rebuild the input list from the ordered values
    for item in temp_list:
        # Get data_list key name using using temp_list value (you're a wizard, Harry!)
        out_key = list(data_list.keys())[list(data_list.values()).index(item)]
        # set value item
        out_value = item
        # update new dictionary
        new_ordered_list.update({out_key: out_value})

    # return reordered dictionary
    return new_ordered_list


def sort(data_list):
    for data_item in range(len(data_list) - 1):
        swap_index = find_smallest(data_list, data_item)
        if swap_index != data_item:
            swap(data_list, swap_index, data_item)


def find_smallest(data_sort, start_index):
    swap_index = start_index
    for index in range(start_index + 1, len(data_sort)):
        if data_sort[index] > data_sort[swap_index]:
            swap_index = index
    return swap_index


def swap(data_swap, from_index, to_index):
    data_swap[from_index], data_swap[to_index] = data_swap[to_index], data_swap[from_index]


# BEGIN MAIN EXECUTION #
print("\nPlease input 5 shopping items and their prices.")
print("For example: Kitchen Foil 2.99\n")

# Get user input
raw_input = []
for x in range(5):
    raw_input.append(input("Input item {}> ".format(x + 1)))

# convert raw input into dictionary
dict_list = process_input_list(raw_input)

# output dictionary
print("\nTHE LIST YOU ENTERED:\n")
output_shopping_list(dict_list)

# reorder input dictionary
ordered_list = reorder(dict_list)

# output reordered dictionary
print("\nYOUR LIST ORDERED:\n")
output_shopping_list(ordered_list)
