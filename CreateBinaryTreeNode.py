class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


# PreOrder
def preorder(root):
    if root is None:
        return
    print(root.data, end = " ")
    preorder(root.left)
    preorder(root.right)
preorder(root) # 1 2 4 5 3


# Inorder
def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)
inorder(root) # 4 2 5 1 3


#Postorder
def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end = " ")
postorder(root) # 4 5 2 3 1


# Height of Binary Tree
def height(root):

    if root is None:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    return 1 + max(left_height, right_height)


print(height(root))


# Count Nodes
def count_nodes(root):

    if root is None:
        return 0

    return (
        1
        + count_nodes(root.left)
        + count_nodes(root.right)
    )

print(count_nodes(root))



# Search in Binary Tree

def search(root, value):
    if root is None:
        return False
    if root.data == value:
        return True
    return (
        search(root.left, value)
        or search(root.right, value)
    )
print(search(root, 5))



# Level Order Traversal

from collections import deque
def level_order(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
level_order(root)


# maximum value in binary tree
def maximum(root):
    if root is None:
        return float("-inf")
    left = maximum(root.left)
    right = maximum(root.right)
    return max(root.data, left, right)
print(maximum(root))



# minimum value in Binary Tree

def minimum(root):
    if root is None:
        return float("inf")
    left = minimum(root.left)
    right = minimum(root.right)
    return min(root.data, left, right)
print(minimum(root))



