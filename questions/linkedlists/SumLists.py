"""
Implements a solution to the sum lists problem:
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

E.g.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

FOLLOW-UP: IF THE TWO LISTS ARE IN FORWARD ORDER, REPEAT THE PROBLEM.
E.g. (6->1->7) + (2->9->5) = (9->0->2)

@author a.k
"""
from data_structures.LinkedList import ListNode, SinglyLinkedList
from data_structures.Stack import Stack
from questions.linkedlists.ReverseLinkedList import reverse_list


def sum_lists(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Adds the two lists and returns a new list with the sum.
    >>N.B: IF WE CAN MODIFY ORIGINAL LIST, SAVE SPACE BY ACCUMULATING SUM IN EITHER l1 or l2!!<<
    Algorithm:
        - Process concurrently both lists
        - Calculate sum of current l1 node, l2 node, and the carry bit
        - Append the last digit (num%10) onto l3, the resulting list
        - If this num > 9, set carry to 1
        - If any list is of greater length, accumulate the sums of that list into l3
        - Important at the end: if l1 and l2 have reached the end and the carry=1, append the carry (e.g. 400+600=1000)
    :param l1: list 1
    :param l2: list 2
    :Time: O(n + m)
    :Space: O(n + m)
    :return: head node of resulting sum list
    """
    l3 = ListNode(-1)  # dummy
    l3_h = l3
    carry = 0  # carry bit
    while l1 and l2:
        num = l1.key + l2.key + carry
        l3.next = ListNode(num % 10)  # add last digit of sum
        if num > 9:
            carry = 1
        else:
            carry = 0
        l3 = l3.next
        l2 = l2.next
        l1 = l1.next
    # either l1 or l2 can still have nodes, accumulate those as well
    while l1:
        num = l1.key + carry
        l3.next = ListNode(num % 10)
        if num > 9:
            carry = 1
        else:
            carry = 0
        l3 = l3.next
        l1 = l1.next
    while l2:
        num = l2.key + carry
        l3.next = ListNode(num % 10)
        if num > 9:
            carry = 1
        else:
            carry = 0
        l3 = l3.next
        l2 = l2.next
    # important step; if at end of both lists and carry bit is set to 1, append that
    if carry == 1 and (l1 is None and l2 is None):
        l3.next = ListNode(carry)

    return l3_h.next


class Follow_up:
    def approach_2(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Adds the two lists in forward order and returns the head of the resulting list.
        Algorithm: Insert both lists, l1 and l2, into separate stacks, S1 and S2.
                    - Then, as from the original alg, pop off S1 and S2 concurrently and add into a new list l3
                    - If either S1 or S2 has remaining items, accumulate into l3
                    - If carry = 1, as before, we add append the carry onto the end as well.
        TODO: *Note that l3 is in reverse order which we do not want. E.g. 7 + 999 = 6001. Fix this by appending to start of l3.
                todo: hack used by reversing l3 at the end -- implement an "insertAtBeginning()" method for l3 to fix!!
        :param l1: list 1
        :param l2: list 2
        :Time: O(n + m)
        :Space: O(n + m)
        :return: head of resulting list
        """
        # Push each list onto a separate stack
        S1 = Stack()
        S2 = Stack()
        while l1:
            S1.push(l1.key)
            l1 = l1.next
        while l2:
            S2.push(l2.key)
            l2 = l2.next
        # What follows is similar to the original approach
        l3_h = l3 = ListNode(-1)
        carry = 0
        while not S1.is_empty() and not S2.is_empty():  # add elements while both stacks are not empty
            num = S1.pop() + S2.pop() + carry
            l3.next = ListNode(num % 10)  # add last digit of sum
            if num > 9:
                carry = 1
            else:
                carry = 0
            l3 = l3.next
        while not S1.is_empty():  # add remaining elements in S1
            num = S1.pop() + carry
            l3.next = ListNode(num % 10)  # add last digit of sum
            if num > 9:
                carry = 1
            else:
                carry = 0
            l3 = l3.next
        while not S2.is_empty():  # add remaining elements in S2
            num = S2.pop() + carry
            l3.next = ListNode(num % 10)  # add last digit of sum
            if num > 9:
                carry = 1
            else:
                carry = 0
            l3 = l3.next
        # important: if carry is set to 1, then it means the sum is overflowing and must include the carry bit
        if carry == 1:
            l3.next = ListNode(carry)
        return reverse_list(l3_h.next)  # todo this is a hack!! when appending sums, append to l3 at the beginning!!!

    def approach_1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Adds the two lists in forward order and returns the head of the resulting list.
        Algorithm: Transform both lists, l1 and l2, into strings, s1 and s2.
                    - Then cast and add them into s3
                    - For each number in s3, append it onto the result list, l3
        :param l1: list 1
        :param l2: list 2
        :Time: O(n + m)
        :Space: O(n + m)
        :return: head of resulting list
        """
        s1 = ""
        s2 = ""
        while l1:  # Append each element into a string
            s1 += str(l1.key)
            l1 = l1.next
        while l2:  # Same for list 2
            s2 += str(l2.key)
            l2 = l2.next
        s3 = str(int(s1) + int(s2))  # s3 contains the casted sum string
        l3_h = l3 = ListNode(-1)  # dummy
        for c in s3:
            l3.next = ListNode(int(c))
            l3 = l3.next
        return l3_h.next


if __name__ == '__main__':
    # T1
    l1 = SinglyLinkedList()
    l2 = SinglyLinkedList()
    l1.insert(2)
    l1.insert(4)
    l1.insert(3)
    l2.insert(5)
    l2.insert(6)
    l2.insert(4)
    l1.print_list()
    print("+")
    l2.print_list()
    print("=")
    head = sum_lists(l1.head, l2.head)
    ans = SinglyLinkedList()
    ans.head = head
    ans.print_list()
    print("---")

    # T2
    l1 = SinglyLinkedList()
    l2 = SinglyLinkedList()
    l1.insert(0)
    l1.insert(0)
    l1.insert(4)
    l2.insert(0)
    l2.insert(0)
    l2.insert(6)
    l1.print_list()
    print("+")
    l2.print_list()
    print("=")
    head = sum_lists(l1.head, l2.head)
    ans = SinglyLinkedList()
    ans.head = head
    ans.print_list()
    print("---")

    # T3
    l1 = SinglyLinkedList()
    l2 = SinglyLinkedList()
    l1.insert(7)
    l2.insert(9)
    l2.insert(9)
    l2.insert(9)
    l1.print_list()
    print("+")
    l2.print_list()
    print("=")
    head = sum_lists(l1.head, l2.head)
    ans = SinglyLinkedList()
    ans.head = head
    ans.print_list()

    # TESTING FOLLOW UP
    # T1
    print(">>TESTING FOLLOW-UP<<")
    fup = Follow_up()
    l1 = SinglyLinkedList()
    l2 = SinglyLinkedList()
    l1.insert(6)
    l1.insert(1)
    l1.insert(7)
    l2.insert(2)
    l2.insert(9)
    l2.insert(5)
    l1.print_list()
    print("+")
    l2.print_list()
    print("=")
    print("Approach using string casting method:")
    head = fup.approach_1(l1.head, l2.head)
    ans = SinglyLinkedList()
    ans.head = head
    ans.print_list()
    print("Approach using stack reverse summing method:")
    head = fup.approach_2(l1.head, l2.head)
    ans = SinglyLinkedList()
    ans.head = head
    ans.print_list()
    print("---")

    # T2
    l1 = SinglyLinkedList()
    l2 = SinglyLinkedList()
    l1.insert(7)
    l2.insert(9)
    l2.insert(9)
    l2.insert(9)
    l1.print_list()
    print("+")
    l2.print_list()
    print("=")
    print("Approach using string casting method:")
    head = fup.approach_1(l1.head, l2.head)
    ans = SinglyLinkedList()
    ans.head = head
    ans.print_list()
    print("Approach using stack reverse summing method:")
    head = fup.approach_2(l1.head, l2.head)
    ans = SinglyLinkedList()
    ans.head = head
    ans.print_list()
