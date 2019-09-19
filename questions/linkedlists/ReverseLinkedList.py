"""
This module reverses a linked list using an iterative and recursive approach.
Iterative: Time: O(N) Space: O(1)
Recursive: Time: O(N) Space: O(N)

N.B. these implementations modify the original list

@author a.k
"""
from data_structures.LinkedList import SinglyLinkedList, ListNode


def iterative(head: ListNode) -> ListNode:
    """
    Iteratively reverses the linked list by manipulating pointers. Uses O(1) aux space.
    Algorithm:
        Consider three pointers, p1, p2, p3;
        p2 = current node; p3 = previous node; p1 = future node (must save this in order to iterate)
        - Save future (next) node in p1.
        - Use p2 to perform a reversal by doing p2.next = p3
        - Update p3 to p2 and p2 to p1
    :param head: head of list
    :Time: O(N)
    :Space: O(1)
    :return: the head of the reversed list
    """
    p1 = head
    p2 = head
    p3 = None
    while p2 is not None:
        p1 = p1.next  # Save next node
        p2.next = p3  # reverse the link of current by pointing its next to the previous, p3
        p3 = p2  # update/step p3
        p2 = p1  # update/step p1
    head = p3
    return head


def recursive(head: ListNode) -> ListNode:
    """
    Recursively reverses a linked list (similar to recursively reverse a string)
    Algorithm:
        - Consider the head of the list, head
        - Recursively reverse head.next
        - Notice head.next points to the last node in the recursively reversed list;
            therefore, set head.next.next to head
        - CAUTION: we are not done: head.next points to the last node of the reversed list and the
                    last node points to the head, creating a cycle; therefore, set head.next = None
    :param head: head of list
    :Time: O(N)
    :Space: O(N)
    :return: starting node of reversed list
    """
    if head is None or head.next is None:
        return head

    # note: added more, unnecessary, lines to make it more readable and clear what is happening
    new_head = recursive(head.next)  # recursively reverse the rest
    last = head.next  # notice: last node in the reversed list will be head.next
    last.next = head  # attach last node's link in the reversed list to head
    last = head  # now, the new last is the head
    last.next = None  # to prevent a cycle, set head's next to None
    head = new_head
    return head


if __name__ == '__main__':
    print("\n>>>Testing iterative<<<\n")
    print('Original:')
    # Test 1
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
    new_list_head = iterative(test.head)
    new_list = SinglyLinkedList()
    new_list.head = new_list_head
    print("Reversed:")
    new_list.print_list()
    # Test 2
    print("Original:")
    test = SinglyLinkedList()
    test.insert(20)
    test.insert(4)
    test.insert(15)
    test.insert(85)
    test.print_list()
    new_list_head = iterative(test.head)
    new_list = SinglyLinkedList()
    new_list.head = new_list_head
    print("Reversed:")
    new_list.print_list()
    # Test 3
    print("Original")
    test = SinglyLinkedList()
    test.insert(20)
    test.print_list()
    new_list_head = iterative(test.head)
    new_list = SinglyLinkedList()
    new_list.head = new_list_head
    print("Reversed:")
    new_list.print_list()
    assert new_list_head == test.head, "Error!"
    # Test 4
    test = SinglyLinkedList()
    new_list_head = iterative(test.head)
    new_list = SinglyLinkedList()
    new_list.head = new_list_head
    assert new_list_head == test.head, "Error!"

    print("\n>>>Testing recursive<<<\n")

    print('Original:')
    # Test 1
    test = SinglyLinkedList()
    test.insert(1)
    test.insert(99)
    test.insert(2)
    test.insert(3)
    test.insert(2)
    test.insert(5)
    test.insert(4)
    test.insert(3)
    test.print_list()
    new_list_head = recursive(test.head)
    new_list = SinglyLinkedList()
    new_list.head = new_list_head
    print("Reversed:")
    new_list.print_list()
    # Test 2
    print("Original:")
    test = SinglyLinkedList()
    test.insert(20)
    test.insert(4)
    test.insert(15)
    test.insert(85)
    test.print_list()
    new_list_head = recursive(test.head)
    new_list = SinglyLinkedList()
    new_list.head = new_list_head
    print("Reversed:")
    new_list.print_list()
    # Test 3
    print("Original")
    test = SinglyLinkedList()
    test.insert(20)
    test.print_list()
    new_list_head = recursive(test.head)
    new_list = SinglyLinkedList()
    new_list.head = new_list_head
    print("Reversed:")
    new_list.print_list()
    assert new_list_head == test.head, "Error!"
    # Test 4
    test = SinglyLinkedList()
    new_list_head = recursive(test.head)
    new_list = SinglyLinkedList()
    new_list.head = new_list_head
    assert new_list_head == test.head, "Error!"
