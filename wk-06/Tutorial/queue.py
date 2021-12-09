from collections import deque

# using deque is more efficient (speedwise) than just using list

queue = deque([1, 2, 3])
print(queue)

print("Adding 4 to the back of the queue")
queue.append(4)
print("Adding 5 to the back of the queue")
queue.append(5)

print(queue)

print("Removing", queue.popleft(), "from the front of the queue") if queue else False
print("Removing", queue.popleft(), "from the front of the queue") if queue else False

print(queue)

