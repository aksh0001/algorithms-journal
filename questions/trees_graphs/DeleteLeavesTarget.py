"""
Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if it's parent node becomes a leaf node and has the value
target, it should also be deleted (you need to continue doing that until you can't).

Approach: Postorder pruning

@author a.k
"""
from data_structures.trees.BinaryTree import TreeNode


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        # This is essentially pruning, where nodes are deleted on a condition, but also the resulting
        # parents are removed if they also meet this condition
        # pruning amounts to POSTORDER traversal
        # RR: Prune left and right; if root matches condition remove the root
        if not root:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        return None if root.val == target and not root.left and not root.right else root
