class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bst_decorator(function):

    def my_function(list):
        root = None
        for value in list:
            root = insert(root, value)
        result = function(root)
        return result

    def insert(node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = insert(node.left, value)
        elif value > node.val:
            node.right = insert(node.right, value)
        return node

    return my_function
