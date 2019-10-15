"""
Invert a binary tree.
Input:
     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:
     4
   /   \
  7     2
 / \   / \
9   6 3   1

@author a.k
"""
from data_structures.trees.BinarySearchTree import TreeNode, BST


def invert(root: TreeNode) -> TreeNode:
    """
    Inverts a binary tree.
    N.b. can be done using preorder and postorder processing (not inorder).
    :param root: root of tree
    :Time: O(N)
    :Space: O(N)
    :return: root of new tree
    """
    if not root:
        return None

    invert(root.left)
    invert(root.right)
    root.left, root.right = root.right, root.left  # postorder process
    return root
