class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return "Stack is empty"
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.top is None:
            return "Stack is empty"
        return self.top.data


s = Stack()
s.push(10)
s.push(20)
s.push(30)

print(s.peek())
print(s.pop())
print(s.peek())
