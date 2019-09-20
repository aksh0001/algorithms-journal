"""
Write a function to test whether two lists intersect at a particular node, and return that node.

E.g.
l1 = 4->5->2->11 \
                   >8->9
l2 =       4->3  /

return 8
Approaches:
1) Standard hashtable seen approach (Con: too much space)
2) Optimal arithmetic approach

@author a.k
"""
from data_structures.LinkedList import ListNode, SinglyLinkedList


def get_intersection_node(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Returns the intersecting node of the two lists
    Algorithm: Calculate the difference in lengths of the two lists, d.
        - Move pointer of the longer list d steps ahead
        - This allows for something really simple to follow:
            - Traverse each list concurrently, one step at a time. If the pointers meet, then its an intersection.
            - If they never meet, there is no intersection.
    :param l1: list 1
    :param l2: list 2
    :Time: O(n + m)
    :Space: O(1)
    :return: the intersecting node of the linked lists; if no intersection, returns None
    """
    # Get the length of both lists
    n = get_length(l1)
    m = get_length(l2)

    # calc d = |n-m| to determine how much we need to advance the longer list; once we advanced the longer list
    # d steps ahead, simply advance concurrently one step at a time and if they meet, return the intersecting node
    d = abs(n - m)

    # if l1 is longer, advance pointer d steps ahead
    if n > m:
        for i in range(d):
            l1 = l1.next
    elif m > n:  # else, advance l2 d steps ahead
        for i in range(d):
            l2 = l2.next

    while l1 and l2:
        if l1 == l2:  # if they meet, then this is the intersection node
            return l1
        l1 = l1.next
        l2 = l2.next

    return None  # no intersection


def get_length(head):
    """
    Returns the length of the linked list.
    :param head: head of list
    :Time: O(N)
    :Space: O(1)
    :return: the length
    """
    c = 0
    while head:
        c += 1
        head = head.next
    return c


def naive(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Returns the intersecting node of the two lists
    Algorithm: Consider the smaller of the two lists:
            - Add each node of the smaller list into a ht to mark that it's seen (n.b. we use smaller one to save space)
            - Traverse the larger list and if a node has been seen before, i.e. it overlaps with a node in the smaller
                list, then we have found the intersecting node.
                - If no such node found, no intersection exists.
    :param l1: list 1
    :param l2: list 2
    :Time: O(n + m)
    :Space: O(min(n,m)) for the seen dict, we choose to create it for the smaller of the two lists
    :return: the intersecting node of the linked lists; if no intersection, returns None
    """
    n = (get_length(l1), l1)
    m = (get_length(l2), l2)
    smaller = min(n, m, key=lambda x: x[0])[1]  # choose the smaller list, of l1 and l2
    larger = max(n, m, key=lambda x: x[0])[1]
    seen = {}
    while smaller:  # Using the smaller list, track seen nodes using a hash table
        seen[smaller] = True
        smaller = smaller.next
    while larger:
        if larger in seen:  # if any node in the larger list has been seen (overlaps with smaller list) return it
            return larger
        larger = larger.next
    return None  # no intersection


def is_intersecting(l1: ListNode, l2: ListNode) -> bool:
    """
    Checks whether l1 and l2 intersect.
    Algorithm: Simple: intersecting nodes have the same last node
    :param l1: list 1
    :param l2: ist 2
    :Time: O(n+m)
    :return: whether they intersect
    """
    while l1.next:  # get last node of l1
        l1 = l1.next
    while l2.next:  # get last node of l2
        l2 = l2.next
    return l1 == l2


if __name__ == '__main__':
    # T1
    l1 = SinglyLinkedList()
    l2 = SinglyLinkedList()
    l1.insert(4)
    l1.insert(5)
    l1.insert(2)
    l1.insert(17)
    intersect = ListNode(8)  # intersecting node
    l1.current.next = intersect
    l1.current = intersect
    l1.insert(9)
    l1.insert(101)
    l1.insert(22)
    l2.insert(4)
    l2.insert(3)
    l2.current.next = intersect
    l2.current = intersect
    print(is_intersecting(l1.head, l2.head))
    print("Arithmetic approach:", get_intersection_node(l1.head, l2.head).key)
    print("Naive:", naive(l1.head, l2.head).key, end="\n\n")
    print(is_intersecting(l1.head, l2.head))

    # T2
    l1 = SinglyLinkedList()
    l2 = SinglyLinkedList()
    l1.insert(4)
    l1.insert(5)
    l1.insert(2)
    l1.insert(17)
    l1.insert(9)
    l1.insert(101)
    l1.insert(22)
    l2.insert(4)
    l2.insert(3)
    print(is_intersecting(l1.head, l2.head))
    print("Arithmetic approach:", get_intersection_node(l1.head, l2.head))
    print("Naive:", naive(l1.head, l2.head), end="\n\n")
    print(is_intersecting(l1.head, l2.head))

    # T3
    l1 = SinglyLinkedList()
    l2 = SinglyLinkedList()
    l1.insert(4)
    l1.insert(1)
    intersect = ListNode(1738)  # intersecting node
    l1.current.next = intersect
    l1.current = intersect
    l1.insert(4)
    l1.insert(5)
    l2.insert(5)
    l2.insert(0)
    l2.insert(1)
    l2.current.next = intersect
    l2.current = intersect
    print(is_intersecting(l1.head, l2.head))
    print("Arithmetic approach:", get_intersection_node(l1.head, l2.head).key)
    print("Naive:", naive(l1.head, l2.head).key)

    print('PASSED')
