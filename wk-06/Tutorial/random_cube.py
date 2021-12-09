import string
import random
import hashlib


def id_generator(size=32, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

# code_cube = [[[id_generator() for x in range(1, 9)] for y in range(1, 9)] for z in range(1, 9)]


code_cube = [[[id_generator() for x in range(1, 9)] for y in range(1, 9)] for z in range(1, 9)]


print(code_cube)
coords = [random.randint(0, 7) for a in range(0, 3)]
print(coords)
print("PASSWORD:")
print(code_cube[coords[0]][coords[1]][coords[2]])
# password = "bag0fw4nk"
# hashedPW = hashlib.md5(password.encode()).hexdigest()
# print(hashedPW)




