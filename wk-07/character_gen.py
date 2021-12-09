# PROJECT: (WK-07) Character Generator
# Solution written by Darren Halpin

# IMPORT RANDOM MODULE
import random

# DEFINE DEFAULT CHARACTER CLASS VALUES
DEFAULT_CHARACTER_CLASSES = {
    "Warrior": {"strength": 15, "intelligence": 0, "wisdom": 0, "dexterity": 12, "constitution": 10},
    "Wizard": {"strength": 0, "intelligence": 15, "wisdom": 10, "dexterity": 10, "constitution": 0},
    "Thief": {"strength": 10, "intelligence": 9, "wisdom": 0, "dexterity": 15, "constitution": 0},
    "Necromancer": {"strength": 10, "intelligence": 10, "wisdom": 15, "dexterity": 0, "constitution": 0}
    }

# DEFINE BLANK CHARACTER BUILDING LISTS
CHARACTER_BUILDER = {
    "random": {"strength": 0, "intelligence": 0, "wisdom": 0, "dexterity": 0, "constitution": 0},
    "deficit": {"strength": 0, "intelligence": 0, "wisdom": 0, "dexterity": 0, "constitution": 0},
    "surplus": {"strength": 0, "intelligence": 0, "wisdom": 0, "dexterity": 0, "constitution": 0},
    "trade": {"strength": 0, "intelligence": 0, "wisdom": 0, "dexterity": 0, "constitution": 0}
    }


# DEFINE STATS TABLE DISPLAY FUNCTION
def display_character_stats_table(class_name):

    # PRINT HEADER ROW
    print("=" * 107)
    print(
        "{0:<12}|{1:^18}|{2:^18}|{3:^18}|{4:^18}|{5:^18}"
        .format("Class", "Strength (S)", "Intelligence (I)", "Wisdom (W)", "Dexterity (D)", "Constitution (C)")
        )
    print("-" * 107)

    # PRINT DATA ROWS
    # print random base score row
    print(
        "{0:<12}|{1:^18}|{2:^18}|{3:^18}|{4:^18}|{5:^18}"
        .format(
            "Base score",
            CHARACTER_BUILDER["random"]["strength"],
            CHARACTER_BUILDER["random"]["intelligence"],
            CHARACTER_BUILDER["random"]["wisdom"],
            CHARACTER_BUILDER["random"]["dexterity"],
            CHARACTER_BUILDER["random"]["constitution"])
        )

    # print pre-defined class stats
    print(
        "{0:<12}|{1:^18}|{2:^18}|{3:^18}|{4:^18}|{5:^18}"
        .format(
            class_name,
            DEFAULT_CHARACTER_CLASSES[class_name]["strength"],
            DEFAULT_CHARACTER_CLASSES[class_name]["intelligence"],
            DEFAULT_CHARACTER_CLASSES[class_name]["wisdom"],
            DEFAULT_CHARACTER_CLASSES[class_name]["dexterity"],
            DEFAULT_CHARACTER_CLASSES[class_name]["constitution"])
        )

    print("-" * 107)

    # print deficit points row
    print(
        "{0:<12}|{1:^18}|{2:^18}|{3:^18}|{4:^18}|{5:^18}"
        .format(
            "Deficit",
            CHARACTER_BUILDER["deficit"]["strength"],
            CHARACTER_BUILDER["deficit"]["intelligence"],
            CHARACTER_BUILDER["deficit"]["wisdom"],
            CHARACTER_BUILDER["deficit"]["dexterity"],
            CHARACTER_BUILDER["deficit"]["constitution"])
        )

    # print surplus points row
    print(
        "{0:<12}|{1:^18}|{2:^18}|{3:^18}|{4:^18}|{5:^18}"
        .format(
            "Surplus",
            CHARACTER_BUILDER["surplus"]["strength"],
            CHARACTER_BUILDER["surplus"]["intelligence"],
            CHARACTER_BUILDER["surplus"]["wisdom"],
            CHARACTER_BUILDER["surplus"]["dexterity"],
            CHARACTER_BUILDER["surplus"]["constitution"])
        )
    print("=" * 107)


def display_points_swap_table():

    print("-" * 107)

    print(
        "{0:<12}|{1:^18}|{2:^18}|{3:^18}|{4:^18}|{5:^18}"
        .format(
            "Trade pts",
            CHARACTER_BUILDER["trade"]["strength"],
            CHARACTER_BUILDER["trade"]["intelligence"],
            CHARACTER_BUILDER["trade"]["wisdom"],
            CHARACTER_BUILDER["trade"]["dexterity"],
            CHARACTER_BUILDER["trade"]["constitution"])
        )

    print("-" * 107)


# DEFINE FUNCTION TO UPDATE SURPLUS AND DEFICIT POINTS TABLES
def update_surplus_and_deficit_lists(class_in):

    # CALCULATE AND POPULATE STATS DEFICIT LIST
    for val_1 in CHARACTER_BUILDER["deficit"].keys():
        if CHARACTER_BUILDER["random"][val_1] < DEFAULT_CHARACTER_CLASSES[class_in][val_1]:
            CHARACTER_BUILDER["deficit"][val_1] = DEFAULT_CHARACTER_CLASSES[class_in][val_1] \
                - CHARACTER_BUILDER["random"][val_1]
        else:
            CHARACTER_BUILDER["deficit"][val_1] = 0

    # CALCULATE AND POPULATE STATS SURPLUS LIST
    for val_2 in CHARACTER_BUILDER["random"].keys():
        if CHARACTER_BUILDER["random"][val_2] > DEFAULT_CHARACTER_CLASSES[class_in][val_2]:
            CHARACTER_BUILDER["surplus"][val_2] = CHARACTER_BUILDER["random"][val_2] \
                - DEFAULT_CHARACTER_CLASSES[class_in][val_2]
        else:
            CHARACTER_BUILDER["surplus"][val_2] = 0


# DEFINE FUNCTION TO CHECK ENOUGH TRADE POINTS ARE SELECTED
def count_trade_points():

    current_points = 0
    for val_3 in CHARACTER_BUILDER["trade"].keys():
        current_points = current_points + CHARACTER_BUILDER["trade"][val_3]

    if current_points == 2:
        return True
    else:
        return current_points


# DEFINE FUNCTION TO RESET TRADE POINTS
def reset_trade_points():

    for val_4 in CHARACTER_BUILDER["trade"].keys():
        CHARACTER_BUILDER["trade"][val_4] = 0


# DEFINE FUNCTION TO CHECK NECESSARY MINIMUM ATTRIBUTE VALUES ARE MET
def check_minimum_class_points(class_in):

    deficit_check_pass = True

    for val_5 in DEFAULT_CHARACTER_CLASSES[class_in].keys():
        if DEFAULT_CHARACTER_CLASSES[class_in][val_5] != 0 and CHARACTER_BUILDER["deficit"][val_5] != 0:
            deficit_check_pass = False


# DEFINE FUNCTION TO MAP STAT TO LIST KEY NAME
def get_stat_name(stat_letter):

    out_stat_name = "none"

    if stat_letter.upper() == "S":
        out_stat_name = "strength"
    elif stat_letter.upper() == "I":
        out_stat_name = "intelligence"
    elif stat_letter.upper() == "W":
        out_stat_name = "wisdom"
    elif stat_letter.upper() == "D":
        out_stat_name = "dexterity"
    elif stat_letter.upper() == "C":
        out_stat_name = "constitution"

    return out_stat_name


# DEFINE FUNCTION TO REMOVE STAT POINTS FROM RANDOM ATTRIBUTES AND UPDATE TRADE ATTRIBUTES
def remove_stat_points(in_selected_stat):

    # MAP SELECTED STAT TO LIST VALUE
    stat_name = get_stat_name(in_selected_stat)

    # CALCULATE NEW RANDOM STAT VALUE
    random_attributes_list_update = CHARACTER_BUILDER["random"][stat_name] - 1
    # UPDATE RANDOM STAT VALUE
    CHARACTER_BUILDER["random"][stat_name] = random_attributes_list_update

    # CALCULATE NEW SURPLUS STAT VALUE
    surplus_attributes_list_update = CHARACTER_BUILDER["surplus"][stat_name] - 1
    # UPDATE SURPLUS ATTRIBUTES VALUE
    CHARACTER_BUILDER["surplus"][stat_name] = surplus_attributes_list_update

    # CALCULATE NEW TRADE STAT VALUE
    trade_attributes_list_update = CHARACTER_BUILDER["trade"][stat_name] + 1
    # UPDATE TRADE ATTRIBUTES VALUE
    CHARACTER_BUILDER["trade"][stat_name] = trade_attributes_list_update

    update_surplus_and_deficit_lists(current_character_class)


# DEFINE FUNCTION TO ADD STAT POINTS TO TARGET ATTRIBUTE WITH SELECTED STAT
def add_stat_points(stat_selection):

    # MAP SELECTED STAT TO LIST VALUE
    add_stat_name = get_stat_name(stat_selection)

    # CALCULATE NEW RANDOM STAT VALUE
    random_attributes_list_update = CHARACTER_BUILDER["random"][add_stat_name] + 1

    # UPDATE RANDOM STAT VALUE
    CHARACTER_BUILDER["random"][add_stat_name] = random_attributes_list_update

    update_surplus_and_deficit_lists(current_character_class)

    reset_trade_points()


# DEFINE FUNCTION TO CHECK FOR A VALID CHARACTER BUILD
def check_valid_character_build(character_class):

    valid_build = True

    for item in DEFAULT_CHARACTER_CLASSES[character_class].keys():
        if CHARACTER_BUILDER["random"][item] < DEFAULT_CHARACTER_CLASSES[character_class][item]:
            valid_build = False

    return valid_build


# ## START MAIN CODE EXECUTION ## #
# ASK USER TO SELECT CHARACTER CLASS
chosen_character_valid = False
current_character_class = "none"

while not chosen_character_valid:
    print("\nSelect your character class.")
    print("Choose from Warrior (1), Wizard (2), Thief (3), Necromancer (4)")
    character_choice = int(input("> "))

    if character_choice == 1:
        current_character_class = "Warrior"
        print("\nYou chose WARRIOR.")
        chosen_character_valid = True
    elif character_choice == 2:
        current_character_class = "Wizard"
        print("\nYou chose WIZARD.")
        chosen_character_valid = True
    elif character_choice == 3:
        current_character_class = "Thief"
        print("\nYou chose THIEF.")
        chosen_character_valid = True
    elif character_choice == 4:
        current_character_class = "Necromancer"
        print("\nYou chose NECROMANCER.")
        chosen_character_valid = True
    else:
        print("\nInvalid character selection, please try again.")
        chosen_character_valid = False

# BUILD RANDOM CHARACTER
# ROLL RANDOM CHARACTER STATS
for stat in CHARACTER_BUILDER["random"].keys():
    random_attribute = random.randint(3, 18)
    CHARACTER_BUILDER["random"][stat] = random_attribute

# UPDATE SURPLUS AND DEFICIT LISTS
update_surplus_and_deficit_lists(current_character_class)

# DISPLAY CHARACTER STATS TABLE
display_character_stats_table(current_character_class)

# START CUSTOMISE CHARACTER PROCESS
# LOOP CHARACTER BUILD PROCESS WHILE CHARACTER BUILD IS NOT VALID
while not check_valid_character_build(current_character_class):

    # CHECK IF THERE ARE ENOUGH SURPLUS POINTS TO COVER THE DEFICIT POINTS

    # GET DEFICIT TOTAL
    total_deficit = 0
    for val_6 in CHARACTER_BUILDER["deficit"].keys():
        total_deficit = total_deficit + CHARACTER_BUILDER["deficit"][val_6]

    # GET SURPLUS TOTAL
    total_surplus = 0
    for val_7 in CHARACTER_BUILDER["surplus"].keys():
        total_surplus = total_surplus + CHARACTER_BUILDER["surplus"][val_7]

    # ACCOUNT FOR 2 FOR 1 POINT TRADE
    actual_surplus = total_surplus // 2

    # CHECK DEFICIT VS SURPLUS DIFFERENCE
    # IF NOT ENOUGH POINTS THEN QUIT
    if total_deficit > actual_surplus:
        print("There are not enough spare points to meet the minimum requirements for your chosen class")
        print("Please re-run the program")
        exit()

    # IF ENOUGH POINTS PROCESS STATS UPDATE
    elif actual_surplus >= total_deficit:
        print("You have enough points to trade to meet the minimum stats for your class")
        print("You can trade 2 non-required points for 1 required stat point")

        # SELECT UPTO 2 POINTS TO RE-ALLOCATE
        while not count_trade_points():
            number_of_points_chosen = count_trade_points()
            number_of_points_to_choose = 2 - number_of_points_chosen

            print("You have {} points left to choose".format(number_of_points_to_choose))
            print("Pick a stat to remove a point from (S,I,W,D,C)")
            selected_stat = input("> ")

            remove_stat_points(selected_stat)
            print("NEW STAT POINTS:")
            display_character_stats_table(current_character_class)

            if count_trade_points() == 1:
                print("Choose another surplus point to move:")
                print("Choose stat (S,I,W,D,C)")
                selected_stat = input("> ")

                remove_stat_points(selected_stat)
                print("NEW STAT POINTS:")
                display_character_stats_table(current_character_class)

        print("You now have 1 point to allocate to another stat")
        print("Choose target stat (S,I,W,D,C)")
        selected_stat = input("> ")

        add_stat_points(selected_stat)
        print("NEW STAT POINTS:")
        display_character_stats_table(current_character_class)

print("Congratulations, your character is ready to go!")
