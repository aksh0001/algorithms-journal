"""
Given a singly linked list, return a random node's value from the linked list.
Each node must have the same probability of being chosen.
Follow up:
What if the linked list is extremely large and its length is unknown to you?
Could you solve this efficiently without using extra space?

Approaches: Naive, --> Reservoir Sampling <--

Ref: https://leetcode.com/problems/linked-list-random-node/discuss/85662/Java-Solution-with-cases-explain

@author a.k
"""
from data_structures.LinkedList import ListNode, SinglyLinkedList
import matplotlib.pyplot as plt  # for graphing probability distribution
from random import randint
import numpy as np


def naive(h: ListNode):
    """
    Easy solution: Get length n, generate d = rand(0,n-1), get d'th node
    :param h: head of list
    :Time: O(N)
    :Space: O(1)
    :return: random node
    """

    def get_length(h: ListNode) -> int:
        count = 0
        while h:
            count += 1
            h = h.next
        return count

    def get_node_by_idx(h: ListNode, idx: int):
        for i in range(idx):
            if h:
                h = h.next
            else:
                raise AssertionError('index out of bounds')
        return h

    d = randint(0, get_length(h) - 1)
    return get_node_by_idx(h, d).key


def reservoir_sampling(h: ListNode):
    """
    Reservoir Sampling algorithm.
    @Algorithm: for a list with n nodes, nth node has 1/n of being chosen, and for the remaining n-1 nodes
                with total probability of n-1/n, each node gets chosen with 1/n prob. This needs to be proven.
    :param h: head
    :return: random node's value
    """
    r, i = 0, 0  # r = result; i = current loop count
    while h:
        take = (randint(0, i)) == 0  # take/update r based on probability of 1/i
        if take:
            r = h.key  # if we take this node, update r
        i += 1
        h = h.next
    return r


if __name__ == '__main__':
    # Testing 1
    n_epochs, n_iter, y_plot, x_plot = 3, int(1e5), [0, 0, 0, 0], [0, 1, 2, 3]
    test = SinglyLinkedList()
    test.insert(0)
    test.insert(1)
    test.insert(2)
    test.insert(3)
    for epoch in range(1, n_epochs + 1):
        for i in range(n_iter):
            y_plot[reservoir_sampling(test.head)] += 1
        plt.bar(x_plot, y_plot, alpha=0.5)
        plt.xticks(np.arange(4), ('1', '2', '3', '4'))
        plt.ylabel('Frequency')
        plt.show()
        plt.title('Run ' + str(epoch) + ' with n = ' + str(n_iter))
        y_plot = [0, 0, 0, 0]
