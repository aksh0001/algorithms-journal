"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

See for Visual Representation: https://media.geeksforgeeks.org/wp-content/uploads/Diameter-of-Binary-Tree.png

@author a.k
"""
from data_structures.trees.BinaryTree import pretty_print_tree, TreeNode, BinaryTree
from typing import Tuple

"Here's how the Algorithm goes..." \
"We essentially have to bring in the concept of depth (or height) into this problem to express the diameter" \
"Assuming the diameter of a tree, T, goes through the root, the diameter can be expressed as:" \
"d(root) = depth(root.left) + depth(root.right). However, the diameter of the tree **DOESN'T** have to go through the root," \
"meaning we should recurse to the left and right subtrees to get the diameter of those subtrees and choose the maximum." \
"Here's the recurrence:" \
">>>>>d(root) = max(depth(root.left)+depth(root.right), d(root.left), d(root.right))<<<<<" \
"Essentially, this is saying we take the max of the diameter going through the root and the diameter of its" \
"left and right subtrees"


def diameter_of_bt(root: TreeNode) -> int:
    """
    Returns the diameter of the bt.
    :param root: root of tree
    :Time: O(N)
    :return: diameter of tree
    """
    return get_diameter(root)[0]


# Quite easy--relies on calculating the depth of two subtrees at each level
# diameter(root) = max(depth(left)+depth(right), diameter(root.left), diameter(root.right))
def get_diameter(root: TreeNode) -> Tuple['Diameter', 'Depth']:
    """
    Returns a tuple[diameter, depth] of the tree.
    :param root: root of tree
    :Time: O(N)
    :return: tuple[diameter, depth]
    """
    if not root:
        return 0, 0  # 0 diameter and 0 depth
    l_diam_dep, r_diam_dep = get_diameter(root.left), get_diameter(root.right)
    return max(l_diam_dep[1] + r_diam_dep[1], l_diam_dep[0], r_diam_dep[0]), max(l_diam_dep[1], r_diam_dep[1]) + 1


if __name__ == '__main__':
    test = BinaryTree.build([1, 1, 1, 1, 1, None, 1, None, None, 1, 1, None, 1, None, None, None, None, 1, 1, None, 1])
    pretty_print_tree(test)
    assert diameter_of_bt(test) == 8
    print('\n\n')
    test = BinaryTree.build(
        ([1, 1, 1, 1, 1, None, None, 1, 1, None, 1, None, None, 1, None, 1, 1, None, 1, None, None, 1, None, None]))
    pretty_print_tree(test)
    assert diameter_of_bt(test) == 8
    print('PASSED')