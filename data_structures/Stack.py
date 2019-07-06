"""
This module implements a stack

@author a.k
"""


class Stack():
    def __init__(self):
        self.stack = [None] * 2  # start off with two elements
        self.size = 0  # current size of the occupied stack (points to the next empty position at top of stack)

    def push(self, item):
        """
        Add an item onto the top of stack
        :param item: item to add
        :return: none
        :Time: O(1)
        :Space: O(1)
        """
        if self.size == len(self.stack):  # Double max capacity if stack is full
            self.resize(2 * len(self.stack))

        self.stack[self.size] = item
        self.size += 1  # Increment $sp--it points to the next unoccupied position

    def pop(self):
        """
        Returns the element at the top of the stack
        :return: element at the top of the stack
        :Time: O(1)
        :Space: O(1)
        """
        if self.is_empty():
            raise Exception("Stack is Empty!")

        ret_val = self.stack[self.size - 1]
        self.stack[self.size - 1] = None  # Prevent loitering (unused space)
        self.size -= 1
        if self.size > 0 and self.size == len(self.stack) // 4:  # Half max cap if popping results in 1/4 full stack
            self.resize(len(self.stack) // 2)

        return ret_val

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is Empty!")
        return self.stack[self.size - 1]

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def resize(self, capacity: float):
        temp = [None] * int(capacity)
        for i in range(self.size):
            temp[i] = self.stack[i]

        self.stack = temp  # Re-point to the newly created temp array
