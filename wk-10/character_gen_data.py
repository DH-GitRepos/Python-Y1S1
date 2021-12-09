# PROJECT: (WK-10) Character Generator (Revisited)
# Solution written by Darren Halpin

import simplejson


def display_import_data(data_package):

    print("\n{:<14}{:^14}{:^14}{:^14}{:^14}{:^14}"
          .format("Class", "Strength", "Intelligence", "Wisdom", "Dexterity", "Constitution"))

    print("-" * 83)

    for key, value in data_package.items():

        print("{:<14}{:^14}{:^14}{:^14}{:^14}{:^14}".format(
                key.capitalize(),
                value["str"],
                value["int"],
                value["wis"],
                value["dex"],
                value["con"]
                ))


# MAIN CODE EXECUTION:

with open('char_classes.json') as json_in:
    min_abilities = simplejson.load(json_in)

display_import_data(min_abilities)
