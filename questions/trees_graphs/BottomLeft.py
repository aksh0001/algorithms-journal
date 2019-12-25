"""
Given a binary tree, find the leftmost value in the last row of the tree.
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7

Approach: BFS with level tracking (wow my first 100% time!!)

@author a.k
"""
from data_structures.trees.utils import pretty_print_tree, TreeNode


def find_bottom_left_value(root: TreeNode) -> int:
    """
    Returns the bottom left value in the last row using bfs with level track. 100% time!
    :param root: root of tree
    :Time: O(N)
    :Space: O(N)
    :return: bottom left value in last row
    """
    bleft = None  # Track the bottom left node; just use the last node removed in bfs when looking at a new level
    q, curr_level = [(root, 1)], -1
    while q:
        rm_node, rm_level = q.pop(0)
        if rm_level != curr_level:  # at start of new level, update bottom left var
            bleft = rm_node
            curr_level = rm_level  # set current level to the new one

        if rm_node.left:  # Add children
            q.append((rm_node.left, rm_level + 1))
        if rm_node.right:
            q.append((rm_node.right, rm_level + 1))
    return bleft.key


if __name__ == '__main__':
    test = TreeNode(1)
    test.left = TreeNode(2)
    test.right = TreeNode(3)
    test.left.left = TreeNode(4)
    test.right.left = TreeNode(5)
    test.right.right = TreeNode(6)
    test.right.left.left = TreeNode(7)
    pretty_print_tree(test)
    assert find_bottom_left_value(test) == 7
    print('PASSED')
