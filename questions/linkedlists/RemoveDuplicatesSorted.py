"""
Module for removing duplicates in a sorted LL.
99.9% performance on leetcode.

@author a.k
"""
from data_structures.LinkedList import SinglyLinkedList, ListNode


def delete_duplicates(head: ListNode) -> ListNode:
    """
    Deletes duplicates from a sorted linked list and returns the head of the resulting list
    :param head: head of list
    :Time: O(N)
    :Space: O(1)
    :return: head of resulting list
    """
    # Two-pointer one-away approach
    # p1 is one ahead of p2; if p1 = p2, remove p1 by p2.next = p1.next
    p1, p2 = head, None
    while p1:
        if p2 and p1.key == p2.key:
            p2.next = p1.next  # remove it
            p1 = p1.next  # dont step p2
        else:
            p2 = p1
            p1 = p1.next
    return head


if __name__ == '__main__':
    test = SinglyLinkedList()
    test.insert(1)
    test.insert(1)
    test.insert(2)
    test.insert(3)
    test.insert(3)
    test.print_list()
    h = delete_duplicates(test.head)
    result = SinglyLinkedList()
    result.head = h
    result.print_list()
