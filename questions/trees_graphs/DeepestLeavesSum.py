"""
Given a binary tree, return the sum of values of its deepest leaves.

Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Approaches: 1) BFS with level tracking; 2) DFS with height helper

@author a.k
"""
from data_structures.trees.BinaryTree import pretty_print_tree, TreeNode, BinaryTree


"""
@Algorithm: 2 passes
1'st pass: Get height of tree to mark this is the level we need the sum of
2'nd pass: DFS through the tree to find the dl sum at that deepest level
"""
class DFS:
    def height(self, root: TreeNode) -> int:
        """
        Returns the height of the tree used to get the deepest leaves sum
        :param root: root of tree
        :return: height of tree
        """
        return 0 if not root else max(self.height(root.left), self.height(root.right)) + 1

    def dfs(self, root: TreeNode) -> int:
        """
        Returns the dl sum using dfs.
        :param root: root of tree
        :Time: O(N)
        :return: dl sum
        """
        return self.dl_sum(root, 1, self.height(root))

    def dl_sum(self, root: TreeNode, curr_level: int, deepest_level: int) -> int:
        """
        Returns the deepest level sum using dfs
        :param root: root of tree
        :param curr_level: current level being considered
        :param deepest_level: the pre-calculated  deepest level from which to get the sum.
        :Time: O(N)
        :return: dl sum
        """
        if not root:  # Empty root has no sum
            return 0
        if curr_level == deepest_level:  # If we are on the deepest level return this sum
            return root.key
        return self.dl_sum(root.left, curr_level + 1, deepest_level) + self.dl_sum(root.right, curr_level + 1,
                                                                                   deepest_level)



"""
BFS with level tracking
Calculate sum at each level, assuming that this sum represents the deepest leaves sum
When we get to a new level, a deeper level, update the sum to reflect a deeper level
If on same level, increment sum
"""
class BFS:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        """
        Returns the dl sum of the tree.
        :param root: root of tree
        :Time: O(N)
        :Space: O(N)
        :return: dl sum
        """
        q, dl_sum, curr_level = [(root, 1)], 0, -1
        while q:
            rm, rm_level = q.pop(0)
            if rm_level != curr_level: # on a new deeper level, reset the sum and the current level
                dl_sum, curr_level = rm.key, rm_level
            else:
                dl_sum += rm.key  # If on the same level, simply accumulate the sum
            if rm.left:
                q.append((rm.left, rm_level+1))
            if rm.right:
                q.append((rm.right, rm_level+1))
        return dl_sum


if __name__ == '__main__':
    test = BinaryTree.build([1,2,3,4,5,None,6,7,None,None,None,None,8])
    assert DFS().dfs(test) == 15, 'ERROR'
    print('PASSED DFS')
    assert BFS().deepestLeavesSum(test) == 15, 'ERROR'
    print('PASSED BFS')