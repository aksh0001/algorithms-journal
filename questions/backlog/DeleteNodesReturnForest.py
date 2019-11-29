"""
TODO
"""
from typing import List

from data_structures.trees.BinaryTree import BinaryTree
from data_structures.trees.utils import *


def delNodes(root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
    forest = []
    parents_of_to_delete = []
    collect_nodes_to_delete(root, parents_of_to_delete, to_delete)
    # for each parent, do two things
    # add the children of the child that must be deleted into our forest;
    # and set the parents pointer to the child that must be deleted to None
    for parent in parents_of_to_delete:
        for delete in to_delete:
            if parent.left and parent.left.key == delete:
                # parent.left is the node to delete, add its children to the forest
                if parent.left.left:
                    forest.append(parent.left.left)
                if parent.left.right:
                    forest.append(parent.left.right)
            if parent.right and parent.right.key == delete:
                if parent.right.left:
                    forest.append(parent.right.left)
                if parent.right.right:
                    forest.append(parent.right.right)

    forest.append(root)
    # now set parent pointer to child to delete to none
    for parent in parents_of_to_delete:
        for delete in to_delete:
            if parent.left and parent.left.key == delete:
                parent.left = None
            if parent.right and parent.right.key == delete:
                parent.right = None
    return forest


def collect_nodes_to_delete(root: TreeNode, parents: List[TreeNode], to_delete: List[int]):
    # This function adds the parent node of a child that must be deleted
    if root is None:
        return
    if root.left:  # if root has a left child
        if root.left.key in to_delete:  # if left child is a node to be deleted, add parent
            parents.append(root)

        collect_nodes_to_delete(root.left, parents, to_delete)  # recur left

    if root.right:  # same for right
        if root.right.key in to_delete:
            parents.append(root)

        collect_nodes_to_delete(root.right, parents, to_delete)


if __name__ == '__main__':
    test = BinaryTree()
    for i in range(1, 8):
        test.insert(i)
    pretty_print_tree(test.root)

    delNodes(test.root, [3, 5])
