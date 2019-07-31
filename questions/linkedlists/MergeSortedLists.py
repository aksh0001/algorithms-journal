"""
Merge two sorted linked lists and return it as a new sorted list.
The new list should be made by splicing together the nodes of the first two lists.

Approaches: Standard merging of two lists approach

@author a.k
"""
from data_structures.LinkedList import ListNode, SinglyLinkedList
import random


def solution(l1: ListNode, l2: ListNode):
    """
    Merges two sorted linked lists, l1 and l2 into a larger linked list
    Algorithm: Standard merge algorithm. This time, no additional auxiliary space is used; we'll be manipulating
    pointers. traverse both lists simultaneously; point a dummy list's next node to the smaller of the two nodes
    :param l1: list 1
    :param l2: list 2
    :Time: O(N + M)
    :Space: O(1) (no linked list is created, only new pointers to a dummy list are created)
    :return: larger, sorted linked list
    """
    dummy = ListNode(-1)  # Only create one dummy node
    curr = dummy
    while l1 and l2:
        if l1.key < l2.key:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    # If a longer list exists, append it to curr.next
    curr.next = l1 or l2

    return dummy.next  # Disregard dummy node


if __name__ == "__main__":
    l1 = SinglyLinkedList()
    l1.insert(5)
    l1.insert(8)
    l1.insert(9)
    l2 = SinglyLinkedList()
    l2.insert(4)
    l2.insert(7)
    l2.insert(8)
    l2.insert(10)

    ans = solution(l1.head, l2.head)
    ans_print = SinglyLinkedList()
    ans_print.head = ans
    ans_print.print_list()

    l1 = SinglyLinkedList()
    l2 = None
    for i in range(-5, 5, ):
        l1.insert(i)
    ans = solution(l1.head, l2)
    ans_print = SinglyLinkedList()
    ans_print.head = ans
    ans_print.print_list()

    l1 = SinglyLinkedList()
    l2 = SinglyLinkedList()
    for i in range(15):
        l1.insert(i)
        l2.insert(2 * i)
    ans = solution(l1.head, l2.head)
    ans_print = SinglyLinkedList()
    ans_print.head = ans
    ans_print.print_list()
