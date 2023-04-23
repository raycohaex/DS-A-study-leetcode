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

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        # traverse the linkedlist, make sure temp always moves 1 up front
        while(temp.next): 
            pre = temp
            temp = temp.next
        # set new tail, which is second last, unset previous tail.
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        # if the linkedlist is now empty, there's no head or tail
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def pop_first(self):
        if self.length == 0:
            return  None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
        



linked_list = LinkedList(5)
linked_list.append(10)
linked_list.append(15)
linked_list.append(20)
linked_list.append(13)

linked_list.print_list()

print('---')

linked_list.pop_first()

linked_list.print_list()