# PROJECT: (WK-10) Rate a restaurant
# Solution written by Darren Halpin


def update_ratings(rating):

    if rating < 1 or rating > 5:
        print("ERROR (Out of range): Requires a number (1-5).\n")

    else:
        match rating:
            case 1:
                ratings["1"] += 1
            case 2:
                ratings["2"] += 1
            case 3:
                ratings["3"] += 1
            case 4:
                ratings["4"] += 1
            case 5:
                ratings["5"] += 1

        print("Thanks for your rating!\n")


def show_ratings(rating_list):

    print("{:<7} | {:<17}".format("Rating", "Number of ratings"))
    print("-" * 27)

    for key, value in rating_list.items():
        print("{:<1}{:<6} | {:<3} ratings".format(key, "*", value))


def get_average_rating(rating_list):

    total_ratings = rating_list["1"] + rating_list["2"] + rating_list["3"] + rating_list["4"] + rating_list["5"]

    # GENERATE AVERAGE RATING
    multi_1 = rating_list["1"] * 1
    multi_2 = rating_list["2"] * 2
    multi_3 = rating_list["3"] * 3
    multi_4 = rating_list["4"] * 4
    multi_5 = rating_list["5"] * 5

    multi_total = multi_1 + multi_2 + multi_3 + multi_4 + multi_5

    try:
        avg_rating = multi_total / total_ratings
        return_vals = ["The average rating is: ", avg_rating]
    except ZeroDivisionError:
        avg_rating = 0
        return_vals = ["No ratings have been submitted\nAverage rating is: ", avg_rating]

    return return_vals


# MAIN CODE EXECUTION:

ratings = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0}

input_rating = 0

print("\nPLEASE RATE OUR RESTAURANT")
print("-" * 26)

while input_rating != -1:
    try:
        print("RATING: Poor (1) - (5) Very good. (-1) to quit.")
        input_rating = int(input("Please enter your rating (1-5)> "))
        update_ratings(input_rating)
        # print(ratings)

    except ValueError:
        print("ERROR (Not a number): Requires a number (1-5).\n")

show_ratings(ratings)
average_rating = get_average_rating(ratings)
print("\n{} {:.1f}".format(average_rating[0], average_rating[1]))
