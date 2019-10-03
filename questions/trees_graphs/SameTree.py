"""
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]
Output: true

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]
Output: false

@author a.k
"""
from data_structures.trees.BinarySearchTree import BST, TreeNode


def is_same_tree(t1: TreeNode, t2: TreeNode) -> bool:
    """
    Returns whether t1 and t2 are the same trees
    :param t1: tree 1
    :param t2: tree 2
    :Time: O(N)
    :Space: O(N) (best case O(log(n)) since num recursion stacks proportional to height)
    :return: whether they are the same
    """
    if t1 is None and t2 is None:  # both nulls are same
        return True
    elif t1 is None:  # if either one is null, not the same
        return False
    elif t2 is None:
        return False
    else:
        if t1.key != t2.key:  # if value mismatch not the same
            return False
        else:  # if value match check left and right
            return is_same_tree(t1.left, t2.left) and is_same_tree(t1.right, t2.right)


if __name__ == '__main__':
    t1 = BST()
    t2 = BST()
    for i in range(11):
        t1.insert(i)
        t2.insert(i)
    assert is_same_tree(t1.root, t2.root)

    t1.insert(66)
    assert not is_same_tree(t1.root, t2.root)

    t1 = BST()
    t2 = BST()
    t2.insert(44)
    assert not is_same_tree(t1.root, t2.root)

    t1 = BST()
    t2 = BST()
    assert is_same_tree(t1.root, t2.root)

    print('PASSED')
