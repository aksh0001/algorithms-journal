"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

@author a.k
"""
from data_structures.trees.BinaryTree import TreeNode
from data_structures.trees.utils import pretty_print_tree


def flatten_suboptimal(root: TreeNode):
    """
    Flattens tree in-place.
    Idea: Recursively flatten left subtree and right subtree.
         Get tail of left subtree (now a linked list).
         Repoint root.right to root.left and point the left tail's right to root.right
    :param root: root of tree
    :return: none
    """
    if root:
        flatten_suboptimal(root.left)
        flatten_suboptimal(root.right)
        left_tail = root.left
        while left_tail and left_tail.right:
            left_tail = left_tail.right
        if left_tail:
            left_tail.right = root.right
            root.right, root.left = root.left, None


previous = None


def flatten_tree(root: TreeNode):
    """
    Flattens tree using reverse post-order traversal.
    :param root: root of tree
    :Time: O(N)
    :return: none
    """
    global previous  # Tracks the previously seen node to avoid a linear pass through the left list!
    if root:
        flatten_tree(root.right)
        flatten_tree(root.left)
        root.right = previous  # Set right subtree to previously seen node
        root.left = None
        previous = root  # Update previous


if __name__ == '__main__':
    test = TreeNode(1)
    test.left = TreeNode(2)
    test.right = TreeNode(5)
    test.left.left = TreeNode(3)
    test.left.right = TreeNode(4)
    test.right.right = TreeNode(6)

    pretty_print_tree(test)
    flatten_tree(test)
    pretty_print_tree(test)
