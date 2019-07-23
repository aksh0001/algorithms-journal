"""
Contains simple Tree util functions

@author a.k
"""
from data_structures.trees.BinaryTree import TreeNode
from queue import Queue


def print_pre_order(root: TreeNode):
    """
    Prints a pre-order traversal of a binary tree: Root, Left, Right
    :param root: root of tree
    :return: none
    :Time: O(N)
    :Space: O(N) stack space due to recursion
    """
    if root is None:
        return

    print(root.key, end=" ")
    print_pre_order(root.left)
    print_pre_order(root.right)


def print_post_order(root: TreeNode):
    """
    Prints a post-order traversal of a binary tree: Left, Right, Root
    :param root: root of tree
    :return: none
    :Time: O(N)
    :Space: O(N) stack space due to recursion
    """
    if root is None:
        return

    print_post_order(root.left)
    print_post_order(root.right)
    print(root.key, end=" ")


def print_in_order(root: TreeNode):
    """
    Prints a in-order traversal of a binary tree: Left, Root, Right
    :param root: root of tree
    :return: none
    :Time: O(N)
    :Space: O(N) stack space due to recursion
    """
    if root is None:
        return

    print_in_order(root.left)
    print(root.key, end=" ")
    print_in_order(root.right)


def print_level_order(root: TreeNode):
    """
    Prints a level-order traversal of a binary tree, using BFS Algorithm.
    :param root: root of tree
    :return: none
    :Time: O(N)
    :Space: O(N)
    """
    # Initialize a marked[] array and mark source as visited -> not relevant
    # Create a queue and enqueue source node
    bfs_queue = Queue()
    bfs_queue.put(root)

    while not bfs_queue.empty():
        # Deque from the queue and print
        removed = bfs_queue.get()
        print(removed.key, end=" ")

        # Get all neighbors/adjacent nodes/vertices of the dequeued vertex and enqueue if not visited and mark it

        # In standard BFS, we push vertices adjacent to a node, which all exist in the adjacency list representation
        # Here, children may be non-existent so we must push only those children that exist
        if removed.left is not None:
            bfs_queue.put(removed.left)
        if removed.right is not None:
            bfs_queue.put(removed.right)
