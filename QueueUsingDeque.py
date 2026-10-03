from collections import deque
queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)
print(queue) # deque([10, 20, 30])
print(queue.popleft()) # 10
print(queue) # deque([20, 30])