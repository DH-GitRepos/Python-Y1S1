# PROJECT: (WK-04) A Night at the Theatre
# Solution written by Darren Halpin

import datetime

# DEFINE CONSTANTS
TICKET_ADULT = 10.5
TICKET_CHILD = 7.3
TICKET_CONCESSION = 8.4
TICKET_POSTAGE = 2.34

# DEFINE FUNCTION


# FUNCTION: check_ten_percent(bill_amount)
# Determines whether to apply final 10% discount based on bill amount.
# Accepts 'bill_amount' float value - bill amount after group discounts.
# Returns list 'final_bill', [discount applied check digit, discount amount, new bill amount]
def check_ten_percent(bill_amount):

    if bill_amount > 100:

        discount_ten = (bill_amount / 100) * 10
        new_bill = bill_amount - discount_ten

        final_bill = [True, discount_ten, new_bill]

        return final_bill

    else:

        final_bill = [False, 0, bill_amount]

        return final_bill


# GET USER INPUT
party_total = int(input("Total number in party: "))
input_adults = int(input("Total adults in party: "))
input_concessions = int(input("Number of concessions (over 65's): "))
postage_required = input("Do you want to collect your tickets in person (y/n): ")

qty_children = int(party_total - input_adults)

# CHECK CONCESSIONS DON'T EXCEED TOTAL ADULTS
if input_concessions > input_adults:
    print("\nERROR: Please specify how many of the adults in the party are concessions.")
    print("- the number of concessions cannot be higher than the total number of adults.")
    exit()

# CHECK CHILDREN ARE ACCOMPANIED BY AN ADULT
if qty_children > 0 and input_adults < 1:
    print("All children must be accompanied by at least one adult, please add adults to the party.")
    exit()

# OUTPUT RECEIPT HEADER
print(" " * 40)
print("{0:^40}".format("PYTHON THEATRE"))
print("{0:^40}".format("5 Theatre Street"))
print("{0:^40}".format("S-O-T, ST1 1AP"))
print("{0:^40}".format("BOOKING REF: Z-01234"))
print(" " * 40)
print("-" * 40)

# CALCULATE TICKETS AT FULL COST

cost_children = qty_children * TICKET_CHILD
qty_full_price_adults = int(input_adults - input_concessions)
cost_adults = float(qty_full_price_adults * TICKET_ADULT)
qty_concessions = int(input_concessions)

# OUTPUT FULL PRICE COST INFO
print(
    "{0:>3} {1:<21}|{2:^3}{3:>10.2f}"
    .format(qty_children, "Children", "£", cost_children)
)
print(
    "{0:>3} {1:<5}{2:<16.2f}|{3:^3}{4:>10}"
    .format(" ", "- @ £", TICKET_CHILD, " ", " ")
)

print(
    "{0:>3} {1:<21}|{2:^3}{3:>10.2f}"
    .format(qty_full_price_adults, "Adult-Full Price", "£", cost_adults)
)

print(
    "{0:>3} {1:<5}{2:<16.2f}|{3:^3}{4:>10}"
    .format(" ", "- @ £", TICKET_ADULT, " ", " ")
)

# CALCULATE AND OUTPUT CONCESSIONS
cost_concessions = float(input_concessions * TICKET_CONCESSION)
if input_concessions > 0:

    print(
        "{0:>3} {1:<21}|{2:^3}{3:>10.2f}"
        .format(qty_concessions, "Concession-Over 65", "£", cost_concessions)
    )

    print(
        "{0:>3} {1:<5}{2:<16.2f}|{3:^3}{4:>10}"
        .format(" ", "- @ £", TICKET_CONCESSION, " ", " ")
    )

# CALCULATE AND OUTPUT PRE DISCOUNT SUB TOTAL
total_cost_pre_disc = cost_children + cost_adults + cost_concessions

print("-" * 40)
print(
    "{0:>3} {1:<21}|{2:^3}{3:>10.2f}"
    .format(" ", "sub total", "£", total_cost_pre_disc)
)
print("-" * 40)

# CALCULATE CONCESSION DISCOUNT DETAILS
free_adult_places = qty_children // 10

# APPLY GROUP DISCOUNT
# if no group discount to apply
if free_adult_places == 0:

    discount_total = 0
    total_sub = total_cost_pre_disc - discount_total
    total_after_free_places = total_sub

else:

    # apply adult discounts to non-concession places only
    if free_adult_places > 0 and input_concessions == 0:

        if free_adult_places <= qty_full_price_adults:
            places_discounted = free_adult_places

        else:
            places_discounted = qty_full_price_adults

        discount_cost_full_price = places_discounted * TICKET_ADULT
        total_after_free_places = total_cost_pre_disc - discount_cost_full_price

        # output adult discount
        adult_disc_display = discount_cost_full_price - (discount_cost_full_price * 2)
        print(
            "{0:>3} {1:<21}|{2:^3}{3:>10.2f}"
            .format(places_discounted, "Adult discount", "£", adult_disc_display)
        )
        print(
            "{0:>3} {1:<5}{2:<16.2f}|{3:^3}{4:>10}"
            .format(" ", "- @ £", TICKET_ADULT, " ", " ")
        )

    # if number of free adult tickets is greater than qty of full price adults, apply remaining
    # adult discounts to concession places (they are also adults)
    elif free_adult_places > 0 and input_concessions > 0:

        if free_adult_places <= qty_full_price_adults:
            places_discounted = free_adult_places

        else:
            places_discounted = qty_full_price_adults

        discount_cost_full_price = places_discounted * TICKET_ADULT
        total_free_place_discounts = discount_cost_full_price
        total_after_free_places = total_cost_pre_disc - total_free_place_discounts

        # output adult discount
        adult_disc_display = discount_cost_full_price - (discount_cost_full_price * 2)
        print(
            "{0:>3} {1:<21}|{2:^3}{3:>10.2f}"
            .format(places_discounted, "Adult discount", "£", adult_disc_display)
        )
        print(
            "{0:>3} {1:<5}{2:<16.2f}|{3:^3}{4:>10}"
            .format(" ", "- @ £", TICKET_ADULT, " ", " ")
        )

        if places_discounted < free_adult_places and input_concessions > 0:
            remaining_discount_places = input_adults - places_discounted

            if remaining_discount_places >= input_concessions:
                discount_cost_concession = remaining_discount_places * TICKET_CONCESSION
                total_free_place_discounts = discount_cost_full_price + discount_cost_concession
                total_after_free_places = total_cost_pre_disc - total_free_place_discounts

                # output concession discount
                conc_disc_display = discount_cost_concession - (discount_cost_concession * 2)
                print(
                    "{0:>3} {1:<21}|{2:^3}{3:>10.2f}"
                    .format(input_concessions, "Concession discount", "£", conc_disc_display)
                )
                print(
                    "{0:>3} {1:<5}{2:<16.2f}|{3:^3}{4:>10}"
                    .format(" ", "- @ £", TICKET_CONCESSION, " ", " ")
                )

            else:
                discount_cost_concession = 0
                total_free_place_discounts = discount_cost_full_price + discount_cost_concession
                total_after_free_places = total_cost_pre_disc - total_free_place_discounts

# CHECK TOTAL FOR 10% DISCOUNT AVAILABILITY

last_discount = check_ten_percent(total_after_free_places)

if last_discount[0]:
    display_ten_disc = last_discount[1] - (last_discount[1] * 2)
    print(
        "{0:>3} {1:<21}|{2:^3}{3:>10.2f}"
            .format("1", "10% discount", "£", display_ten_disc)
    )
    print(
        "{0:>3} {1:<5}{2:<16.2f}|{3:^3}{4:>10}"
            .format(" ", "- @ £", last_discount[1], " ", " ")
    )

    final_bill = last_discount[2]
else:
    final_bill = last_discount[2]

# print("-" * 40)

# ADD POSTAGE ON TO BILL IF REQUIRED
if postage_required.casefold() == "n":
    postage_added = TICKET_POSTAGE

    print(
        "{0:>3} {1:<21}|{2:^3}{3:>10.2f}"
        .format("1", "Postage & packaging", "£", postage_added)
    )
    print(
        "{0:>3} {1:<5}{2:<16.2f}|{3:^3}{4:>10}"
        .format(" ", "- @ £", postage_added, " ", " ")
    )
else:
    postage_added = 0

print("-" * 40)

final_total = last_discount[2] + postage_added

print(
    "{0:>3} {1:<21}|{2:^3}{3:>10.2f}"
    .format(" ", "TOTAL", "£", final_total)
)
print("-" * 40)

# OUTPUT RECEIPT FOOTER
print(" " * 40)
dateval_day = datetime.date.today().day
dateval_month = datetime.date.today().month
dateval_year = datetime.date.today().year
date_str = "DATE: " + str(dateval_day) + "/" + str(dateval_month) + "/" + str(dateval_year)
print("{0:^40}".format(date_str))
