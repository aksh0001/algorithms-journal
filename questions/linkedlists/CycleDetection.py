"""
Implements the linked list cycle detection problem. Given a linked list, which may or may not be circular,
implement an algorithm that returns the node at the start of the cycle.

Approaches: Naive + Floyd's Cycle detection algorithm

@author a.k
"""
from data_structures.LinkedList import SinglyLinkedList, ListNode


def naive(head: ListNode) -> ListNode:
    """
    If a cycle exists in the LL, returns the node at the start of the cycle. Else, returns None
    Algorithm: Track visited nodes using a map. If a node is re-visited, return that node (start of cycle)
    Edge-cases: None head, only one node
    :param head: head of LL
    :return: the point where the cycle begins, if it exists
    :Time: O(N)
    :Space: O(N)
    """
    if head is None or head.next is None:  # Not possible to have a cycle
        return None
    seen = {}  # A hash-set would work better
    curr = head
    while curr is not None:
        if curr in seen:
            return curr
        else:
            seen[curr] = True
        curr = curr.next
    return None


if __name__ == "__main__":
    test_1 = SinglyLinkedList()
    for i in range(1, 4 + 1):  # 1->2->3->4
        test_1.insert(i, i ** 2)
    test_1.current.next = test_1.get(2)  # 1->2->3->4->2

    test_2 = SinglyLinkedList()
    for i in range(1, 4 + 1):  # 1->2->3->4
        test_2.insert(i, i ** 2)
    test_2.current.next = test_2.get(1)  # 1->2->3->4->1

    test_3 = SinglyLinkedList()
    for i in range(1, 4 + 1):  # 1->2->3->4
        test_3.insert(i, i ** 2)
    test_3.current.next = test_3.get(3)  # 1->2->3->4->3

    test_4 = None
    test_5 = SinglyLinkedList().insert(1)

    tests = [test_1, test_2, test_3, test_4, test_5]
    ans = [4, 1, 9, None, None]

    for t, a in zip(tests, ans):
        if a is not None:
            assert naive(t.head).val == a, "Error!"
        else:
            if t is None:
                assert naive(t) is None, "Error!"
            else:
                assert naive(t.head) == a, "Error!"
