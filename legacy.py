"""
Contains deprecated/unoptimized code fragments.
"""
from data_structures.trees.BinarySearchTree import BST, TreeNode


# For binary tree deletion
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


# For "Parens" problem
# LEGACY code (first accepted solution)
def generate(n, open, closed, ans, curr):
    if open > n or closed > n:
        return
    if open == closed:  # must use open (using close will invalidate expression)
        generate(n, open + 1, closed, ans, curr + '(')
    elif open == n:  # must fill rest with remaining closed
        rest_closed = "".join([')'] * (n - closed))
        ans.append(curr + rest_closed)
        return
    else:
        generate(n, open + 1, closed, ans, curr + '(')
        generate(n, open, closed + 1, ans, curr + ')')


# For AVL Tree insertion
# Note how we calculate the balance factors during construction
# (i.e. increase if we insert left and decrease if we insert right)
# legacy implementation that doesn't track the height--which is important
class AVLTreeNode(TreeNode):
    def __init__(self, key, val=None, bf=0):
        super().__init__(key, val)
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.parent = None  # Also track parent of this node
        self.bf = bf  # Balance factor of current node


class AVLTree(BST):
    def __init__(self):
        super().__init__()

    def insert(self, key, val=None):
        node = AVLTreeNode(key, val, bf=0)
        if self.root is None:
            self.root = node
        else:
            self._insert(self.root, node)
        self.n += 1

    def _insert(self, root: AVLTreeNode, node: AVLTreeNode):
        """
        Given an AVLTreeNode, inserts the node in the Tree rooted at "root" and also updates balance
        factors of every node in the tree.
        :param root: root of AVL tree
        :param node: node to insert
        :Time: O(log(n))
        :Space: O(log(n)) stack space proportional to height
        :return: none
        """
        if not root:
            return
        if node.key < root.key:
            root.bf += 1  # increase root's bf to indicate it's left subtree will be lengthened
            if root.left is None:
                root.left = node
                node.parent = root  # assign the parent to the node just inserted
            else:
                self._insert(root.left, node)
        elif node.key > root.key:
            root.bf -= 1  # decrease root's bf to indicate it's right subtree will be lengthened
            if root.right is None:
                root.right = node
                node.parent = root  # assign the parent to the node just inserted
            else:
                self._insert(root.right, node)

        # RE-BALANCE CURRENT ROOT IF REQUIRED
        self.rebalance(root)

    def rebalance(self, root: AVLTreeNode):
        pass


# For MinStack problem - 99.50% on leetcode
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [None] * (2)  # stack itself
        self.cap = 2
        self.n = 0  # number of items in the stack (points to next empty item)
        self.min_stack = [float('inf')]  # *** tracks the current minimum; item at top = current min

    def push(self, x: int) -> None:
        if self.n == self.cap:
            self.resize(int(self.cap * 1.5))
        self.stack[self.n] = x
        self.n += 1
        # NOW DO THE MIN STACK CHECK!!
        # @ SREERAM!!! --> EVEN IF X = CURRENT MIN WE HAVE TO APPEND! - THINK OF DUPS!
        if x <= self.min_stack[-1]:  # If current item is smaller, push onto min_stack
            self.min_stack.append(x)
        # else, do nothing

    def pop(self) -> None:
        ret_val = self.stack[self.n - 1]
        self.stack[self.n - 1] = None  # prevent loitering
        self.n -= 1
        # MIN STACK CHECK - if item popped is the current min in min_stack, pop it also
        if ret_val == self.min_stack[-1]:
            self.min_stack.pop()
        return ret_val

    def top(self) -> int:
        return self.stack[self.n - 1]

    def getMin(self) -> int:
        # Return the top of the min_stack, which is the current minimum
        return self.min_stack[-1]

    def resize(self, new_cap):
        aux = [None] * new_cap
        for i in range(self.n):
            aux[i] = self.stack[i]
        self.stack = aux
        self.cap = new_cap


if __name__ == '__main__':
    pass
