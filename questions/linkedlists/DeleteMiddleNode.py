"""
Module to delete a middle node in a LL, given only that node.

@author a.k
"""
from data_structures.LinkedList import *


def attempt_1(node: ListNode):
    # next_node = node.next
    # node = next_node  # Cannot do this since we are passing by value (i.e. cannot manipulate arg directly)
    pass


def delete_mid_node(node: ListNode):
    """
    Deletes the node in a linked list, specified by the input, node
    :param node: node to be deleted
    :return: none
    :Time: O(1)
    :Space: O(1)
    """
    if node is None or node.next is None:
        return False  # Not possible (cannot pass in a None and last node cannot be a middle node)

    next_node = node.next  # Point to the next node
    node.key = next_node.key  # Copy the next node's data into the current node
    node.val = next_node.val

    # Delete the next node
    node.next = next_node.next


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
    print("Before deleting 2: ")
    test.print_list()
    delete_mid_node(test.head.next.next)  # Delete the first 2
    print("After deleting 2: ")
    test.print_list()
