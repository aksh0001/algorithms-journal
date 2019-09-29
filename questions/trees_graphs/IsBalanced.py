"""
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
    3
   / \
  9  20
    /  \
   15   7
Return true.

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

REF: https://www.afternerd.com/blog/python-check-tree-balanced/

@author a.k
"""
from data_structures.trees.BinaryTree import BinaryTree
from data_structures.trees.utils import *
from data_structures.trees.BinarySearchTree import BST


def naive(root: TreeNode) -> bool:
    """
    Returns whether the tree rooted at root is height-balanced.
    @Algorithm
                - At each level, validate the heights of every node's left and right subtrees
                - If the absolute difference between the heights exceeds 1, then not balanced
                - Return true IFF both the left and right subtrees are height-balanced
    :param root: root of tree
    :Time: O(N^2) worst case if skewed tree (Average case O(N*log(N))
    :Space: O(N)
    :return: true if height balanced
    """
    if not root:
        return True
    else:
        # At each node validate the absolute difference in heights of the left and right subtrees
        if abs(get_height(root.left) - get_height(root.right)) > 1:
            return False

        left_is_balanced = naive(root.left)
        right_is_balanced = naive(root.right)
        return left_is_balanced and right_is_balanced


def get_height(root: TreeNode) -> int:
    """
    Returns the height of the tree rooted at root.
    Uses post-order traversal: Use the results of the height of left and right subtrees to process the root
    :param root: root of tree
    :Time: O(N)
    :Space O(N)
    :return: height of tree
    """
    if not root:
        return 0
    else:
        return max(get_height(root.left), get_height(root.right)) + 1


def is_balanced(root: TreeNode) -> bool:
    """
    Returns whether the tree rooted at root is height-balanced.
    @Algorithm: uses the helper function, which only works on balanced trees, and otherwise raises an error, to
                determine if tree is height balanced. In a nutshell, as soon as you calculate heights of left
                and right subtrees, if unbalanced immediately return to the main call stack to indicate so.
                We do all the work--getting height and balance check--within one function.
                Side Note: We are still adhering to singe responsibility principle.
    :param root: root of tree
    :Time: O(N)
    :Space: O(N)
    :return: true if height balanced
    """
    try:
        get_balanced_height(root)
        return True  # If no error raised, then height-balanced
    except AssertionError:
        return False  # If error raised, not height-balanced


def get_balanced_height(root: TreeNode) -> int:
    """
    Returns the height of a balanced binary tree. If tree is NOT BALANCED, raises an exception.
    :param root: root of tree
    :Time: O(N)
    :Space: O(N)
    :raises AssertionError if tree is unbalanced
    :return: the height of a balanced binary tree
    """
    if not root:
        return 0

    left_subtree_height = get_balanced_height(root.left)
    right_subtree_height = get_balanced_height(root.right)
    # Immediately check for balance and throw exception if unbalanced
    if abs(left_subtree_height - right_subtree_height) > 1:
        raise AssertionError('ERROR - Tree is not height-balanced!!!')
    else:
        return max(left_subtree_height, right_subtree_height) + 1  # else normally return the height combined with root


if __name__ == '__main__':
    test = BinaryTree()
    for i in range(10):
        test.insert(i)
    assert naive(test.root) and is_balanced(test.root), 'ERROR!!'
    test = BST()
    for i in range(10):
        test.insert(i)
    assert not naive(test.root) and not is_balanced(test.root), 'ERROR!!'

    test = BST()
    test.insert(3)
    test.insert(20)
    test.insert(27)
    test.insert(15)
    test.insert(1)
    assert naive(test.root) and is_balanced(test.root), 'ERROR!'

    test = BST()
    test.insert(4)
    test.insert(3)
    test.insert(2)
    test.insert(1)
    test.insert(3.5)
    test.insert(2.5)
    assert not naive(test.root) and not is_balanced(test.root), 'ERROR!!'

    test = BST()
    test.insert(10)
    test.insert(9)
    test.insert(8)
    test.insert(20)
    test.insert(30)
    test.insert(40)
    assert not naive(test.root) and not is_balanced(test.root), 'ERROR!!'

    print('PASSED!')
