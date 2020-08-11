

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current.next != None:
            current = current.next
            current.next = new_node
