"""
Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must **ALSO** be binary search trees.

2 Approaches: 1) Continuous tracking of min and max 2) Inorder sorting check

@author a.k
"""
from data_structures.trees.BinaryTree import BinaryTree, TreeNode
from data_structures.trees.BinarySearchTree import BST
import random
from typing import List


def trap(root: TreeNode) -> bool:
    """
    Simply, but WRONG!: For all nodes simply check if left child is smaller and the right child is larger
    :param root: root of tree
    :return: incorrectly returns whether the tree is a BST.
    """
    # BC: empty tree is a BST
    if not root:
        return True
    # Check if left is smaller and right is larger
    if (root.left and root.left.key >= root.key) or (root.right and root.right.key <= root.key):
        return False  # not a BST
    else:
        return trap(root.left) and trap(root.right)  # check left and right subtrees


class Approach1:
    def validate_using_inorder(self, root: TreeNode) -> bool:
        """
        Recollect that TreeSort is a sorting routine that traverses a BST inorder to sort an array.
        Therefore, simply traverse the tree inorder and verify that the output is sorted!
        :param root: root of tree
        :Time: O(N)
        :Space: O(N)
        :return: whether it is a BST
        """
        return self.is_sorted(self.inorder(root))

    def is_sorted(self, a: List) -> bool:
        """
        Checks if the array is sorted.
        :return: if a is sorted
        """
        for i in range(len(a) - 1):
            if a[i + 1] <= a[i]:  # Note the "<=" since BSTs have unique elements!
                return False
        return True

    def inorder(self, root) -> List:
        """
        Returns a list of keys in an inorder fashion.
        :param root: root of tree
        :return: inorder traversal list
        """
        if not root:
            return []
        else:
            return self.inorder(root.left) + [root.key] + self.inorder(root.right)


def validate_bst(root: TreeNode) -> bool:
    """
    CONTINUOUS TRACKING OF MIN/MAX INTERVAL:
    :param root: root of tree
    :Time: O(N)
    :Space: O(N)
    :return: whether it is a BST
    """

    def validate(root: TreeNode, curr_min, curr_max):
        """
        Returns whether the tree at root is a valid BST bounded by lower and upper intervals, curr_min & curr_max.
        Algorithm: Instead of comparing root with children values, compare with L-R intervals.
                - If current root is within the interval check left and right
                    - recur on left while updating upper interval to current root's key (ensure nothing bigger than it)
                    - recur on right while updating lower interval to current root's key (ensure everything bigger than it)
                    - if both the left and right subtrees are valid, then entire tree is valid
                - else, not valid
        :param root: root of tree
        :param curr_min:
        :param curr_max:
        :return: whether tree is a BST.
        """
        if not root:  # BC: empty tree is valid
            return True
        if curr_min < root.key < curr_max:  # recur left and right and update intervals accordingly
            return validate(root.left, curr_min, root.key) and validate(root.right, root.key, curr_max)
        else:
            return False  # not valid

    return validate(root, float('-inf'), float('+inf'))


if __name__ == '__main__':
    test1, test2, test3, test4 = BinaryTree(), BinaryTree(), BinaryTree(), BST()
    test1.insert(2)
    test1.insert(1)
    test1.insert(3)
    test2.insert(6)
    test2.insert(4)
    test2.insert(9)
    test2.insert(2)
    test2.insert(8)
    test2.insert(7)
    for i in range(50):
        test4.insert(random.randint(-i, i ** 2))

    assert trap(test1.root), 'ERROR!'  # passes as expected
    # assert not trap(test2.root), 'ERROR!'  # FAIL - NOT A BST!

    assert Approach1().validate_using_inorder(test1.root), 'ERROR!'
    assert not Approach1().validate_using_inorder(test2.root), 'ERROR!'
    assert Approach1().validate_using_inorder(test3.root), 'ERROR!'
    assert Approach1().validate_using_inorder(test4.root), 'ERROR!'

    assert validate_bst(test1.root), 'ERROR!'
    assert not validate_bst(test2.root), 'ERROR!'
    assert validate_bst(test3.root), 'ERROR!'
    assert validate_bst(test4.root), 'ERROR!'
    print('PASSED!')
