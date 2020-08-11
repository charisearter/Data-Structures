"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


class Node:  # initial node has no value and no next
    def __init__(self, value=None):  # constructor takes 2 elements
        self.value = value  # default is none and this is where value is stored
        self.next = None  # default next is = to none


class Stack:
    def __init__(self):
        self.head = None  # beginning no head
        self.tail = None  # beginning no tail
        self.storage = []  # initial value for size

    def __len__(self):  # return length of storage
        return len(self.storage)

    def push(self, value):  # add / accepts value
        new_node = Node(value)  # new node variable
        if self.head == None:  # if head == none or no head / empty
            self.head = new_node  # new node is now head
            self.tail = new_node  # new node is tail too
        else:
            temp = self.head  # temp variable for head
            # new_node is now the head (added to top of stack)
            self.head = new_node
            self.head.next = temp  # next node after new head is the old head
        return self.storage.append(new_node)  # add to storage

    def pop(self):
        if self.head == None:  # if stack is empty return None
            return None
        temp = self.head  # temp variable for head
        if self.head == self.tail:  # if only one node
            self.tail == None  # tail is None
        self.head = self.head.next  # sets head to None as well
        self.storage.pop()   # subtract 1 from storage
        return temp.value  # return value
