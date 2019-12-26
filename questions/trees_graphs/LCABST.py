"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
"""
from data_structures.trees.utils import pretty_print_tree, TreeNode


def lca(root: TreeNode, p: int, q: int) -> TreeNode:
    """
    LCA of p and q in BST.
    :param root: root of tree
    :param p: node p
    :param q: node q
    :Time: O(H) H = height of tree (avg = O(log(N))
    :Space: O(H)
    :return: lca of p and q
    """
    # BC1: If current root is itself p or q, then this is the lca by definition
    if root.key == p or root.key == q:
        return root
    # BC2: If root.val is in between [p, q] (or [q, p]) then this is the lca
    if p < root.key < q or q < root.key < p:
        return root
    # RC1: If both, p & q, are smaller than root, search left, else search right
    if p < root.key and q < root.key:
        return lca(root.left, p, q)
    else:
        return lca(root.right, p, q)


if __name__ == '__main__':
    test = TreeNode(6)
    test.left = TreeNode(2)
    test.right = TreeNode(8)
    test.left.left = TreeNode(0)
    test.left.right = TreeNode(4)
    test.right.left = TreeNode(7)
    test.right.right = TreeNode(9)
    test.left.right.left = TreeNode(3)
    test.left.right.right = TreeNode(5)

    pretty_print_tree(test)

    assert lca(test, 2, 8).key == 6
    assert lca(test, 2, 4).key == 2
    assert lca(test, 3, 0).key == 2
    print('PASSED')
