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


def pretty_print_tree(root):
    """
    This function pretty prints a binary tree
    :param root: root of tree
    :return: none
    """
    lines, _, _, _ = _pretty_print_tree(root)
    for line in lines:
        print(line)


def _pretty_print_tree(root):
    """
    Code credits: Stack overflow
    :param root: root of tree
    :return: none
    """
    if root.right is None and root.left is None:
        line = '%s' % root.key
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if root.right is None:
        lines, n, p, x = _pretty_print_tree(root.left)
        s = '%s' % root.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if root.left is None:
        lines, n, p, x = _pretty_print_tree(root.right)
        s = '%s' % root.key
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _pretty_print_tree(root.left)
    right, m, q, y = _pretty_print_tree(root.right)
    s = '%s' % root.key
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2
