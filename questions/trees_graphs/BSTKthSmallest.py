"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Approach: Inorder traversal

@author a.k
"""
from data_structures.trees.utils import pretty_print_tree, TreeNode


class Solution:
    def kth_smallest(self, root: TreeNode, k: int) -> int:
        """
        Returns the kth smallest node in a BST.
        :param root: root of tree
        :param k: number k
        :Time: O(H) H = height of tree
        :Space: O(H)
        :return: value of kth smallest node
        """
        self.count, self.result = 0, 0
        try:
            self.get_kth_smallest(root, k)
        except:
            return self.result

    def get_kth_smallest(self, root, k):
        """
        Assigns the kth smallest element's key to instance variable self.result by counting nodes.
        Algorithm: Essentially, the problem breaks down to finding the Kth node of the inorder traversal, *while* traversing the tree.
        :param root: root of tree
        :param k: number k
        :Time: O(H)
        :Space: O(H)
        :return: none
        """
        if root:
            self.get_kth_smallest(root.left, k)  # Inorder traversal (L, *, R)
            self.count += 1  # mark root as seen by incrementing total count
            if self.count == k:  # if count reaches k, assign the instance variable and exit
                self.result = root.key
                raise Exception()  # no need to continue
            self.get_kth_smallest(root.right, k)


if __name__ == '__main__':
    test = TreeNode(5)
    test.right = TreeNode(6)
    test.left = TreeNode(3)
    test.left.left = TreeNode(2)
    test.left.right = TreeNode(4)
    test.left.left.left = TreeNode(1)
    pretty_print_tree(test)
    assert Solution().kth_smallest(test, 4) == 4, 'ERROR'
    assert Solution().kth_smallest(test, 5) == 5, 'ERROR'
    assert Solution().kth_smallest(test, 6) == 6, 'ERROR'
    print('PASSED')
