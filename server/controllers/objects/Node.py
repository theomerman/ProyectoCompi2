class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

def traverse(node):
    if node is not None:
        traverse(node.left)
        traverse(node.right)
        print(node.value, end=" ")
