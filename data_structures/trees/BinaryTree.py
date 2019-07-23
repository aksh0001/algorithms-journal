"""
This module implements Binary Trees.

@author a.k
"""
from data_structures.trees.utils import *


class TreeNode:
    def __init__(self, key, val=None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.n = 0  # total nodes in the tree

    def insert(self, key, val=None):
        node = TreeNode(key, val)
        if self.root is None:
            self.root = node
        else:
            self._insert(self.root, node)

    def _insert(self, root: TreeNode, node: TreeNode):
        """
        This helper inserts a node into a binary tree. Uses level-order traversal/bfs like algorithm to ensure balance.
        :param root: root of tree
        :param node: node to be inserted
        :return: none
        :Time: O(N)
        """
        # Initialise a queue and enqueue source node
        bfs_queue = Queue()
        bfs_queue.put(root)

        while not bfs_queue.empty():
            removed = bfs_queue.get()  # Dequeue from front

            # If removed node's left child is empty, insert there
            if removed.left is None:
                removed.left = node
                return
            else:  # If a left child exists, enqueue it
                bfs_queue.put(removed.left)

            # Similarly for the right child
            if removed.right is None:
                removed.right = node
                return
            else:
                bfs_queue.put(removed.right)

    def get(self, key: TreeNode.key) -> TreeNode:
        return self._get(self.root, key)

    def _get(self, root: TreeNode, key: TreeNode.key) -> TreeNode:
        if root.key == key:  # BC1 - found
            return root
        if root is None:  # BC2 - not found
            raise LookupError("Error! Key doesn't exist!")


if __name__ == "__main__":
    test = BinaryTree()
    for i in range(1, 11):
        test.insert(i)

    print_level_order(test.root)
    print("")
    print_post_order(test.root)
