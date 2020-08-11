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


class Node:  # initial node has no value and no next
    def __init__(self, value=None):  # constructor takes 2 elements
        self.value = value  # default is none and this is where value is stored
        self.next = None  # default next is = to none

    # def __str__(self):
    #     return f'Node data: {0.value} Next Node: {0.next}'


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        pass

    def enqueue(self, value):
        node = Node(value)  # new node from value passed in
        if self.size == 0:  # if there is a nothing in the queue
            self.head = node  # head equals the new node (end of line)
            # tail equals new node (starting point head and tail are same)
            self.tail = node
        else:
            self.tail.next = node  # move to next , will be new node
            self.tail = node  # new node is the tail
        return self.size + 1

    def dequeue(self):
        if self.head == None:  # head is None
            return None  # return None
        temp = self.head  # current head
        if self.head == self.tail:  # if head and tail are the same
            self.tail = None  # tail is none
        self.head = self.head.next  # updated to be next item
        self.size -= 1  # decrement by 1
        return temp.value  # return temp node value
