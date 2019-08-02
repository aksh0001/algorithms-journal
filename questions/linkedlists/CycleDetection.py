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


def solution_alternate(head: ListNode) -> ListNode:
    """
    Another O(1) space alternative to Floyd's algorithm.
    Very clever strategy: Create a dummy node. Traverse the list and re-point the next link of every node to the dummy.
    If we come across that the next link is already pointing to the dummy node--cycle found. If we come across a None,
    no cycle exists.
    :param head: head of list
    :Time: O(N)
    :Space: O(1)
    :return: the starting node of the cycle; none if no cycle present
    """
    DUMMY = ListNode(-1)
    curr = head
    while curr:
        if curr.next == DUMMY:  # If the node is already pointing to the dummy, then it indicates start of cycle
            return curr

        next_copy = curr.next  # Save link to the next node that is about to be re-pointed to the dummy
        curr.next = DUMMY  # Re-point the next node to the dummy node
        curr = next_copy  # Using the saved link, update curr
    return None


def solution(head: ListNode) -> ListNode:
    """
    Uses Floyd's algorithm to return the starting node in a cycle in a linked list
    "Much like two cars racing around a track at different speeds, they must eventually meet"
    @see proof of why this works!
    :param head: head of list
    :Time: O(N)
    :Space: O(1)
    :return: the node at the start of the cycle; None, otherwise.
    """
    p1 = head  # p1 be at a distance = d from the head (by advancing by one)
    p2 = head  # p2 be at a distance = 2*d from the head (by advancing by two)

    while p1 and p2 and p2.next:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:  # Cycle detected if they meet
            break
    if p2 is None or p2.next is None:
        return None  # No cycle

    # Cycle is detected and now we must find the starting point of the cycle, this is where the maths needs to be proven
    # Move either pointer to the head. Each pointer is k steps away from the loop's start. If they move at the same
    # pace, they MUST meet at the start of the loop.
    p1 = head
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next

    # Both pointers point to the start of the cycle
    return p1

    return False  # No cycle detected


def contains_cycle(head: ListNode) -> bool:
    """
    Uses Floyd's algorithm to detect whether there is a cycle in a linked list
    :param head: head of list
    :Time: O(N)
    :Space: O(1)
    :return: True if a cycle exists
    """
    p1 = head  # p1 be at a distance = d from the head (by advancing by one)
    p2 = head  # p2 be at a distance = 2*d from the head (by advancing by two)

    while p1 and p2 and p2.next:  # If p2 is at last node (and its next is None) then no cycle detected
        if p1 == p2:  # Cycle detected if they meet
            return True
        p1 = p1.next
        p2 = p2.next.next

    return False  # No cycle detected


if __name__ == "__main__":
    test_1 = SinglyLinkedList()
    for i in range(1, 4 + 1):
        test_1.insert(i, i ** 2)
    test_1.current.next = test_1.get(2)  # 1->2->3->4->2
    print(contains_cycle(test_1.head))

    test_2 = SinglyLinkedList()
    for i in range(1, 4 + 1):
        test_2.insert(i, i ** 2)
    test_2.current.next = test_2.get(1)  # 1->2->3->4->1
    print(contains_cycle(test_2.head))

    test_3 = SinglyLinkedList()
    for i in range(1, 4 + 1):
        test_3.insert(i, i ** 2)
    test_3.current.next = test_3.get(3)  # 1->2->3->4->3
    print(contains_cycle(test_3.head))

    test_4 = None
    print(contains_cycle(test_4))
    test_5 = SinglyLinkedList()
    test_5.insert(1)
    print(contains_cycle(test_5.head))

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
    print("PASSED NAIVE")

    for t, a in zip(tests, ans):
        if a is not None:
            assert solution(t.head).val == a, "Error!"
        else:
            if t is None:
                assert solution(t) is None, "Error!"
            else:
                assert solution(t.head) == a, "Error!"
    print("PASSED SOLUTION")

    for t, a in zip(tests, ans):
        if a is not None:
            assert solution_alternate(t.head).val == a, "Error!"
        else:
            if t is None:
                assert solution_alternate(t) is None, "Error!"
            else:
                assert solution_alternate(t.head) == a, "Error!"
    print("PASSED ALTERNATE")
    print(">>>PASSED ALL<<<")
