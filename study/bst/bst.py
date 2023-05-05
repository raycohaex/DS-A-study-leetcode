class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class binarysearchtree:
    def __init__(self, value):
        new_node = Node(value)
        self.root = new_node
        self.length = 1