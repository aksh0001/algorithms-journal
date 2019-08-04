"""
How would you design a stack which, in addition to the normal stack operations, also has a min() method
that returns the minimum element?

Approach: Keep another stack that tracks the minimum element

@author a.k
"""
from data_structures.Stack import Stack
import random


class StackWithMin(Stack):
    def __init__(self):
        super(StackWithMin, self).__init__()
        self.s2 = Stack()  # This stack stores the minimum element; the top of the stack contains the minimum

    def push(self, item):
        # This time, when pushing, we check to see if the item being pushed is less than our current min
        # If so, we add this item to the top of our stack
        if item < self.get_min():
            self.s2.push(item)
        super().push(item)

    def pop(self):
        ret_val = super().pop()
        # This time, when popping, if the item we are popping is the minimum, reflect this in our second stack, s2
        if ret_val == self.get_min():
            self.s2.pop()
        return ret_val

    def get_min(self):
        """
        Returns the minimum element in the original stack, which is stored at the top of s2.
        :Time: O(1)
        :Space: O(1)
        :return: the minimum element in the stack
        """
        if self.s2.is_empty():
            return float('+inf')
        else:
            return self.s2.peek()


if __name__ == '__main__':
    print('Testing...')
    stack = StackWithMin()
    test_1 = [4, 5, 1, 19, -4, 9, -3, 6, 1]
    for i in test_1:
        stack.push(i)
    assert stack.get_min() == -4, 'Error!'
    stack.push(-15)
    assert stack.get_min() == -15, 'Error!'
    for i in range(6):
        stack.pop()
    assert stack.get_min() == 1, 'Error!'
    print('Basic Test Cases PASSED!')
