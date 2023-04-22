class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head # start at the head
        while temp is not None: # while we have not reached the end of the list
            print(temp.value)
            temp = temp.next # move to the next node

    def append(self, value):
        new_node = Node(value)
        if self.head is None: # if the list is empty, create new
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node # point the current tail to the new node
            self.tail = new_node # update the tail to be the new node
        self.length += 1


linked_list = LinkedList(5)
linked_list.append(10)
linked_list.append(15)
linked_list.append(20)
linked_list.append(13)

linked_list.print_list()