"""
Two elements of a binary search tree (BST) are swapped by mistake. Recover the tree without changing its structure.

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
-------

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?

Approach: Inorder traversal

@author a.k
"""
from data_structures.trees.utils import pretty_print_tree, TreeNode
from typing import List


def recoverTree(root: TreeNode) -> None:
    """
    In-place algorithm to recover the tree based on inorder traversal.
    Algorithm: Output the inorder traversal, which will be unsorted, output the two elements that have been swapped
                in the inorder traversal and reassign these elements in the tree. Quite straightforward but not optimal.
    :param root: root of tree
    :Time: O(N)
    :Space: O(N)
    :return: none
    """
    v1, v2 = get_swapped_elements(tree_sort(root))
    recover(root, v1, v2)


def get_swapped_elements(A):
    """
    Analyzes the unsorted array, A,  and returns the two swapped elements in A that violate the sorted property.
    :param A: unsorted array A.
    :Time: O(N)
    :Space: O(1)
    :return: two elements that have been swapped
    """
    i, j = 0, len(A) - 1
    while i < len(A) - 1 and A[i] <= A[i + 1]:
        i += 1
    v1 = A[i]  # get first violation
    while j > i and A[j] >= A[j - 1]:
        j -= 1
    v2 = A[j]
    return v1, v2


# Inorder traversal to get sorted array
def tree_sort(root) -> List[int]:
    """
    Returns sorted array based on inorder traversal.
    :param root: root of tree
    :Time: O(N)
    :return: sorted list
    """
    if not root:
        return []
    return tree_sort(root.left) + [root.key] + tree_sort(root.right)


# Swaps elements by reassigning nodes
def recover(root, v1, v2):
    """
    Recovers tree by reassigning nodes u, v with value v1, v2 such that u.val = v2 and v.val = v1.
    :param root: root of tree
    :param v1: value 1
    :param v2: value 2
    :Time: O(N)
    :return: none, inorder swap
    """
    if root:
        if root.key == v1:
            root.key = v2
        elif root.key == v2:
            root.key = v1
        recover(root.left, v1, v2)
        recover(root.right, v1, v2)


if __name__ == '__main__':
    test = TreeNode(3)
    test.left = TreeNode(1)
    test.right = TreeNode(4)
    test.right.left = TreeNode(2)
    pretty_print_tree(test)
    recoverTree(test)
    print('--RECOVERED--')
    pretty_print_tree(test)
