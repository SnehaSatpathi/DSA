class stack:
    def __init__(self):
        self.stack = []
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if self.is_empty():
            return "stack is empty"
        return self.stack.pop()
    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self.stack[-1]
    def is_empty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)

s =stack()

s.push(10)
s.push(20)
s.push(30)

print(s.peek())
print(s.pop())
print(s.size())
