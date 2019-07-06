"""
Module to find the Kth to last element in a linked list.
@author a.k
"""
from data_structures.LinkedList import *
from data_structures.Stack import *


class Attempt():
    def __init__(self):
        pass

    def attempt_1(self, head: ListNode, k: int) -> ListNode:
        """
        Naive solution: Find the length of the list, N, and return the N-kth node
        :param head: head of list
        :param k: parameter, k
        :return: returns the k'th to last element
        :Time: O(N)
        :Space: O(1)
        """
        # Find the length, N of the list; then, calculate L = N - k; and return the L'th node
        N = 0
        curr = head
        while curr is not None:
            N += 1
            curr = curr.next

        L = N - k
        i = 0
        curr = head
        while curr is not None and i < L:
            i += 1
            curr = curr.next

        return curr

    def attempt_2(self, head: ListNode, k: int) -> ListNode:
        """
        Better solution: Insert all elements into a stack and pop k elements. The last popped is returned.
        Don't need to know the length of the list in this algorithm.
        :param head: head of list
        :param k: parameter, k
        :return: returns the k'th to last element
        :Time: O(N)
        :Space: O(N)
        """
        stack = Stack()
        curr = head
        while curr is not None:
            stack.push(curr)
            curr = curr.next

        ret_val = None
        for i in range(k):
            popped = stack.pop()
            if i == k - 1:
                ret_val = popped

        return ret_val

    def attempt_recursive(self, head: ListNode, k: int):
        """
        Similar to attempt_2 using stack;this time, it is recursion. When base case is hit, returns a counter set to 0.
        Each parent call adds 1 to the counter and when the value, k, is hit, we print out the node.
        :param head: head of list
        :param k: parameter, k
        :return: none
        :Time: O(N)
        :Space: O(N) N calls
        """
        if head is None:
            return 0

        index = self.attempt_recursive(head.next, k) + 1
        if index == k:
            print(k, "th to last node is", head.key)

        return index


def solution(head: ListNode, k: int) -> ListNode:
    """
    Neat Trick: pointer, p1, is first moved to position k; there are N - k nodes to traverse.
    Then, move pointer p1, along with p2, from k to N.
    Pointer, p2, will now point to the N-kth position, or k nodes from the end.
    :param head: head of list
    :param k: parameter, k
    :return: returns the k'th to last element
    :Time: O(N)
    :Space: O(1)
    """
    p1 = head
    p2 = head
    for i in range(k):  # Move p1 k nodes into the list
        p1 = p1.next
    # Now move p1 to the end while moving p2
    while p1 is not None:
        p1 = p1.next
        p2 = p2.next
    return p2


if __name__ == "__main__":
    print("Testing...")
    test = SinglyLinkedList()
    test.insert(1)
    test.insert(1)
    test.insert(2)
    test.insert(3)
    test.insert(2)
    test.insert(5)
    test.insert(4)
    test.insert(3)
    test.print_list()

    att = Attempt()
    print(solution(test.head, 3).key)
