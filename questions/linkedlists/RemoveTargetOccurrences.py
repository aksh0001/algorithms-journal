"""
Remove all elements from a linked list of integers that have value val.
Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

E.g. 6 (val = 6) ==> []
6->6->6->6 (val = 6) ==> []
6->6->2->6 (val = 6) ==> 2
1->3->6->2->6->6->2 (val = 6) ==> 1->3->2->2
"""
from data_structures.LinkedList import ListNode, SinglyLinkedList


def remove_occurrences(head: ListNode, key: int) -> ListNode:
    """
    Given a key, key, removes all occurrences of it in the list.
    @Algorithm: 2-pointer approach (with p2 1-away from p1):
                - using standard 2-pointer approach if p1.key = key and p2 exists, follow standard deletion
                - however the special case is handling a list with the head itself that needs to be removed
                - for this case we make use of ret_val, which represents the head of resulting list.
                - if the head itself needs to be removed, p2 will be none;
                - therefore, we can update our ret_val to p1.next to signify that we are excluding this node
    :param head: head of list
    :param key: instances of nodes with key to be removed
    :Time: O(N)
    :Space: O(1)
    :return: resulting list head
    """
    """
    State trackers for two-pointer (1-away p1, p2) approach:
    p1 = current node
    p2 = prev node
    ret_val = head of resulting list (which is useful if the head itself = val)
    """
    p1, p2, ret_val = head, None, head
    while p1:
        if p1.key == key and p2:  # standard deletion case (p2 exists)
            p2.next = p1.next
            p1 = p1.next  # don't update p2 since it's still prev

        elif p1.key == key and not p2:  # special case; head itself = val (because p2 is None)
            ret_val = p1.next  # update resulting head node to exclude this node
            p1 = p1.next  # don't update p2

        else:  # just advance as normal
            p2 = p1
            p1 = p1.next
    return ret_val


if __name__ == '__main__':
    t = SinglyLinkedList()
    t.insert(6)
    tmp = SinglyLinkedList()
    tmp.head = remove_occurrences(t.head, 6)
    tmp.print_list()

    t = SinglyLinkedList()
    t.insert(6)
    t.insert(6)
    t.insert(6)
    t.insert(6)
    tmp = SinglyLinkedList()
    tmp.head = remove_occurrences(t.head, 6)
    tmp.print_list()

    t = SinglyLinkedList()
    t.insert(6)
    t.insert(6)
    t.insert(2)
    t.insert(6)
    tmp = SinglyLinkedList()
    tmp.head = remove_occurrences(t.head, 6)
    tmp.print_list()

    t = SinglyLinkedList()
    t.insert(1)
    t.insert(3)
    t.insert(6)
    t.insert(2)
    t.insert(6)
    t.insert(6)
    t.insert(2)
    tmp.head = remove_occurrences(t.head, 6)
    tmp.print_list()

    t = SinglyLinkedList()
    t.insert(1)
    t.insert(2)
    t.insert(6)
    t.insert(3)
    t.insert(4)
    t.insert(5)
    t.insert(6)
    tmp.head = remove_occurrences(t.head, 6)
    tmp.print_list()
