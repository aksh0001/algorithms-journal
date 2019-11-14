"""
Sort a list of numbers using trees in O(Nlog(N))
N.B. numbers must be unique since BSTs and AVL Trees by definition do not allow duplicates

Approach: - Construct AVL tree using list
          - Inorder traverse tree
@author a.k
"""
from typing import List
from data_structures.trees.AVLTree import AVLTree, TreeNode
from data_structures.trees.BinarySearchTree import BST
import random


def inorder(root: TreeNode) -> List:
    """
    Returns a list of keys in an inorder fashion.
    :param root: root of tree
    :return: inorder traversal list
    """
    if not root:
        return []
    else:
        return inorder(root.left) + [root.key] + inorder(root.right)


def naive(nums: List):
    """
    Naive TreeSort routine using BST
    :param nums: list of numbers
    :Time: O(N^2)
    :Space: O(N)
    :return: sorted list
    """
    bst = BST()
    for n in nums:
        bst.insert(n)
    # perform inorder
    return inorder(bst.root)


def tree_sort(nums: List):
    """
    Efficient tree sort routine using AVL Tree
    :param nums: list of numbers
    :Time: O(N*log(N))
    :Space: O(N)
    :return: sorted list
    """
    avl = AVLTree()
    for n in nums:
        avl.insert(n)
    # perform inorder
    return inorder(avl.root)


if __name__ == '__main__':
    for i in range(10):
        res = set([random.randrange(1, 50, 1) for _ in range(random.randint(0, 25 * i))])  # duplicates not alllowed!
        assert naive(list(res)) == sorted(res), 'ERROR: {}, {}'.format(i, res)
        assert tree_sort(list(res)) == sorted(res), 'ERROR: {}'.format(res)
    print('PASSED')
