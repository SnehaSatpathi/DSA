from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self,data):
        self.queue.append(data)

    def deque(self):
        if not self.queue:
            return "Queue is empty"
        return self.queue.popleft()

    def peek(self):
        if not self.queue:
            return "Queue is empty"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue)==0

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.peek()) # 10
print(q.deque()) # 10