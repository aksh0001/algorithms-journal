"""
Module for removing duplicates in a linked list
@author a.k
"""
from data_structures.LinkedList import *


def remove_duplicates(head: ListNode):
    """
    Removes duplicate keys in a linked list
    :param head: head of the linked list
    :return: none
    :Time: O(N)
    :Space:  O(N)
    """
    seen = {}  # track seen elements
    temp = head  # Pointer tracks current node
    prev = None  # Pointer tracks previous node

    while temp is not None:
        if temp.key in seen:
            prev.next = temp.next  # Remove that node that is seen
        else:
            seen[temp.key] = True
            prev = temp  # Update pointer to point to temp/current (only update if not seen)
        temp = temp.next


def remove_duplicates_no_buffer(head: ListNode):
    """
    Removes duplicate keys in a linked list, using O(1) auxiliary space
    :param head: head of list
    :return: none
    :Time: O(N^2)
    :Space: O(1)
    """
    current = head
    while current is not None:
        # Inner loop to check if current's value matches with a runner pointer which iterates over the rest of the list
        runner = current
        while runner.next is not None:  # Avoided using a prev pointer by only comparing runner.next
            if runner.next.key == current.key:
                runner.next = runner.next.next
            else:
                runner = runner.next

        current = current.next


if __name__ == "__main__":
    test = SinglyLinkedList()
    test.insert(1)
    test.insert(1)
    test.insert(2)
    test.insert(3)
    test.insert(2)
    test.insert(5)
    test.insert(4)
    test.insert(3)
    print("Before:")
    test.print_list()
    remove_duplicates_no_buffer(test.head)
    print("After")
    test.print_list()

    test2 = SinglyLinkedList()
    # for i in range (1, 11):
    #     test2.insert(i)
    test2.insert(1)
    test2.insert(1)
    test2.insert(1)

    print("Before:")
    test2.print_list()
    print("After: ")
    remove_duplicates_no_buffer(test2.head)
    test2.print_list()
