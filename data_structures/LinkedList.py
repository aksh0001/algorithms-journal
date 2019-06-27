"""
This module implements Linked Lists.

@author a.k
"""


class ListNode():
    def __init__(self, key, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class SinglyLinkedList():
    def __init__(self):
        self.head = None  # Head of LL
        self.current = None  # Keeps track of most recently inserted node for O(1) insert

    def insert(self, key, val=None):
        """
        Adds a new node to the end of the list
        :param key: key to be added
        :param val: associated val (optional)
        :return: void
        :Time: O(1) as we keep track of most recently added node (else we'd need to traverse)
        :Space: O(1)
        """
        node = ListNode(key, val)
        if self.head is None:
            self.head = node
            self.current = self.head
        else:
            self.current.next = node
            self.current = self.current.next  # Update most recently inserted node

    def delete_start(self):
        """
        Deletes node at the start of the list
        :return: none
        :Time: O(1)
        """
        self.head = self.head.next

    def delete_end(self):
        """
        Deletes node at end of list
        :return: none
        :Time: O(N)
        """
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next is not None:
            temp = temp.next

        temp.next = None
        self.current = temp

    def print_list(self):
        """
        Prints the linked list
        :return: void
        :Time: O(N)
        :Space: O(1)
        """
        temp = self.head
        while temp.next is not None:
            print(str(temp.key) + "->", end=" ")
            temp = temp.next
        print(str(temp.key) + "|")

    def delete_by_key(self, key):
        """
        Deletes a node in the list by given key
        :param key: key
        :return: none
        :Time: O(1)
        """
        temp = self.head
        if temp.key == key:
            self.delete_start()
            return
        while temp.next.key != key and temp.next is not None:  # Find prior node to matching node (same as delete_end)
            temp = temp.next

        if temp.next is not None:  # If temp references last node, not found
            if temp.next.next is None:  # If last node to be deleted, update current
                self.current = temp
            temp.next = temp.next.next


if __name__ == "__main__":
    test = SinglyLinkedList()
    for i in range(1, 10 + 1):
        test.insert(i)

    test.delete_start()
    test.delete_end()
    test.delete_end()
    test.delete_start()

    test.delete_by_key(5)
    test.delete_by_key(3)
    test.delete_by_key(7)
    test.delete_by_key(8)

    for i in range(10, 15 + 1):
        test.insert(i)

    test.delete_by_key(12)
    test.delete_by_key(14)
    test.delete_start()
    test.delete_end()
    test.delete_by_key(13)

    test.print_list()  # test: 6->10->11
