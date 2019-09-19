"""
This moudule implements a minheap that allows for priority assignment of items.
An item that is the same as another item but with a higher priority will be considered as smaller.
I.e.  x(y) < x(z) where x is some item, y and z are priorities where y > z.

Todo: Add stable heap implementation using secondary key (using index of element -- check FIT2085 tutes)

@author a.k
"""


class MinHeap:
    def __init__(self):
        """
        This class represents a MinHeap
        """
        self.size = 0
        self.heap = [None]  # Use 1-based indexing

    def push(self, item, priority=1):
        """
        This functions adds item into the min heap
        :param item: item to be added. In this case item will be a list with the second element used as the key
        :param priority: priority of the item which determines the removal order. Default to 1 (highest priority)
        :Time: O(log(n))
        """
        self.size += 1
        self.heap.append((item, priority))
        self.swim()

    def pop(self):
        """
        This method pops and returns the minimum element from the heap
        :return: the minimum element
        """
        if self.size > 0:
            min = self.heap[1]
            self._swap(1, self.size)
            self.size -= 1
            self.sink()
            self.heap.pop(self.size + 1)  # Prevent loitering
            return min
        raise Exception("Heap is empty!!")

    def swim(self):
        """
        This method performs the swim operation that restores heap ordering.
        :Time: O(logn)
        """
        j = self.size
        while j > 1 and (self.heap[self.parent(j)][0] > self.heap[j][0] or (  # Parent larger/its priority smaller
                (self.heap[self.parent(j)][0] == self.heap[j][0]) and self.heap[self.parent(j)][1] <
                self.heap[j][1])):  # Note: item key is second element. If equal, compare priorities
            self._swap(j, self.parent(j))
            j = self.parent(j)

    def sink(self):
        """
        This method performs the sink operation that restores heap ordering
        :Time: O(log(n))
        """
        r = 1
        while 2 * r <= self.size:
            j = 2 * r
            if j < self.size and self.heap[j + 1][0] < self.heap[j][0]:  # Note: item's key is second element
                j += 1  # If parent's right child is smaller than its left, we swap it with that
            elif j < self.size and ((self.heap[j + 1][0] == self.heap[j][0]) and self.heap[j + 1][1] > self.heap[j][1]):
                j += 1  # If elements are equal, compare priorities (a larger priority value means relatively smaller)

            if self.heap[r][0] < self.heap[j][0] or (
                    (self.heap[r][0] == self.heap[j][0]) and self.heap[r][1] > self.heap[j][1]):
                break
            self._swap(r, j)
            r = j

    def get_size(self):
        """
        This method returns the size of the minheap
        :return: the size of the minheap
        """
        return self.size

    def peek(self):
        """
        This method returns the minimum of the heap
        :return: the root of the heap (min)
        """
        return self.heap[1]

    def _swap(self, i, j):
        """
        This functions swaps the nodes i and j
        :param i: node i to be swapped
        :param j: node j to be swapped
        """
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def parent(self, i):
        """
        This function returns the parent of node i
        :param i: the node to which to get the parent ti
        :return: index of parent of node i
        """
        return i // 2


if __name__ == '__main__':
    print('Testing...')
    mh1 = MinHeap()
    for i in range(10, 4, -1):
        mh1.push(i)
    print(mh1.heap)

    mh1 = MinHeap()
    mh1.push(6, priority=3)
    mh1.push(6, priority=8)
    mh1.push(17, priority=2)
    mh1.push(17, priority=5)
    print(mh1.heap)

    print("peek:", mh1.peek())

    p1 = mh1.pop()
    print(p1[0], 'priority:', p1[1])  # notice that the higher priority (of 8) 6 is popped first
    p2 = mh1.pop()
    print(p2[0], 'priority:', p2[1])
