with open('message.txt', 'w') as f:
    f.write("Hello World")

try:
    with open('message.txt', 'r') as f:
        contents = f.read(5)
except FileNotFoundError:
    print("File doesn't exist")
else:
    print(contents)


try:
    with open('message.txt', 'r') as f:
        contents = f.readline()
        while contents != '':
            print("Contents length: ", len(contents), end=": ")
            print(contents)
            contents = f.readline()

except FileNotFoundError:
    print("File doesn't exist")

else:
    print(contents)


try:
    with open('message.txt', 'r') as f:
        contents = f.readlines()
except FileNotFoundError:
    print("File doesn't exist")
else:
    print(contents)
