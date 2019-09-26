"""
Contains deprecated/unoptimized code fragments.
"""
from data_structures.trees.utils import *


def delete(self, key):
    def delete_helper(root: TreeNode, key):
        if root is None:
            return None
        if key < root.key:  # First check to determine direction
            if root.left:
                if root.left.key == key:
                    # case 1 and 2
                    if root.left.left is None:
                        root.left = root.left.right
                    elif root.left.right is None:
                        root.left = root.left.left
                    else:  # case 3
                        inorder_successor = self.get_min_node(root.left.right)
                        root.left.key = inorder_successor.key  # copy key, val
                        root.left.val = inorder_successor.val
                        delete_helper(root.left.right, inorder_successor.key)  # delete inorder successor
                else:
                    delete_helper(root.left, key)
        elif key > root.key:  # same for right
            if root.right:
                if root.right.key == key:
                    # case 1 and 2
                    if root.right.right is None:
                        root.right = root.right.left
                    elif root.right.left is None:
                        root.right = root.right.right
                    else:  # case 3
                        inorder_successor = self.get_min_node(root.right.right)
                        root.right.key = inorder_successor.key  # copy key, val
                        root.right.val = inorder_successor.val
                        delete_helper(root.right.right, inorder_successor.key)  # delete inorder successor
                else:
                    delete_helper(root.right, key)
        else:  # if global root to be deleted: todo need to handle the same cases as above for the global root
            inorder_successor = self.get_min_node(root.right)
            root.key = inorder_successor.key  # copy key, val
            root.val = inorder_successor.val
            delete_helper(root.right, inorder_successor.key)  # delete inorder successor

    delete_helper(self.root, key)


if __name__ == '__main__':
    pass
