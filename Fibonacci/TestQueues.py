from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Park")
print(queue)

queue.popleft()
print(queue)

queue.popleft()
print(queue)

