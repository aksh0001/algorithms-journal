"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.
Input: [1,7,0,7,-8,null,null]
Output: 2
Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

Approach: BFS with level tracking

@author a.k
"""
from data_structures.trees.utils import pretty_print_tree, TreeNode


def max_level_sum(root: TreeNode) -> int:
    """
    Returns the max level sum of a binary tree using BFS with level tracking.
    :param root: root of tree
    :Time: O(N)
    :Space: O(N)
    :return: max level sum
    """
    max_sum = curr_sum = (0, 1)  # var format: (sum, level)
    # BFS with level tracking
    q = [(root, 1)]
    while q:
        rm_node, rm_level = q.pop(0)
        if rm_level != curr_sum[1]:  # we are on a new level
            max_sum = max(max_sum, curr_sum, key=lambda x: x[0])  # update max after finish level
            curr_sum = (rm_node.key, rm_level)  # reset current sum
        else:
            curr_sum = (curr_sum[0] + rm_node.key, rm_level)  # Increment sum if on same level

        if rm_node.left:
            q.append((rm_node.left, rm_level + 1))  # Add children and increment their level
        if rm_node.right:
            q.append((rm_node.right, rm_level + 1))

    return max_sum[1]


if __name__ == '__main__':
    test = TreeNode(1)
    test.left = TreeNode(7)
    test.right = TreeNode(0)
    test.left.left = TreeNode(7)
    test.left.right = TreeNode(-8)
    assert max_level_sum(test) == 2, 'ERROR'
    print('PASSED')
