"""
This module implements a prefix trie using an array of child references--instead of hash tables--as the underlying
data structure, to allow for string sorting.

Possible ways to index children:
1) Array of child pointers (quick to access, but high space requirement since a lot of None pointers exist)
2) Balanced BST for child pointers (minimal amount of space, but lookup time reduces since we need to search tree)
3) Hashtable for child pointers (minimal amount of space, quick to access, but less versatile--e.g. cannot sort)

Ref: https://www.youtube.com/watch?v=zIjfhVPRZCg
Ref: https://en.wikipedia.org/wiki/Trie
Ref: https://algs4.cs.princeton.edu/52trie/TrieST.java.html

@author a.k
"""
from typing import *

R = 128  # Extended ASCII


class TrieNode:
    """
    This class represents a trie node that contains two things:
    1) A value list for this node (assume duplicate keys with different values allowed; e.g. ('hi', 8), ('hi', 11)
    2) References to R child nodes as array(R = 256)indexed by the ascii value of a character
    NOTE: neither keys or characters are explicitly stored --> defined by the implicit ascii index of the reference
    Tracing a valid path in the trie corresponds to the key, and the node at the end of the path contains the value
    NOTE: An empty values list indicates an incomplete word, whereas a non-empty values indicates a complete word
    """

    def __init__(self):
        self.values = []  # Allow duplicate keys with different values, so we have an array of values
        self.children: List[TrieNode] = [None] * R  # References to child nodes

    def put_value(self, value):
        """
        This method takes in a value and adds it to the node's instance variable, values
        :param value: the value to be added
        """
        self.values.append(value)

    def get_values(self):
        """
        This method returns the values stored in this node
        :return: value stored in this node
        """
        return self.values


class Trie:
    def __init__(self):
        self.root = TrieNode()  # Empty root
        self.n = 0  # Total nodes

    def insert(self, key: str, value: Any):
        """
        Inserts the value in the trie with the insertion path traced by the key.
        :param key: key that acts as the trace of the insertion path
        :param value: value to be inserted
        :Time: O(k) where k is the length of the key
        :return: none
        """
        curr = self.root  # defines the starting point
        for c in key:
            index = ord(c)  # calculate the index of the insertion point
            if curr.children[index] is None:  # create node along insertion path if it doesn't exist
                curr.children[index] = TrieNode()
            curr = curr.children[index]  # move to the node containing c
        #  now curr refers to the last node along the insertion path; insert the value here
        curr.put_value(value)
        self.n += 1

    def get(self, key: str) -> List:
        """
        This method returns the value list associated with the given key.
        Duplicate keys can have different values; hence, we return a list of values
        :param key: the key that the path is traced from to get to the value
        :Time: O(k)
        :return: the values associated with the key if exists. If the key doesn't exist, an empty list
        """
        curr = self.root  # defines the starting point
        for c in key:
            index = ord(c)  # get index of path trace
            if curr.children[index] is None:  # if a node containing c doesn't exist, the key doesn't exist in the trie
                return []
            curr = curr.children[index]  # move to the node
        #  now curr refers to the last node along the trace; the value list will be located at this node
        return curr.get_values()

    def prefix_match(self, prefix: str) -> List[str]:
        """
        Solves the auto-complete/prefix matching problem. Given a prefix, returns all entries within the Trie
        that have a prefix that matches the input prefix
        :param prefix: prefix to match
        :Time: O(k) where k is the length of the prefix. Assume the DFS call to return all entries is constant.
        :Space: O(1)
        :return: a list of strings indicating matched prefixes
        N.B. the returned list includes matched entries not including the input prefix.
        E.g. if prefix is 'sh' and trie contains ['shot', 'short', 'sheep'], it will return, ['ot', 'ort, 'eep']
        """
        curr = self.root  # defines the starting point
        for c in prefix:
            index = ord(c)  # get index of path trace
            if curr.children[index] is None:  # if node containing c doesn't exist, then the prefix doesn't exist
                return []
            curr = curr.children[index]  # move to the node
        #  now curr refers to the last node along the trace; get all keys rooted at this node
        return self.get_all_keys(curr)

    def get_all_values(self, root: TrieNode) -> List:
        """
        Uses DFS (pre-order traversal) to return all the values from all nodes rooted at a particular node in the trie.
        :param root: a root in the Trie from which to get all the values from
        :Time: O(T) if we wish to get all the values from the main root
        :return: a list of all values
        """
        ret_val = []  # Empty list that we will populate with values
        if root.get_values() != []:  # if the current node has values (i.e. a complete node), populate in our list
            ret_val = ret_val + root.get_values()

        # Recurse on each existing child and populate values
        for child in root.children:
            if child:
                ret_val = ret_val + self.get_all_values(child)  # Recursively add on values returned from its children
        return ret_val

    def get_all_keys(self, root: TrieNode, curr: str = '') -> List[str]:
        """
        Using DFS (pre-order), retrieves/constructs the path represented by keys rooted at the given root.
        E.g. given root node is 's' and the trie contains, 'she', 'sheep', 'shop', it returns ['he', 'heep', 'hop']
        Algorithm: The state at a given node is defined by Two parameters:
                1) The node itself (to enable to recur to children)
                2) The current string being traced (doesn't include the starting node--see example in description)
            At each call, if the current node is a complete node, then we can use the current string being traced
            to append the result.
            We also need to recur on each of the current node's children and add each result to our key_list
        :param root: root from which to construct the key path
        :param curr: current path being traced
        :Time: O(T) if we are getting all keys from the root
        :return: a list of all constructed keys along explored paths
        """
        key_list = []  # Empty list for populating the actual string keys (e.g. 'she', 'shore', 'shot')
        if root.get_values() != []:  # if current node is a complete node, append the current string being built
            key_list.append(curr)
        for i in range(len(root.children)):
            if root.children[i]:
                result = self.get_all_keys(root.children[i], curr + chr(i))  # Recur on children, pass child's character
                key_list = key_list + result  # Concat our key_list with the result from the recursive call
        return key_list

    def get_size(self):
        """
        Returns the total number of nodes in the trie
        :return: total number of nodes
        """
        return self.n

    @staticmethod
    def build_trie(strings: List[str]):
        """
        Using a list of strings, build and returns a Trie.
        :param strings: list of strings to be inserted
        :Time: O(n*m) where n is the length of the list and m is the maximal string size
        :Space: O(n*m)
        :return: a prefix Trie containing the list of strings, with default values set to 1
        """
        ret_val = Trie()
        for string in strings:
            ret_val.insert(string, 1)
        return ret_val


if __name__ == '__main__':
    test = Trie()
    test.insert("by", 4)
    test.insert("the", 5)
    test.insert("sea", 6)
    test.insert("sells", 1)
    test.insert("shells", 3)
    test.insert("she", 0)
    test.insert("shore", 7)
    test.insert("shot", 69)
    test.insert("short", 1738)
    test.insert('shells', 44)
    test.insert('shells', 99)
    test.insert('by', 78)

    assert test.get('shells') == [3, 44, 99], 'Error!'
    assert test.get('the') == [5], 'Error!'
    assert test.get('by') == [4, 78], 'Error!'
    assert test.get('s') == [], 'Error!'
    assert test.get('k') == [], 'Error!'

    print(test.get_all_values(test.root))  # get all values from all existing nodes that are rooted at the main root
    assert len(test.get_all_values(test.root)) == test.get_size(), 'Error!'
    # print(test.get_all_values(test.root.children[ord('s')].children[ord('e')]))  # now get all from the root of 'se'
    # print(test.get_all_keys(test.root.children[ord('s')].children[ord('h')], code=ord('h')))

    print(test.prefix_match('sh'))
    print(test.prefix_match('s'))
    print(test.prefix_match('by'))

    print('PASSED')
