"""
This module implements Linked Lists.

@author a.k
"""
from typing import List


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
        self.n = 0  # Track number of nodes

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
        self.n += 1

    def get(self, key) -> ListNode:
        """
        Returns a node associated with a key
        :param key: key to be added
        :return: node with the given key
        :Time: O(N)
        :Space: O(1)
        """
        if self.head is None:
            return None

        curr = self.head
        while curr is not None:
            if curr.key == key:
                return curr
            curr = curr.next

    def delete_start(self):
        """
        Deletes node at the start of the list
        :return: none
        :Time: O(1)
        """
        self.head = self.head.next
        self.n -= 1

    def delete_end(self):
        """
        Deletes node at end of list
        :return: none
        :Time: O(N)
        """
        if self.head is None:
            return
        if self.head.next is None:  # if list only has one node
            self.head = None
            self.n -= 1
            return

        temp = self.head
        while temp.next.next is not None:
            temp = temp.next

        temp.next = None
        self.current = temp
        self.n -= 1

    def print_list(self):
        """
        Prints the linked list
        :return: void
        :Time: O(N)
        :Space: O(1)
        """
        if not self.head:
            print(None)
            return
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
            self.n -= 1

    def add_at_head(self, key: int) -> None:
        """
        Adds a node to the head of the list
        :param key: key of node
        :Time: O(1)
        :return: none
        """
        if not self.head:
            self.head = ListNode(key)
            self.current = self.head
        else:
            node = ListNode(key)
            node.next = self.head
            self.head = node
        self.n += 1

    def add_at_tail(self, key: int) -> None:
        """
        Adds a node at the tail
        :param key: key of node to be added
        :Time: O(1)
        :return: none
        """
        if not self.head:
            self.add_at_head(key)
        else:
            self.current.next = ListNode(key)
            self.current = self.current.next
            self.n += 1

    def add_at_index(self, index: int, key: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of LL,
        the node will be appended to the end of linked list.
        :param index: index of node to be added
        :param key: key of node to be added
        :Time: O(N)
        :return: none
        """
        if index == self.n:  # append to end if we have to add at the index'th node
            self.add_at_head(key)
        elif index == 0:  # add to head if we hae to add at the start
            self.add_at_tail(key)
        elif 0 <= index <= self.n - 1:
            p1 = self.head
            for i in range(index - 1):
                p1 = p1.next
            tmp = p1.next  # save next
            p1.next = ListNode(key)  # create
            p1.next.next = tmp  # repoint to saved
            self.n += 1

    def delete_at_index(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        :param index: index of node to be deleted
        :Time: O(1)
        :return: none
        """
        if 0 <= index <= self.n - 1:
            if index == 0:  # remove from head if deleting at index 0
                self.head = self.head.next
                if self.n == 1:  # update curr if deleting from a list with 1 node
                    self.current = None
            else:
                p1 = self.head
                for i in range(index - 1):  # get p1 to index-1 position ready to delete
                    p1 = p1.next
                if index == self.n - 1:  # if deleting last node, update curr
                    self.current = p1
                p1.next = p1.next.next  # delete the node
            self.n -= 1

    def get_by_index(self, index: int):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :param index: index of item
        :Time: O(N)
        :return: the key at the index'th node
        """
        if index < 0 or index >= self.n:
            return -1
        p1 = self.head
        for i in range(index):
            p1 = p1.next
        return p1.key

    def __iter__(self):
        """
        Iterate over the linked list.
        """
        current = self.head
        while current:
            yield current.key
            current = current.next


if __name__ == "__main__":
    test = SinglyLinkedList()
    for i in range(1, 10 + 1):
        test.insert(i, i ** 2)

    test.delete_start()
    test.delete_end()
    test.delete_end()
    test.delete_start()

    test.delete_by_key(5)
    test.delete_by_key(3)
    test.delete_by_key(7)
    test.delete_by_key(8)

    for i in range(10, 15 + 1):
        test.insert(i, i ** 2)

    test.delete_by_key(12)
    test.delete_by_key(14)
    test.delete_start()
    test.delete_end()
    test.delete_by_key(13)

    test.print_list()  # test: 6->10->11
    print(test.get(10).val)
    print(test.get(11).val)
    print(test.get(1738))

    # Testing iterator
    test.print_list()
    print('---')
    for t in test:
        print(t)
