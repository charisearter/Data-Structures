"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


# class Node:  # initial node has no value and no next
#     def __init__(self, value=None):  # constructor takes 2 elements
#         self.value = value  # default is none and this is where value is stored
#         self.next = None  # default next is = to none


# class Queue:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         node = Node(value)  # new node from value passed in
#         if self.head == None:  # if there is a nothing in the queue
#             self.head = node  # head equals the new node (end of line)
#             # tail equals new node (starting point head and tail are same)
#             self.tail = node
#         else:
#             self.tail.next = node  # move to next , will be new node
#             self.tail = node  # new node is the tail
#         return self.storage.append(node)

#     def dequeue(self):
#         if self.head == None:  # head is None
#             return None  # return None
#         temp = self.head  # current head
#         if self.head == self.tail:  # if head and tail are the same
#             self.tail = None  # tail is none
#         self.head = self.head.next  # updated to be next item
#         self.storage.pop()  # decrement by 1
#         return temp.value  # return temp node value

# Singly linked list
print('Answer: ', 111 % 7 )

class Node:  # initial node has no data and no next
    def __init__(self, value, next_node=None):  # constructor takes 2 elements
        self.value = value  # default is noe and this is where data is stored
        self.next_node = next_node  # default next is = to none

    def get_next(self):  # return next node
        return self.next_node

    def get_value(self):  # return value of node
        return self.value

    def set_next(self, new_next):  # set next node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_tail(self):
        if self.head == None:
            return None

        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val

        else:
            val = self.tail.get_value()
            current = self.head
            while current.get_next() != self.tail:
                current = current.get_next()
            self.tail = current
            self.tail.set_next(None)
            return val

    def remove_head(self):
        if self.head is None:
            return None

        if self.head is self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val

        else:
            val = self.head.get_value()
            self.head = self.head.get_next()
            return val

# Queue version 2


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:  # nothing there
            return None  # return None
        value = self.storage.head.value  # variable for temp head
        self.storage.remove_head()  # remove the head
        self.size -= 1  # decrease by 1
        return value  # give value of new head
