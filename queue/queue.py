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


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
        self.head = None
        self.tail = None

    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        node = Node(value)

        if self.size = 0:
            self.head = node
            self.tail = node
            self.size += 1
            self.storage.append(node)
            return
        last = self.last
        last.next = node
        self.last = node
        self.length += 1

    def dequeue(self):
        if self.size == 0:
            return None
        value = self.head.valueself.head = self.head.next
        self.size -= 1
        if self.storage == 0:
            self.last = None
            return data
