"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_next(self):  # get next node
        return self.next

    def get_prev(self):  # get Previous node
        return self.prev

    def set_next(self, new_next):  # set next node
        self.next = new_next

    def set_prev(self, new_prev):  # set new prev
        self.prev = new_prev

    def get_value(self):  # return value
        return self.value


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):  # node ste to None by default
        self.head = node  # set to None by default node
        self.tail = node  # set to None by default node
        # length is 0 unless there is a node then whatever length
        self.length = 1 if node is not None else 0

    def __len__(self):  # give length of list
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):  # add to beginning (unshift)
        new_node = ListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.set_prev(new_node)
            new_node.set_next(self.head)
            self.head = new_node
        self.length += 1
        return new_node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):  # remove from beginning (shift)
        if self.length == 0:  # if length is 0
            return None  # return nothing
        old_head = self.head  # old head  = current head
        if self.length == 1:  # if length is 1
            self.head = None  # set head to None
            self.tail = None  # set tail to None
        else:  # otherwise
            self.head = old_head.next  # new head is old head.next
            self.head.prev = None  # set new head previous to None
            old_head.next = None  # set old head next to None
        self.length -= 1  # -1 from length
        return old_head  # return the old head

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):  # end to end
        new_node = ListNode(value)  # variable for new node
        if self.length == 0:  # if length is 0
            self.head = new_node  # set head to new node
            self.tail = new_node  # set tail to new node
        else:  # otherwise
            self.tail.set_next(new_node)  # set current tail.next to new node
            new_node.prev = self.tail  # set new tail previous to old tail
            self.tail = new_node  # the new tail is new node
        self.length += 1  # add 1 to length
        return new_node  # return the value of new node
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):  # remove from end
        if self.length == 0:  # if length is 0
            return None  # return None
        poppedNode = self.tail  # popped node variable is the tail
        if self.length == 1:  # if length is 1
            self.head = None  # set head to None
            self.tail = None  # set tail to None
        else:  # otherwise
            self.tail = poppedNode.prev  # new tail is the node before popped nonde
            self.tail.set_next(None)  # set new tail next to None
            poppedNode.set_prev(None)  # set popped node previous to None
        self.length -= 1  # - 1from length
        return poppedNode  # return the value of popped Node

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        pass

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        pass
