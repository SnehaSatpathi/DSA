# BST Insert

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root
root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 70)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 60)
root = insert(root, 80)






# BST Search

def search(root, value):
    if root is None:
        return False
    if root.data == value:
        return True
    if value < root.data:
        return search(root.left, value)
    return search(root.right, value)
print(search(root, 60))




# BST Minimum
def find_min(root):
    current = root
    while current.left:
        current = current.left
    return current



# BST maximum
def find_max(root):
    current = root
    while current.right:
        current = current.right
    return current



# BST Delete

def delete(root,value):
    if root is None:
        return None
    if value < root.data:
        root.left = delete(root.left,value)
    elif value > root.data:
        root.right = delete(root.right,value)
    else:
        # No Child
        if root.left is None and root.right is None:
            return None
        # Only right child
        if root.left is None:
            return root.right
        # Only left child
        if root.right is None:
            return root.left
        # Two Children
        successor = find_min(root.right)
        root.data = successor.data
        root.right = delete(root.right,successor.data)
    return root




# check if Binary Tree is BST
def is_bst(root,minimum = float("-inf"), maximum = float("inf")):
    if root is None:
        return True
    if root.data <= minimum or root.data >= maximum:
        return False
    return(
        is_bst(root.left,minimum,root.data)
        and
        is_bst(root.right,root.data,maximum)
    )



# Lowest Common Ancestor in BST
def LCA(root,n1,n2):
    while root:
        if n1 < root.data and n2 < root.data:
            root = root.left
        elif n1 < root.data and n2 > root.data:
            root = root.right
        else:
            return root
    return None



# Tree Diameter
def diameter(root):
    result = [0]
    def height(node):
        if node is None:
            return 0
        left = height(node.left)
        right = height(node.right)
        result[0] = max(result[0], left + right )
        return 1 + max(left,right)
    height(root)
    return result[0]
print(diameter(root))




# Mirror a Binary Tree
def mirror(root):
    if root is None:
        return None
    root.left,root.right = root.right,root.left
    mirror(root.left)
    mirror(root.right)
    return root


# Iterative inorder traversal
def inorder_iterative(root):
    stack = []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current.data,end = " ")
        current = current.right


# Iterative Preorder
def preorder_iterative(root):
    if root is None:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.data,end = " ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)



# Iterative Postoder
def postorder_iterative(root):
    if root is None:
        return
    stack1 = [root]
    stack2 = []
    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)

        if node.right:
            stack1.append(node.right)

    while stack2:
        print(stack2.pop().data,end = " ")

