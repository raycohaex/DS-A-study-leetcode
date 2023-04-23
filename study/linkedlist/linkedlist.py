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

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index): # _ replaces "unused" variable
            temp = temp.next
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after



linked_list = LinkedList(5)
linked_list.append(10)
linked_list.append(15)
linked_list.append(20)
linked_list.append(13)

linked_list.print_list()

print('---')

linked_list.set_value(1, 99)
linked_list.insert(2, 105)
linked_list.pop_first()

linked_list.print_list()

print('---')

linked_list.remove(1)

linked_list.print_list()

print('---')

linked_list.reverse()
linked_list.print_list()