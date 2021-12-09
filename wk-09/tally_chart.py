# PROJECT: (WK-09) Tally Ho
# Solution written by Darren Halpin

def check_vote(in_vote):

    match in_vote:
        case "A":
            cast_vote(in_vote)
        case "B":
            cast_vote(in_vote)
        case "C":
            cast_vote(in_vote)
        case "D":
            cast_vote(in_vote)
        case "E":
            cast_vote(in_vote)
        case _:
            print("You entered an invalid option, please try again.\n")


def cast_vote(in_vote):

    print("Thankyou, you voted for candidate {}\n".format(in_vote))
    candidates[in_vote]["votes"] += 1


def show_candidates():

    counter = 1
    print("Please choose a candidate to vote for:")
    for person in candidates:
        print("{} ({})".format(candidates[person]["name"], person), end='')
        if counter < 5:
            print(", ", end='')
        else:
            print(".", end='')
        counter += 1


def capture_vote():

    vote = input("\nPlease choose your candidate (A-E).\n> ")
    if vote == "1":
        print("Thanks for voting.\nThe results are:\n")
        show_votes()
        return vote

    else:
        check_vote(vote.upper())


def show_votes():

    display_list = reorder_votes(candidates)

    for key, value in display_list.items():
        print("{:>2} votes for {}".format(value, key))


def reorder_votes(data_list):

    temp_list = []
    new_ordered_list = {}

    # Get values from input data
    for key, value in data_list.items():
        temp_list.append(value["votes"])

    # sort the values
    sort(temp_list)

    # populate sorted output dictionary
    for num_votes in temp_list:
        for record in data_list:
            if data_list[record]["votes"] == num_votes:
                name_str = "Candidate ({}) - {}".format(record, data_list[record]["name"])
                new_ordered_list.update({name_str: data_list[record]["votes"]})

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


candidates = {
    "A": {"name": "Mr Burns", "votes": 0},
    "B": {"name": "Skeletor", "votes": 0},
    "C": {"name": "Hannibal Lector", "votes": 0},
    "D": {"name": "Gozer the Gozerian", "votes": 0},
    "E": {"name": "Ming the Merciless", "votes": 0}
}

vote = ""
while vote != "1":
    show_candidates()
    vote = capture_vote()




