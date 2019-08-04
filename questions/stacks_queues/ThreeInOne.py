"""
How can you use a single array to implement three stacks.

Note: Many solutions exist. This implementation uses a resizeable multi-stack with resizeable partitions
todo: finish pop() operation and tests
@author a.k
"""
NUM_STACKS = 3


class MultiStack:
    def __init__(self):
        self.stack = [None] * NUM_STACKS
        self.i = 0  # pointer i for first partition
        self.j = 0  # pointer j for second partition
        self.k = 0  # pointer k for third partition

        self.size = 0  # total used up by all partitions
        self.i_size = 0  # total used up in partition i
        self.j_size = 0
        self.k_size = 0

        self.i_capacity = 1  # max capacity for partition i
        self.j_capacity = 1
        self.k_capacity = 1

    def push(self, stack_id: int, item):
        if stack_id == 1:
            if self.i_size == self.i_capacity:
                self.grow(2 * self.size)
            self.stack[self.i] = item
            self.i += 1
            self.i_size += 1
        if stack_id == 2:
            if self.j_size == self.j_capacity:
                self.grow(2 * self.size)
            self.stack[self.j] = item
            self.j += 1
            self.j_size += 1
        if stack_id == 3:
            if self.k_size == self.k_capacity:
                self.grow(2 * self.size)
            self.stack[self.k] = item
            self.k += 1
            self.k_size += 1
        self.size += 1

    def grow(self, capacity: float):
        temp = [None] * int(capacity)
        for i in range(self.size):
            temp[i] = self.stack[i]

        self.stack = temp  # Re-point to the newly created temp array
        self.i_capacity *= 2
        self.j_capacity *= 2
        self.k_capacity *= 2
