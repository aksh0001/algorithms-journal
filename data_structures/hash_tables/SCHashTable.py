""" This module implements a Separate chaining hash table using a BST as the chained DS"""

from data_structures.hash_tables.MyBST import BST
from data_structures.hash_tables.referential_array import *


class HashTable:
    def __init__(self, init_size=31, b=31):
        """
        This constructor performs initialisation tasks
        :param init_size: the initial size of the table
        :raises ValueError: via build_array() if init_size is illegal
        """
        self.table = build_array(init_size)  # Array of BST references
        self.size = init_size
        # Fill array with BST references (an array of references)
        for i in range(self.size):
            self.table[i] = BST()

        self.count = 0
        self.base = b
        self.count_collisions = 0

    def __getitem__(self, key):
        """
        This method returns the corresponding value for the given key in the hash table. Equivalent to get()
        :param key: the key that corresponds to the value to get
        :raises KeyError: via BST get item if key does not exist in the table
        :Complexity: Average-case O(1)
        :return: the value corresponding to the key
        """
        hashed_idx = self.hash(key)
        return self.table[hashed_idx][key]  # Invokes the BST's get item

    def __setitem__(self, key, value):
        """
        This method inserts a value into the hash table associating with it a supplied key. Equivalent to put()
        :param key: key to be set
        :param value: value corresponding to the key to be set
        :Complexity: Average-case O(1)
        :return: void
        """
        # if self.count == self.size:  # For now, rehash only when full (better to keep it half empty always)
        #     self.rehash()
        hashed_idx = self.hash(key)
        if self.table[hashed_idx] is not None and self.table[
            hashed_idx].root is not None:  # Collision when we find that a root exists in that table spot
            self.count_collisions += 1
        self.table[hashed_idx][key] = value  # Insert via set item of BST
        self.count += 1

    def hash(self, key):
        """
        This method hashes the given key into an index into the table.
        :param key: the key to be hashed
        :return: an integer in the range [0, self.size-1] that represents an index in the table
        :Complexity: Constant-time O(1)
        """
        return self._hash_function(key) % self.size  # Modular hashing

    def __contains__(self, key):
        """
        This method returns a boolean indicating whether or not key exists in the table
        :param key: key to searched for in the table
        :Complexity: O(1)
        :return: T if exists, F otherwise
        """
        try:
            ret_val = self[key]
            return True
        except KeyError:  # get item throws KeyError if not found
            return False

    def _hash_function(self, key):
        """
        This method attempts to hash the key given into a unique integer. The integer is in the range [0, M-1]
        :param key: the key to be hashed
        :Complexity: O(k) where k is the length of the key
        :return: void
        """
        h = 0
        table_size = self.size
        for i in range(len(key)):
            h = (h * self.base + ord(key[i])) % table_size
        return h

    def get_total_collisions(self):
        """
        Accessor method that returns the total number of collisions that have been encountered
        :return: total collisions in self
        """
        return self.count_collisions


def read_into_table(fname, b=31, size=31):
    """
    This function reads the contents of the file fname into a hashtable.
    :param fname: the name of the file to be read
    :param b: the hash function parameter
    :param size: the initial size of the hashtable
    :pre-conditions: the file must be readable
    :Complexity: O(L) where L is the number of lines in the file -> Asssumes a perfect hash function O(1) insert
    :return: the hash table
    """
    assert file_readable(fname), "Error: File cannot be read"
    table = HashTable(size, b)
    with open(fname, 'r') as file:
        for line in file:
            table[line.strip("\n")] = 1
    return table


def file_readable(filepath):
    """
    Returns whether filepath is readable
    :param filepath:
    :return: whether the file is readable
    :Complexity: O(1)
    """
    try:
        f = open(filepath, 'r')
        f.close()
    except FileNotFoundError:
        return False

    return True


if __name__ == "__main__":
    pass
