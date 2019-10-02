"""
Given two binary trees and imagine that when you put one of them to cover the other;
some nodes of the two trees are overlapped while the others do not.
You need to merge them into a new binary tree.
The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of new tree.

Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7

@author a.k
"""
from data_structures.trees.BinarySearchTree import TreeNode


def merge_trees(t1: TreeNode, t2: TreeNode) -> TreeNode:
    """
    Merges t1 and t2 together and returns the root of resulting tree
    @Algorithm: Merge t2 onto t1
                - If both nodes exist add onto t1
                - If either node is None, return the other to indicate that's the root of the new tree
                - Recur on children and assign the new root of the children
    :param t1: tree 1
    :param t2: tree 2
    :Time: O(M) where M is the nodes in the smaller tree
    :Space: O(M) in case of skewed tree
    :return:
    """
    # Assume we can modify original
    # modify t1
    if t1 and t2:
        t1.val += t2.val
    elif t2 is None:
        return t1  # do nothing return back up to insert
    elif t1 is None:
        return t2  # return t2 (new root) back up to insert
    else:
        return None

    root_left = merge_trees(t1.left, t2.left)
    root_right = merge_trees(t1.right, t2.right)

    t1.left = root_left  # Set new left subtree root
    t1.right = root_right  # Set new right subtree root
    return t1


if __name__ == '__main__':
    print('PASSED LEETCODE TESTS')
