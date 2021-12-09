lst = [1, 2, 3]
lst_copy = lst
lst += [4]
print("(list) Original: {} -- Copy: {}".format(lst, lst_copy))

tup = (1, 2, 3)
tup_copy = tup
tup += (4,)
print("(tuple) Original: {} -- Copy: {}".format(tup, tup_copy))

modules = {
    "SDAM": "Tue",
    "DT": "Mon",
    "WOS": "Tue",
    "NCCS": "Mon"
}

print("*" * 10)

for module in modules:
    print(module)

print("*" * 10)

for module in modules:
    print(modules[module])

print("*" * 10)

for module, day in modules.items():
    print(module, "->", day)

print("*" * 10)

# multi dimensional lists
times_table1 = [x * y for x in range(1, 6) for y in range(1, 6)]
print(times_table1)

times_table2 = [[x * y for x in range(1, 6)] for y in range(1, 6)]
print(times_table2)

times_cube = [[[x * y * z for x in range(1, 4)] for y in range(1, 4)] for z in range(1, 4)]
print(times_cube)

"""
# LIST METHODS
list.append(value)
list.extend(iterable)
list.insert(index, position)
list.remove(value)
list.pop([index])
list.clear()
list.index(value[, start[, end]])
list.count(value)
list.sort(key=None, reverse=False)
list.reverse()
"""

print("*" * 10)

stack = [1, 2, 3]

print("Pushing 4 to the top of the stack")
stack.append(4)

print("Pushing 5 to the top of the stack")
stack.append(5)

print(stack)

if len(stack) > 0:
    print("Popping", stack.pop(), "from the top of the stack")

print(stack)
