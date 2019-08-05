"""
Implement an optimal way to design a queue using two stacks

Approach: When enqueueing, push onto s1. When dequeueing, pop from s1 and push onto s2, then pop and return from s2.
Optimization: Repeated bursts of dequeue operations will unnecessarily update s2. Therefore, we can let the elements
              in s2 "sit" until we absolutely must update it -- this occurs when s2 is empty.

@author a.k
"""
from data_structures.Stack import Stack
from data_structures.Queue import Queue


class MyQueue(Queue):
    def __init__(self):
        super(MyQueue, self).__init__()
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, item):
        """
        Enqueues an item onto the queue by pushing the item onto stack 1.
        :param item: item to enqueue
        :Time: O(1)
        :Space: O(1)
        :return: none
        """
        self.s1.push(item)  # Simply push item onto s1

    def dequeue(self):
        """
        Returns the element at the front of the queue. This is achieved by popping from s2, which mimics a queue.
        @note: To save needlessly shifting elements into s2, we will only populate s2 when it is depleted.
                I.e. only update s2 until the previously populated items have been popped.
        :Time: O(N)
        :Space: O(N)
        :return: none
        """
        if self.s2.is_empty():  # We will only update s2 when it cannot be popped() from further
            self.shift_stacks()
        return self.s2.pop()

    def peek(self):
        if self.s2.is_empty():
            self.shift_stacks()
        return self.s2.peek()

    def shift_stacks(self):
        """
        Pops each element in s1 and pushes it onto s2 such that s2 now mimics a queue which can be dequeued via popping
        :Time: O(N)
        :Space: O(N)
        :return: none
        """
        while not self.s1.is_empty():  # pop() from s1 and push() onto s2
            self.s2.push(self.s1.pop())

    def get_size(self):
        return self.s1.get_size() + self.s2.get_size()  # Size of queue is the size of both stacks

    def is_empty(self):
        return self.get_size() == 0


if __name__ == "__main__":
    print("Testing")
    q = MyQueue()
    print(q.is_empty())
    print(q.get_size())
    for i in range(-10, 5):
        q.enqueue(i)
    while not q.is_empty():
        print(q.dequeue(), end=" ")
    print("")
    for i in range(10, 50, 10):  # Enqueue again
        q.enqueue(i)
    while not q.is_empty():
        print(q.dequeue(), end=" ")
    print("")
