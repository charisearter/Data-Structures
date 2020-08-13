"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BST:  # Binary Search Tree (BST because I ain't typing all that)
    def __init__(self):
        self.root = None

    def insert(self, value):  # insert node
        if self.root:
            return self.root.insert(value)
        else:
            self.root = BSTNode(value)
            return True

    def contains(self, target):  # find node
        if self.root:
            return self.root.contains(target)
        else:
            return False


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if the value is less than the current node's value
        if value < self.value:
            # does the current node have a left child?
            if self.left:
                self.left.insert(value)
            # otherwise, it doesn't have a left child
            # we can park the new node here
            else:
                self.left = BSTNode(value)
        # otherwise the value is greater or equal to the current node's value
        else:
            # does the current node have a right child?
            if self.right:
                # if it does, call the right child's `insert` method to repeat the process
                self.right.insert(value)
            # otherwise, it doesn't have a right child
            # we can park the new node here
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):  # check to see if target matches node
        if self.value == target:  # if node is == target, stop and return true
            return True
        # if node is > than target (target is less than node)
        elif self.value > target:
            if self.left:  # if left child node exists go left
                return self.left.contains(target)  # repeat steps again
            else:  # otherwise
                return False  # if no left child node stop and return False
        else:  # otherwise
            # if node is < than target (target is greater than node) and has right child node
            if self.right:
                # repeat steps after going to right child node
                return self.right.contains(target)
            else:  # if no right child node
                return False

    # Return the maximum value found in the tree

    def get_max(self):  # largest number / largest number is always on the right
        current = self  # self is the node  (self.value would be wrong)
        while current.right != None:  # if has right node go there
            current = current.right
        return current.value  # return the final right nodes value

    # Call the function `fn` on the value of each node
    # This method doesn't return anything

    def for_each(self, fn):  # call function on each node / recursion (call on itself)
        fn(self.value)  # call function on self.value
        if self.left:  # if left node, call this method for_each with fn argument
            self.left.for_each(fn)
        if self.right:  # if right node, call this method for_each on with fn argument
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint: Use a recursive, depth first traversal

    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal (DFT)
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT (specific type of DFT)
    def pre_order_print(self):
        pass

    # Print Post-order recursive DFT (another type of DFT)
    def post_order_print(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_print()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_print()
