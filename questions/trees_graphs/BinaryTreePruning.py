"""
We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.
Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

Example 1:
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]
Example 2: (good example)
Input: [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]

@author a.k
"""
from data_structures.trees.BinaryTree import TreeNode
from data_structures.trees.utils import pretty_print_tree


def prune_tree(root: TreeNode) -> TreeNode:
    """
    Returns a pruned tree. Essentially removing all leaf nodes with value 0.
    :param root: root of tree
    :Time: O(N)
    :Space: O(N)
    :return: root of resulting tree
    """
    if not root:  # BC: If empty tree nothing to prune
        return None
    root.left, root.right = prune_tree(root.left), prune_tree(root.right)  # prune left and right
    if root.key == 0 and (not root.left and not root.right):
        return None  # If root is a leaf node with value 0, remove it
    else:
        return root


if __name__ == '__main__':
    t = TreeNode(1)
    t.left = TreeNode(0)
    t.right = TreeNode(1)
    t.left.left = TreeNode(0)
    t.left.right = TreeNode(0)
    t.right.left = TreeNode(0)
    t.right.right = TreeNode(1)
    pretty_print_tree(t)
    pretty_print_tree(prune_tree(t))
