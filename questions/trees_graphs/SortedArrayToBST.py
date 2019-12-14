"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never
differ by more than 1.

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

 Approach: Binary midpoint insertion approach

 @author a.k
"""
from data_structures.trees.utils import pretty_print_tree, TreeNode
from typing import List


def sortedArrayToBST(nums: List[int]) -> TreeNode:
    """
    Given a sorted array of numbers, creates a height-balanced tree and returns root of new tree.
    :param nums: array of numbers
    :return: root of new tree
    """
    return insert(nums, 0, len(nums) - 1)


# Binary midpoint insertion routine
def insert(A: List[int], lo: int, hi: int) -> TreeNode:
    """
    Inserts elements and returns root of new tree.
    @Algorithm: Cannot insert in any sorted, serial order. Must insert in a "shuffled" manner. How?
                - Well, think of mid of array as pivot (root). Left of this pivot must be in the left subtree
                and the right of the pivot must be in the right subtree.
                - Now... we know the left of the pivot must go on the left. But, again, we cannot process the elements
                in a serial fashion; therefore, like above, we recursively insert left/right based on the midpoint approach.
    :param A: list of numbers
    :param lo: lower endpoint interval
    :param hi: higher endpoint interval
    :Time: O(N)
    :Space: O(N)
    :return: root of resulting tree
    """
    if lo > hi:
        return None
    mid = (lo + hi) // 2
    root = TreeNode(A[mid])
    root.left, root.right = insert(A, lo, mid - 1), insert(A, mid + 1, hi)
    return root


if __name__ == '__main__':
    test1 = [-10, -3, 0, 5, 9]
    test2 = [-6, -2, -1, 1, 6, 21, 22]
    pretty_print_tree(sortedArrayToBST(test1))
