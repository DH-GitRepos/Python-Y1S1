stack = [1, 2, 3]

print("Pushing 4 to the top of the stack")
stack.append(4)

print("Pushing 5 to the top of the stack")
stack.append(5)

print(stack)

if len(stack) > 0:
    print("Popping", stack.pop(), "from the top of the stack")

print(stack)
