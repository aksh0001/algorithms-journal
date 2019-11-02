"""
This module implements AVL self-balancing trees.


Note 1: There are two ways to implement this:
        1) This approach: track parents of nodes to make it easier to manipulate the tree (more space)
        2) Regular, standard return node recursive insertion approach
            See: https://www.geeksforgeeks.org/avl-tree-set-1-insertion/

Ref: https://rosettacode.org/wiki/AVL_tree#Java

@author a.k
"""
from data_structures.trees.BinarySearchTree import BST, TreeNode
from data_structures.trees.utils import pretty_print_tree


class AVLTreeNode(TreeNode):
    def __init__(self, key, val=None, bf=0):
        super().__init__(key, val)
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.parent = None  # Also track parent of this node for easier rotations
        self.bf = bf  # Balance factor of current node
        self.height = 1  # Height of subtree rooted at this node (this is important to update bf's after re-balancing)


class AVLTree(BST):
    def __init__(self):
        super().__init__()

    def insert(self, key, val=None):
        node = AVLTreeNode(key, val, bf=0)
        if self.root is None:
            self.root = node
            self.root.parent = None
        else:
            self._insert(self.root, node)
        self.n += 1

    def _insert(self, root: AVLTreeNode, node: AVLTreeNode):
        """
        Given an AVLTreeNode, inserts the node in the Tree rooted at "root" and also updates heights and balance
        factors of every node in the tree.
        :param root: root of AVL tree
        :param node: node to insert
        :Time: O(log(n))
        :Space: O(log(n)) stack space proportional to height
        :return: none
        """
        if not root:
            return
        if node.key < root.key:
            if root.left is None:
                root.left = node
                node.parent = root  # assign the parent to the node just inserted
            else:
                self._insert(root.left, node)  # insert and update heights and bf's of left subtree
        elif node.key > root.key:
            if root.right is None:
                root.right = node
                node.parent = root  # assign the parent to the node just inserted
            else:
                self._insert(root.right, node)  # insert and update heights and bf's of right subtree

        # update heights and bf's using postorder processing
        root.height = max(self._get_height(root.left), self._get_height(root.right)) + 1
        root.bf = abs(self._get_height(root.left) - self._get_height(root.right))

        self.rebalance(root)  # RE-BALANCE CURRENT ROOT IF REQUIRED

    def rebalance(self, root: AVLTreeNode):
        if root.bf == 2:
            if root.left.bf < 0:
                # double rotate r
                pass
            else:
                self.rotate_right(root)
        elif root.bf == -2:
            if root.left.bf > 0:
                # double rotate l
                pass
            else:
                self.rotate_left(root)

    def rotate_right(self, root: AVLTreeNode):
        """
        Performs a right rotation on the tree rooted at root.
        :param root: root of tree
        :Time: O(1)
        :Space: O(1)
        :return: none
        """
        pivot = root.left  # set up pointers
        tmp = pivot.right

        pivot.right = root  # reassign pivot's right child and update parent pointers as well
        pivot.parent = root.parent  # pivot's parent now root's parent
        root.parent = pivot  # root's parent now pivot

        root.left = tmp  # use saved right child of pivot and assign it to root's left and update its parent
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
        root.bf = abs(self._get_height(root.left) - self._get_height(root.right))
        pivot.height = max(self._get_height(pivot.left), self._get_height(pivot.right)) + 1
        pivot.bf = abs(self._get_height(pivot.left) - self._get_height(pivot.right))

    def rotate_left(self, root: AVLTreeNode):
        """
        Performs a left rotation on the tree rooted at root.
        :param root: root of tree
        :Time: O(1)
        :Space: O(1)
        :return: none
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
        root.bf = abs(self._get_height(root.left) - self._get_height(root.right))
        pivot.height = max(self._get_height(pivot.left), self._get_height(pivot.right)) + 1
        pivot.bf = abs(self._get_height(pivot.left) - self._get_height(pivot.right))

    def _get_height(self, root: AVLTreeNode) -> int:
        """
        Overridden to account for the fact that we are tracking heights during tree construction.
        :param root: root of subtree to which to get height for
        :return: height of tree rooted at root
        """
        if not root:
            return 0
        else:
            return root.height


if __name__ == '__main__':
    test = AVLTree()
    test.insert(13)
    test.insert(10)
    test.insert(15)
    test.insert(5)
    test.insert(11)
    test.insert(14)
    test.insert(16)
    test.insert(4)
    test.insert(6)
    test.insert(3)
    pretty_print_tree(test.root)
