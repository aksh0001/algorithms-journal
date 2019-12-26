"""
Return the root node of a binary search tree that matches the given preorder traversal.
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Approach: Min/Max interval tracking (same idea as validate bst question)

@author a.k
"""
from data_structures.trees.utils import pretty_print_tree, TreeNode
from typing import List


class Solution:
    def __init__(self):
        self.count = 0

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return self.construct(preorder)

    def construct(self, A: List[int], i=0, min=float('-inf'), max=float('+inf')) -> TreeNode:
        """
        Constructs a tree from preorder traversal and returns its root using Min/Max Interval tracking with count nodes.
        Algorithm:  Essentially we need to track whether the current node, A[i], is allowable in the current tree
                    by using min/max intervals.
                    If it is outside those bounds we can't include it in our tree.
                    If within bounds, since this is preorder traversal, we first recursively build the left subtree.
                    However, we soon realize the need for a self.count variable that will allow us to ascertain at which
                    point in the array we start to build our right subtree. Therefore we also track total nodes inserted.
                    Hence, by this logic, we recurisively build the left subtree along with tracking the total nodes
                    that have been inserted. Then, we know that the next element to look at to recursively build the
                    right subtree will be at the position self.count (now updated to the count of nodes in left subtree)
        :param A: preorder output
        :param i: element being considered
        :param min: minimum interval for element to be included
        :param max: maximum interval for element to be included
        :Time: O(N)
        :Space: O(N)
        :return:
        """
        # BC 1, 2: out-of-bounds of array and or current value being considered outside of min/max interval
        if i >= len(A) or A[i] > max or A[i] < min:
            return None
        root, self.count = TreeNode(A[i]), self.count + 1  # Create root and increment total nodes seen
        root.left = self.construct(A, i + 1, min, root.key)  # Recursively build and assign left subtree
        root.right = self.construct(A, self.count, root.key, max)  # Recurse to pos total nodes seen
        return root


if __name__ == '__main__':
    A = [8, 5, 1, 7, 10, 12]
    # A  = [1, 2, 3]
    pretty_print_tree(Solution().bstFromPreorder(A))
