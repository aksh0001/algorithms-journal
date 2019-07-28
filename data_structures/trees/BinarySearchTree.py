"""
This module implements Binary Search Trees

@author a.k
"""
from data_structures.trees.utils import *
from data_structures.trees.BinaryTree import TreeNode
import random


class BST:
    def __init__(self):
        self.root = None
        self.n = 0

    def insert(self, key, val=None):
        node = TreeNode(key, val)
        if self.root is None:
            self.root = node
        else:
            self._insert(self.root, node)
        self.n += 1

    def _insert(self, root: TreeNode, node: TreeNode):
        """
        Recursively inserts the passed in node into the BST.
        Clever Algorithm: First ascertain direction (l or r) to recur.
            Before recurring, check if we can insert directly in the ascertained direction by checking the child
            If a child in that direction does not exist, simply assign it there
            Else, recur in that direction
        :param root: root of bst
        :param node: node to insert
        :Time: O(log(n))
        :Space: O(log(n)) stack space
        :return: none
        """
        if root is None:
            return  # Could simply return/"rebound" the node parameter up the stack and assign where needed, or return

        if node.key < root.key:  # First check to determine direction: left
            if root.left is None:  # Second check to check if a left child doesn't exist
                root.left = node  # If it doesn't simply assign
            else:
                self._insert(root.left, node)  # Else, simply recur left

        if node.key > root.key:  # Similar for the right subtree
            if root.right is None:
                root.right = node
            else:
                self._insert(root.right, node)

    def get(self, key) -> TreeNode:
        ret_val = self._get(self.root, key)
        if ret_val is None:
            raise LookupError("Error! Key doesn't exist!")
        else:
            return ret_val

    def _get(self, root: TreeNode, key: TreeNode) -> TreeNode:
        """
        Helper get method that to get the node associated with key
        :param root: root of tree
        :param key: key to look for
        :return: None if not found, the node, otherwise
        :Time: O(log(N))
        :Space: O(log(N))
        """
        # Always do the edge-case check, which could raise an error, FIRST!!
        if root is None:  # BC2 - not found
            return None
        # BST-order traverse: examine root first, then recur left or recur right depending on key comparison
        if root.key == key:  # BC1 - found
            return root

        result_left_subtree = None
        result_right_subtree = None

        if key < root.key:
            result_left_subtree = self._get(root.left, key)
        elif key > root.key:
            result_right_subtree = self._get(root.right, key)

        if result_left_subtree is not None:
            return result_left_subtree
        elif result_right_subtree is not None:
            return result_right_subtree
        else:
            return None

    def contains(self, key) -> bool:
        """
        Returns whether the tree contains a given key, this time using level-order traversal (standard BFS)
        :param key: key to be checked
        :Time: O(log(n))
        :return: whether the tree contains the key
        """
        # BFS (level-order traversal) algorithm
        bfs_queue = Queue()
        bfs_queue.put(self.root)  # Enqueue source node and mark as visited

        while not bfs_queue.empty():
            removed = bfs_queue.get()  # Dequeue from front
            if removed.key == key:  # If the removed node matches, return
                return True
            # Add the removed vertex's adjacent unmarked nodes into the queue and mark them
            # But as in the standard BFS, we only add the adjacent vertices that exist (i.e. not None)
            # NOTE: THIS TIME WE ONLY ENQUEUE ONE CHILD BASED ON THE BST KEY COMPARISON!!!

            if key < removed.key and removed.left is not None:
                bfs_queue.put(removed.left)  # mark visited
            if key > removed.key and removed.right is not None:
                bfs_queue.put(removed.right)  # mark visited
        return False

    def get_height(self) -> int:
        return self._get_height(self.root)

    def _get_height(self, root) -> int:
        """
        Returns the height of the binary tree.
        Algorithm: max(recur left, recur right) + 1
        Explanation: The height of a binary tree that is rooted at a certain node is equal to the
        maximum of the heights of its left and right subtrees + 1 (take into account the root node)
        :param root: root of the tree
        :return: the height of the tree
        """
        # BC
        if root is None:
            return 0
        # Take the maximum of the height of the left subtree and the right subtree, and add 1 to the result
        height = max(self._get_height(root.left), self._get_height(root.right)) + 1
        return height

    def get_max(self):
        """
        This returns the maximum key in the BST
        Algorithm: If root is none, no solution. Else, traverse the right subtree like a linked list
        and return the right-most node
        :Time: O(N)
        :Space: O(1)
        :return: the maximum key in the tree
        """
        if self.root is None:  # BC1
            return float('-inf')

        current = self.root
        while current.right is not None:  # Traverse like a linked-list
            current = current.right

        return current.key

    def get_min(self):
        """
        This returns the minimum key in the BST
        Algorithm: If root is none, no solution. Else, traverse the left subtree like a linked list
        and return the left-most node
        :Time: O(N)
        :Space: O(1)
        :return: the minimum key in the tree
        """
        if self.root is None:  # BC1
            return float('+inf')

        current = self.root
        while current.left is not None:  # Traverse like a linked-list
            current = current.left

        return current.key


if __name__ == "__main__":
    test = BST()
    for i in range(1, 11):
        test.insert(int(random.random() * 100), i ** 2)
    pretty_print_tree(test.root)
    print("")
    print(test.get_max())
    print(test.get_min())
    print("")
    test = BST()
    for i in range(1, 11):
        test.insert(i, i ** 2)

    # print(test.get(11))
    print(test.get(10).val)
    # print(test.contains(19))
    print(test.contains(3))
    print(test.get_max())
