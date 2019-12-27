"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

@author a.k
"""
from data_structures.trees.BinaryTree import pretty_print_tree, TreeNode, BinaryTree


def sumOfLeftLeaves(root: TreeNode) -> int:
    return get_sum(root, is_left=False)


def get_sum(root: TreeNode, is_left: bool) -> int:
    """
    Returns the sum of left leaves of a tree using boolean flag, "is_left"
    :param root: root of tree
    :Time: O(N)
    :param is_left: whether the current node we are looking at is descendent from the left.
    :return: sum of left leaves
    """
    if not root:
        return 0
    if not root.left and not root.right and is_left:
        return root.key  # Left leaf
    return get_sum(root.left, is_left=True) + get_sum(root.right, is_left=False)


if __name__ == '__main__':
    test = BinaryTree.build([3, 9, 20, None, None, 15, 7])
    pretty_print_tree(test)
    print(sumOfLeftLeaves(test))
