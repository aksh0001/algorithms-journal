"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.

Approach: BFS

@author a.k
"""
from data_structures.trees.BinaryTree import TreeNode


def are_cousins(root: TreeNode, x: int, y: int) -> bool:
    """
    Returns whether the x and y are cousins in the tree.
    Algorithm: BFS with level tracking.
            - Essentially we make use of markers, parent of x & y and level of x & y, which we find from
                scanning the tree in level-order. Then use these markers to make a determination.
    :param root: root of tree
    :param x: node with key x
    :param y: node with key y
    :return: true if x and y are cousins.
    """
    if not root:
        return False
    x_par = x_lev = y_par = y_lev = None
    bfs_queue = [(root, 1)]
    while bfs_queue:
        removed, removed_level = bfs_queue.pop(0)
        if removed.left:
            bfs_queue.append((removed.left, removed_level + 1))
            if removed.left.key == x:
                x_par, x_lev = removed, removed_level + 1
            if removed.left.key == y:
                y_par, y_lev = removed, removed_level + 1
        if removed.right:
            bfs_queue.append((removed.right, removed_level + 1))
            if removed.right.key == x:
                x_par, x_lev = removed, removed_level + 1
            if removed.right.key == y:
                y_par, y_lev = removed, removed_level + 1
    return x_lev == y_lev and x_par != y_par  # true if same level and different parent


if __name__ == '__main__':
    t1, t2, t3, a1, a2, a3 = TreeNode(1), TreeNode(1), TreeNode(1), False, True, False
    t1.left = TreeNode(2); t1.right = TreeNode(3); t1.left.left = TreeNode(4)
    assert are_cousins(t1, 4, 3) == a1, 'ERROR!'
    t2.left = TreeNode(2); t2.right = TreeNode(3); t2.left.left = TreeNode(4); t2.right.right = TreeNode(5)
    assert are_cousins(t2, 5, 4) == a2, 'ERROR!'
    t3.left = TreeNode(2); t3.right = TreeNode(3); t3.left.left = TreeNode(4)
    assert are_cousins(t3, 2, 3) == a3, 'ERROR!'
    print('PASSED!')