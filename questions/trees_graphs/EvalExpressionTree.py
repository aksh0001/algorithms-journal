"""
Given a simple expression tree, consisting of basic binary operators i.e., + , – ,* and / and some integers,
evaluate the expression tree.

         (/)                -> (2*(3+(6/2)))/4 = 3
         / \
        /   \
      (*)   (4)
      / \
     /   \
   (2)   (+)
         / \
        /   \
      (3)   (/)
            / \
           /   \
         (6)   (2)

        (/)  --> 8/4 = 2
         / \
        /   \
      (8)   (4)

Ref: https://www.geeksforgeeks.org/evaluation-of-expression-tree/

@author a.k
"""
from data_structures.trees.BinaryTree import BinaryTree, TreeNode

OPERATORS = {'+', '-', '*', '/'}


def is_operator(c: chr):
    """
    Returns whether the character is an operator.
    :param c: char
    :return: true if supported operator
    """
    return c in OPERATORS


def calculate(a: int, operator: chr, b: int) -> int:
    """
    Utility function that calculates "a operator b".
    :param a: int 1
    :param operator: the operator to define the operation
    :param b: int 2
    :return: the result
    """
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '/':
        return a // b
    else:
        return a * b


def evaluate(root: TreeNode) -> int:
    """
    Evaluates the expression tree using post order processing
    :param root: root of tree
    :return: the result
    """
    # BC1: empty tree means nothing to do
    if not root:
        return None
    # BC2: if root is not an operator, i.e. just a value, then nothing to evaluate
    if not is_operator(root.key):
        return root.key
    else:
        # RC: root is an operator; get result of evaluation of the left and right subtree and operate on them
        return calculate(evaluate(root.left), root.key, evaluate(root.right))


if __name__ == '__main__':
    t1 = BinaryTree()
    t1.insert('/')
    t1.insert('*')
    t1.insert(4)
    t1.insert(2)
    t1.insert('+')
    t1.root.left.right.left = TreeNode(3)
    t1.root.left.right.right = TreeNode('/')
    t1.root.left.right.right.left = TreeNode(6)
    t1.root.left.right.right.right = TreeNode(2)
    print(evaluate(t1.root))

    t2 = BinaryTree()
    t2.insert('/')
    t2.insert(8)
    t2.insert(4)
    print(evaluate(t2.root))

    t3 = BinaryTree()
    t3.insert('+')
    t3.insert('*')
    t3.insert('-')
    t3.insert(5)
    t3.insert(4)
    t3.insert(100)
    t3.insert(20)
    print(evaluate(t3.root))

    t4 = BinaryTree()
    print(evaluate(t4.root))
