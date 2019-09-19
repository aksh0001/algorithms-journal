"""
Module to check whether a linked list is a palindrome.
Approaches: 1) Use a stack (O(N) space and time); 2) Reverse and compare (O(N) time O(N) space)

todo: we are comparing the whole list - only need to check half the list, since the other half will be identical
See: https://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/

@author a.k
"""
from data_structures.LinkedList import ListNode, SinglyLinkedList
from data_structures.Stack import Stack


def is_palindrome(head: ListNode) -> bool:
    """
    Returns whether the linked list is a palindrome.
    Algorithm: Add each node into a stack
               Then, for each node pop() and check if that node equals the popped node; if not, return False
               since a palindrome must read the same backwards and forwards
    :param head: head of list
    :Time: O(N)
    :Space: O(N)
    :return: true if palindrome
    """
    S = Stack()
    curr = head
    while curr is not None:
        S.push(curr)  # add each node onto a stack
        curr = curr.next
    curr = head
    while curr is not None:
        if curr.key != S.pop().key:  # check if the current node is the same as the node at the top of the stack
            return False  # if not, then LL is not a palindrome
        curr = curr.next
    return True


def alternate(head: ListNode) -> bool:
    """
    Returns whether the linked list is a palindrome.
    Algorithm: Reverse the list and compare element by element if the reversed list matches the original list
    :param head: head of list
    :Time: O(N)
    :Space: O(N)
    :return: true if palindrome
    """
    rev_head = clone_reverse(head)
    curr = head
    while curr is not None:
        if curr.key != rev_head.key:
            return False
        curr = curr.next
        rev_head = rev_head.next
    return True


def clone_reverse(head: ListNode) -> ListNode:
    """
    Reverses the original list by creating a new one with the help of a stack
    :param head: original list head
    :Time: O(N)
    :Space: O(N)
    :return: new list head
    """
    S = Stack()
    curr = head
    while curr is not None:
        S.push(curr)  # add each node onto a stack
        curr = curr.next
    new_list = ListNode(S.pop().key)
    new_list_head = new_list
    while not S.is_empty():
        new_list.next = ListNode(S.pop().key)
        new_list = new_list.next
    return new_list_head


if __name__ == '__main__':
    test = SinglyLinkedList()
    test.insert(6)
    test.insert(5)
    test.insert(5)
    test.insert(6)
    assert is_palindrome(test.head), "Error!"
    assert alternate(test.head), "Error!"

    test = SinglyLinkedList()
    test.insert(1)
    test.insert(7)
    test.insert(3)
    test.insert(8)
    test.insert(3)
    test.insert(7)
    test.insert(1)
    assert is_palindrome(test.head), "Error!"
    assert alternate(test.head), "Error!"

    test = SinglyLinkedList()
    test.insert(2)
    test.insert(6)
    test.insert(1)
    assert not is_palindrome(test.head), "Error!"
    assert not alternate(test.head), "Error!"
