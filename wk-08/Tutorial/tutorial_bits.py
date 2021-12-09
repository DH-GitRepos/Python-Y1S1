# len() function
# - returns the length of a sequence or collection
print("len() function")
print("-" * 16)

todo = ['Open editor', 'Write code', 'Run program']

for item in range(len(todo)):
    print("{}. {}".format(item + 1, todo[item]))

print("\n")

# reversed() function
# - returns a reversed iterator of a sequence
print("reversed() function")
print("-" * 21)

numbers = [1, 2, 3, 4]

for item in reversed(numbers):
    print(item)

print("\n")

# sorted() function
# returns a new sorted list
# sorted(iterable, key=None, reverse=False)
print("sorted() function")
print("-" * 19)

def sort_by(tuple_in_months):
    return tuple_in_months[1]
    # this is a user-defined function – It takes a single argument and returns a key that will be used for sorting

months = [
    ('January', 31),
    ('February', 28),
    ('March', 31),
    ('April', 30)
]

months1 = sorted(months)
# months2 = sorted(months, key=sort_by)
months2 = sorted(months, key=lambda x: x[1])
print(months, months1, months2, sep='\n')

print("\n")

# filter() function
# filter(<function>, <iterable>)
# returns a filtered iterator
print("filter() function")
print("-" * 19)

ages = [10, 18, 21, 15, 17]

adults = filter(lambda x: x >= 18, ages)

print(list(adults))

print("\n")

# map() function
# map(function, iterable, …)
# returns an iterator with function applied to every element of one or more iterable (in parallel)
print("map() function")
print("-" * 16)

ages = [10, 18, 21, 15, 17]
last_checked = [1998, 2020, 2015, 2018, 2019]

actual_age = map(
    lambda age, year: (2020 - year) + age,
    ages,
    last_checked
)
actual_age = list(actual_age)
adults = filter(lambda x: x >= 18, actual_age)

print(actual_age)
print(list(adults))

print("\n")

# open() function
# - open a file and return a file object
# open(
#     <file>,
#     mode='r',
#     buffering=-1,
#     encoding=None,
#     errors=None,
#     newline=None,
#     closefd=True,
#     opener=None
# )
# returns an iterator with function applied to every element of one or more iterable (in parallel)
print("open() function")
print("-" * 16)

