"""
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
The binary search tree is guaranteed to have unique values.

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15; Output: 32
Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10; Output: 23

@author a.k
"""
from data_structures.trees.BinarySearchTree import BST, TreeNode


def bst_rs(root: TreeNode, L: int, R: int) -> int:
    """
    Returns the range sum of this bst.
    @Algorithm:
            - Choose any traversal (e.g. post-order)
            - Recurse left 'n add, Recurse right 'n add, and add onto root iff root's val is within the range.
            - turn into 1-liner ;)
    :param root: root of tree
    :param L: left endpoint
    :param R: right endpoint
    :return: range sum within those endpoints.
    """
    # 1-liner post-order process
    return bst_rs(root.left, L, R) + bst_rs(root.right, L, R) + (root.key if L <= root.key <= R else 0) if root else 0


if __name__ == '__main__':
    test = BST()
    test.insert(10)
    test.insert(5)
    test.insert(15)
    test.insert(3)
    test.insert(7)
    test.insert(18)
    assert bst_rs(test.root, 7, 15) == 32, 'ERROR!'

    test = BST()
    test.insert(10)
    test.insert(5)
    test.insert(15)
    test.insert(3)
    test.insert(7)
    test.insert(13)
    test.insert(18)
    test.insert(1)
    test.insert(6)
    assert bst_rs(test.root, 6, 10) == 23, 'ERROR!'
    print('PASSED')
