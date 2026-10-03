from collections import deque
dq = deque()
dq.append(10)
dq.append(20)
dq.appendleft(5)
print(dq) # deque([5, 10, 20])
dq.pop()
dq.popleft()
print(dq) # deque([10])
