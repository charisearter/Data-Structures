

class Node:  # initial node has no data and no next
    def __init__(self, data=None):  # constructor takes 2 elements
        self.data = data  # default is noe and this is where data is stored
        self.next = None  # default next is = to none


class Linked_List:  # data structure that wraps over node subclass
    def __init__(self):
        self.head = Node()  # placeholder that points to the first element in the list (the head)
        self.tail = None  # no tail in the beginning

    def append(self, data):  # add to the end of the list
        # pass in data point for new_node with Node class
        new_node = Node(data)
        current = self.head  # variable for current node
        while current.next != None:  # while current next does not = none
            current = current.next  # go to next in list
            # when at the end, set current to new node (add new node)
            current.next = new_node

    def length(self):  # givve the length of the list
        current = self.head  # variable for current node
        total = 0  # variable to hold the amount of nodes starting at 0
        while current.next != None:  # each node that next does not = none
            total += 1  # add +1
            current = current.next  # go down line until current.next = None
        return total  # return the total

    def display(self):  # displays the lists so I can check it
        elems = []  # empty list variable for elements
        current_node = self.head  # variable for current head node
        while current_node.next != None:  # while current node next doesn't = none
            current_node = current_node.next  # do down the list
            # add each node to the list until current node next == None
            elems.append(current_node.data)
        print(elems)  # print all elements in the list

