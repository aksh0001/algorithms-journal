"""
This module implements a queue

@author a.k
"""


class Queue:
    def __init__(self):
        self.queue = [None] * 2  # start off with two elements
        self.first = 0  # points to the start of queue
        self.last = 0  # points to the end of the queue
        self.size = 0

    def enqueue(self, item):
        """
        Adds an item to the end of the queue.
        :param item: item to add
        :Time: O(1)
        :Space: O(1)
        :return: none
        """
        if self.size == len(self.queue):  # Double max capacity if queue becomes full
            self.resize(2 * len(self.queue))
        self.queue[self.last] = item
        self.last += 1
        if self.last == len(self.queue):
            self.last = 0  # wrap around
        self.size += 1

    def dequeue(self):
        """
        Removes and returns the item at the front of the queue
        :Time: O(1)
        :Space: O(1)
        :return: item at the front
        """
        if self.is_empty():
            raise Exception("Queue is Empty!!")
        ret_val = self.queue[self.first]
        self.queue[self.first] = None  # Prevent loitering
        self.first += 1
        self.size -= 1
        if self.first == len(self.queue):
            self.first = 0  # wrap around
        if self.size > 0 and self.size == len(self.queue) // 4:  # Half max cap if dequeue results in 1/4 full queue
            self.resize(len(self.queue) // 2)
        return ret_val

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty!!")
        return self.queue[self.first]

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def resize(self, capacity: float):
        temp = [None] * int(capacity)
        for i in range(self.size):
            temp[i] = self.queue[(self.first + i) % len(self.queue)]

        self.queue = temp  # Re-point to the newly created temp array
        self.first = 0
        self.last = self.size


if __name__ == "__main__":
    print("Testing")
    q = Queue()
    print(q.is_empty())
    print(q.get_size())
    for i in range(-10, 5):
        q.enqueue(i)
    while not q.is_empty():
        print(q.dequeue(), end=" ")
    print("")
