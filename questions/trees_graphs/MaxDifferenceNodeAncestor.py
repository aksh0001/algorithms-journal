"""
Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)

Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation:
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

@author a.k
"""
from data_structures.trees.utils import pretty_print_tree, TreeNode

#TODO -- FINISH THIS OFF! A LOT TO EXPLORE!!

def maxAncestorDiff(root: TreeNode) -> int:
    return get_max_diff(root, "fuck")


def get_max_diff(root, curr):
    if not root.left and not root.right:  # BC with Leaf Node
        return abs(curr - root.key)
    this = abs(curr - root.key)  # Calculate 'V' value for this current node
    # Include/Exclude
    incl_left = incl_right = excl_left = excl_right = float('-inf')
    if root.left:
        incl_left, excl_left = get_max_diff(root.left, root.key), get_max_diff(root.left, curr)
    if root.right:
        incl_right, excl_right = get_max_diff(root.right, root.key), get_max_diff(root.right, curr)
    return max(max(incl_right, incl_left), max(excl_right, excl_left), this)


if __name__ == '__main__':
    t = TreeNode(8)
    t.left = TreeNode(3)
    t.right = TreeNode(10)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(6)
    t.right.right = TreeNode(14)
    t.left.right.left = TreeNode(4)
    t.left.right.right = TreeNode(7)
    t.right.right.left = TreeNode(13)
    pretty_print_tree(t)
    print(maxAncestorDiff(t))
