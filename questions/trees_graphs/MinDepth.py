"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

Approach: Simple get_height() function with customized min() function.

@author a.k
"""
from data_structures.trees.utils import TreeNode, pretty_print_tree


def min_depth(root: TreeNode) -> int:
    """
    Returns the minimum depth of a binary tree
    :param root: root of tree
    :Time: O(N)
    :Space: O(N)
    :return: minimum depth
    """
    if not root:
        return 0
    return min_tree_heights(min_depth(root.left), min_depth(root.right)) + 1


def min_tree_heights(t1_h: int, t2_h: int) -> int:
    """
    Given heights of two trees, returns the minimum height, but where an empty tree is considered invalid for this use case.
    :param t1_h: height of tree 1
    :param t2_h: height of tree 2
    :return: minimum of the tree heights
    """
    if not t1_h and not t2_h:
        return 0
    elif not t1_h:
        return t2_h
    elif not t2_h:
        return t1_h
    else:
        return min(t1_h, t2_h)


if __name__ == '__main__':
    t1 = TreeNode(3)
    t1.left = TreeNode(9)
    t1.right = TreeNode(20)
    t1.right.left = TreeNode(15)
    t1.right.right = TreeNode(7)
    pretty_print_tree(t1)
    print(min_depth(t1))
    assert min_depth(t1) == 2, 'ERROR'
    print('PASSED')
