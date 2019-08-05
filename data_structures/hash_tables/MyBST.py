""" This module implements a binary search tree for use in the linked DS for separate chaining collision handling"""


class BST:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None  # Left subtree link
            self.right = None  # Right subtree link

    def __init__(self):
        self.root = None  # Initialise an empty BST (root is the access point of this data structure)

    def __setitem__(self, key, value):
        if self.root is None:
            self.root = self.Node(key, value)
        else:
            self.put_aux(key, value, self.root)

    def put_aux(self, key, value, node):
        """
        This auxiliary method defines inserting items into a BST. The implemented pattern does not require returning
        any node references. It simply uses a bit of logic to avoid this.
        :param key: the key to be inserted
        :param value: the value to be inserted
        :param node: the root node
        :return: void
        :Complexity: O(log(n))
        """
        if key < node.key:  # Look LEFT
            if node.left is None:  # Tada -> this is the place to insert
                node.left = self.Node(key, value)
            else:
                self.put_aux(key, value, node.left)  # Insert/Recurse into left subtree
        elif key > node.key:  # Look RIGHT
            if node.right is None:
                node.right = self.Node(key, value)
            else:
                self.put_aux(key, value, node.right)  # Insert/Recurse into right subtree

        else:  # If keys are equal, simply update existing <KV> pair!
            node.key = key
            node.value = value

    def __getitem__(self, key):
        return self.get_aux(key, self.root)

    def get_aux(self, key, node):
        # BC/Handling case: none Node -> signifies that the key does NOT exist (think about it)
        if node is None:
            # raise KeyError("Error: " + str(key) + " is not found!!!") TODO uncomment this, will return none for simplicity
            return None

        # BC: found key
        if node.key == key:
            return node.value

        # RCs: look at left and right trees
        if key < node.key:
            return self.get_aux(key, node.left)  # return the found item which exists in left tree
        elif key > node.key:
            return self.get_aux(key, node.right)  # return the found item which exists in right tree

    def __len__(self):
        return self.count_aux(self.root)

    def count_aux(self, node):
        """
        TODO: Not counting the root
        :param node:
        :return:
        """
        if node is None:
            return 0
        # RCs
        left_subtree_count = 0
        right_subtree_count = 0
        if node.left is not None:  # I.e. there exists a left subtree
            left_subtree_count = 1 + self.count_aux(
                node.left)  # Count left subtree (define the problem in terms of ITSELF!)

        if node.right is not None:  # I.e. there exists a right subtree
            right_subtree_count = 1 + self.count_aux(node.right)  # Count right subtree

        return left_subtree_count + right_subtree_count


if __name__ == "__main__":
    print("Quick tests")
    B = BST()
    B[0] = "hello"
    assert B[0] == "hello"
    print(1, len(B))
    B[5] = "there"
    assert B[5] == 'there'
    print(2, len(B))
    B[5] = "world"
    assert B[5] == 'world'
    print(2, len(B))
    B[3] = "thing beneath world"
    assert B[3] == "thing beneath world"
    B[-5] = "left of root"

    assert B[-5] == "left of root"
    print(B[-5], "should be left of root")

#    print(99999 in B)
