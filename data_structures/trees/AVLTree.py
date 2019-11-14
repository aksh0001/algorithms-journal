"""
This module implements AVL self-balancing trees.


Note 1: There are two ways to implement this:
        1) Track parents of nodes to make it easier to manipulate the tree (more space)
        2) Regular, standard return node recursive insertion approach
            See: https://www.geeksforgeeks.org/avl-tree-set-1-insertion/
We will follow the parent node and return node recursive insertion approach.

Ref: https://rosettacode.org/wiki/AVL_tree#Java

@author a.k
"""
from typing import List

from data_structures.trees.BinarySearchTree import BST, TreeNode


class AVLTreeNode(TreeNode):
    def __init__(self, key, val=None, bf=0):
        super().__init__(key, val)
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.parent = None  # Also track parent of this node for easier rotations
        self.bf = bf  # Balance factor of current node
        self.height = 1  # Height of tree rooted at this node (this is important to update bf's after re-balancing)


class AVLTree(BST):
    def __init__(self):
        super().__init__()

    def insert(self, key, val=None):
        """
        Public insert function to insert a node into an AVL Tree.
        :param key: key of node to be inserted
        :param val: corresponding value
        :Time: O(log(n))
        :Space: O(log(n))
        :return: none
        """
        self.root = self._insert(self.root, key, val)  # Returns root of resulting tree after insertion - update it
        self.n += 1

    def _insert(self, root: AVLTreeNode, key, val=None) -> AVLTreeNode:
        """
        Given an AVLTreeNode, inserts the node in the tree rooted at "root", updates heights and balance
        factors of affected nodes in the tree, and updates parent pointers; finally, returns root of resulting tree.
        :param root: root of AVL tree
        :param key: key of node to be inserted
        :param val: value of node to be inserted
        :Time: O(log(n))
        :Space: O(log(n)) stack space proportional to height
        :return: root of resulting tree after insertion
        """
        if not root:
            return AVLTreeNode(key, val, bf=0)  # If empty root this is the root of new tree
        if key < root.key:
            left_sub_root = self._insert(root.left, key, val)  # insert and update left subroot
            root.left = left_sub_root
            left_sub_root.parent = root  # assign the parent
        elif key > root.key:
            right_sub_root = self._insert(root.right, key, val)  # insert and update right subroot
            root.right = right_sub_root
            right_sub_root.parent = root
        else:
            return root  # no duplicate keys allowed; no insertion, return current root as is
        # finally, update heights and bf's of current root after insertion completed (postorder processing)
        root.height = max(self._get_height(root.left), self._get_height(root.right)) + 1
        root.bf = self._get_height(root.left) - self._get_height(root.right)
        return self.rebalance(root)  # RE-BALANCE CURRENT ROOT (if required)

    def rebalance(self, root: AVLTreeNode) -> AVLTreeNode:
        """
        Main rebalance routine to rebalance the tree rooted at root appropriately using rotations.
        4 cases:
        1) bf(root) = 2 and bf(root.left) < 0 ==> L-R Imbalance
        2) bf(root) = 2 ==> L-L Imbalance
        3) bf(root) = -2 and bf(root.right) > 0 ==> R-L Imbalance
        4) bf(root) = -2 ==> R-R Imbalance
        :param root: root of tree needing rebalancing.
        :return: root of resulting tree after rotations
        """
        if root.bf == 2:
            if root.left.bf < 0:  # L-R
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
            else:  # L-L
                return self.rotate_right(root)
        elif root.bf == -2:
            if root.right.bf > 0:  # R-L
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)
            else:  # R-R
                return self.rotate_left(root)
        else:
            return root  # no need to rebalance

    def rotate_right(self, root: AVLTreeNode) -> AVLTreeNode:
        """
        Performs a right rotation on the tree rooted at root, and returns root of resulting tree
        :param root: root of tree
        :Time: O(1)
        :Space: O(1)
        :return: root of updated tree
        """
        pivot = root.left  # set up pointers
        tmp = pivot.right
        # 1st Move: reassign pivot's right child to root and update parent pointers
        pivot.right = root
        pivot.parent = root.parent  # pivot's parent now root's parent
        root.parent = pivot  # root's parent now pivot
        # 2nd Move: use saved right child of pivot and assign it to root's left and update its parent
        root.left = tmp
        if tmp:  # tmp can be null
            tmp.parent = root

        # Not done yet - need to update pivot's parent (manually check which one matches the root that was passed)
        if pivot.parent:
            if pivot.parent.left == root:  # if the parent's left subtree is the one to be updated
                pivot.parent.left = pivot  # assign the pivot as the new child
            else:
                pivot.parent.right = pivot  # vice-versa for right child

        # Still not done :) -- update heights and bf's using tracked heights
        root.height = max(self._get_height(root.left), self._get_height(root.right)) + 1
        root.bf = self._get_height(root.left) - self._get_height(root.right)
        pivot.height = max(self._get_height(pivot.left), self._get_height(pivot.right)) + 1
        pivot.bf = self._get_height(pivot.left) - self._get_height(pivot.right)
        return pivot  # return root of new tree

    def rotate_left(self, root: AVLTreeNode) -> AVLTreeNode:
        """
        Performs a left rotation on the tree rooted at root, and returns root of resulting tree.
        :param root: root of tree
        :Time: O(1)
        :Space: O(1)
        :return: root of updated tree.
        """
        pivot = root.right
        tmp = pivot.left

        pivot.left = root
        pivot.parent = root.parent
        root.parent = pivot

        root.right = tmp
        if tmp:  # tmp can be null
            tmp.parent = root

        # Not done -- need to update pivot's parent as well
        if pivot.parent:
            if pivot.parent.left == root:  # if the parent's left subtree is the one to be updated
                pivot.parent.left = pivot  # assign the pivot as the new child
            else:
                pivot.parent.right = pivot  # vice-versa for right child
        # Still not done :) -- update heights and bf's using tracked heights
        root.height = max(self._get_height(root.left), self._get_height(root.right)) + 1
        root.bf = self._get_height(root.left) - self._get_height(root.right)
        pivot.height = max(self._get_height(pivot.left), self._get_height(pivot.right)) + 1
        pivot.bf = self._get_height(pivot.left) - self._get_height(pivot.right)
        return pivot  # return root of new tree

    def _get_height(self, root: AVLTreeNode) -> int:
        """
        Overridden to account for the fact that we are tracking heights during tree construction.
        :param root: root of subtree of which to get height for
        :return: height of tree rooted at root
        """
        if not root:  # empty tree means height of 0
            return 0
        else:
            return root.height  # return instance var height

    @staticmethod
    def burst_insert(a: List):
        """
        Inserts a list of n items into an AVL Tree and returns the root.
        :param a: list of items
        :Time: O(N*log(N))
        :Space: O(N)
        :return: tree root
        """
        root = AVLTree()
        for item in a:
            root.insert(item)
        return root


if __name__ == '__main__':
    print('SEE TESTING MODULE')
