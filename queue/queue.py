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


class Node:  # initial node has no data and no next
    def __init__(self, data=None):  # constructor takes 2 elements
        self.data = data  # default is none and this is where data is stored
        self.next = None  # default next is = to none

    def __str__(self):
        return f'Node data: {0.data} Next Node: {0.next}'


class Queue:
    def __init__(self):
        self.head = head
        self.tail = tail
        self.size = 0
        
    def __len__(self):
        pass
    
    def enquegue(self,value):
        pass
    
    def dequeque(self):
        pass