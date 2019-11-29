"""
You need to find the largest value in each row of a binary tree.
Example:
Input:

          1
         / \
        3   2
       / \   \
      5   3   9

Output: [1, 3, 9]

Approach: Simple BFS with level tracking

@author a.k
"""
from typing import List
from data_structures.trees.BinaryTree import TreeNode


def largest_values(root: TreeNode) -> List[int]:
    """
    Returns a list of the largest values at each level.
    Algorithm: BFS with level tracking. And using dict for mapping level to largest value.
    :param root: root of tree
    :Time: O(N)
    :Space: O(N)
    :return: list of largest values at each level
    """
    if not root:
        return []
    ret_val, bfs_queue = {}, [(root, 1)]
    while bfs_queue:
        removed, removed_level = bfs_queue.pop(0)
        if removed_level in ret_val:  # update maximum if already seen this level
            ret_val[removed_level] = max(removed.key, ret_val[removed_level])
        else:
            ret_val[removed_level] = removed.key  # if not seen this level, assign current max
        # Add children
        if removed.left:
            bfs_queue.append((removed.left, removed_level + 1))
        if removed.right:
            bfs_queue.append((removed.right, removed_level + 1))
    return list(ret_val.values())


if __name__ == '__main__':
    t, a = TreeNode(1), [1, 3, 9]
    t.left = TreeNode(3)
    t.right = TreeNode(2)
    t.left.left = TreeNode(5)
    t.left.right = TreeNode(3)
    t.right.right = TreeNode(9)
    assert largest_values(t) == a, 'ERROR'
    print('PASSED')
