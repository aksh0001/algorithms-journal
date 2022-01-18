"""
This module implements a hash table class with a linear probing collision resolution
"""
from data_structures.hash_tables.referential_array import build_array
from data_structures.hash_tables.referential_array import primes


class HashTable:
    def __init__(self, init_size=31):
        """
        This constructor performs initialisation tasks
        :param init_size: the initial size of the table
        :raises ValueError: via build_array() if init_size is illegal
        """
        self.keys = build_array(init_size)  # Parallel arrays - key[]
        self.values = build_array(init_size)  # Parallel arrays - values[]
        self.size = init_size
        self.count = 0
        # Task3 counters
        self.count_collisions = 0
        self.total_probe_length = 0
        self.count_rehashes = 0
        self.longest_probe_chain = 0

    def __str__(self):
        """
        This method represents a toString() version of the hash table data structure
        :return: a string formatted to display the underlying hash table neatly
        :Complexity: O(n)  where n is the length of the table
        """
        string = "| "
        for i in range(self.size):
            if self.keys[i] is None:
                pass
            else:
                string += str(i) + "(" + str(self.keys[i]) + ", " + str(self.values[i]) + ") "
        string += "|"
        return string

    def _linear_probe(self, key, operation):
        """
        This method returns the index corresponding to where the key-value pair can be inserted. Collision resolution
        is handled via linear probing. NOTE: If key already exists, then it returns its position (to overwrite it)
        :param key: the key to determine where to put a <Key-Value> pair
        :param operation: the operation (set/get) that has called this method -> useful for determining collisions
        :Complexity: Average case: O(1). Worst case: O(n) <-- highly unlikely as long as we maintain M > 2N
        where M is the table size and N is current number of <K,V> pairs in the table (ensure it is atleast 1/2 empty)
        :return: the index to put the item in
        """
        hashed_idx = self.hash(key)
        place_to_insert = hashed_idx
        if self.keys[place_to_insert] is None:
            return place_to_insert
        else:  # Find next empty spot (linear probing), while ensuring an already existing key has its value replaced
            # If the place to insert already contains the key, not a collision. only set() is relevant for collisions
            if self.keys[place_to_insert] != key and operation == "set":
                self.count_collisions += 1  # Increment total collisions
            probe_length = 0
            while self.keys[place_to_insert] is not None and self.keys[place_to_insert] != key:
                if operation == "set":
                    probe_length += 1  # Increment probe length
                place_to_insert = (place_to_insert + 1) % self.size  # Use modulo to wrap around if we get to the end
            if operation == "set":
                self.total_probe_length += probe_length  # Increment total probe length
                if self.longest_probe_chain < probe_length:  # If current longest < new probe length, update longest
                    self.longest_probe_chain = probe_length

        return place_to_insert

    def __getitem__(self, key):
        """
        This method returns the corresponding value for the given key in the hash table. Equivalent to get()
        :param key: the key that corresponds to the value to get
        :raises KeyError: if key does not exist in the table (i.e. the array of keys)
        :Complexity: Average-case O(1)
        :return: the value corresponding to the key
        """
        exists = self.keys[self._linear_probe(key, "get")] is not None  # _linear_probe() returns None if not found
        if not exists:
            raise KeyError("Error: " + str(key) + " does not exist in the table")
        else:
            location = self._linear_probe(key, "get")
            assert self.keys[location] == key, "Error in linear probing to get()"
            return self.values[location]

    def __setitem__(self, key, value):
        """
        This method inserts a value into the hash table associating with it a supplied key. Equivalent to put()
        :param key: key to be set
        :param value: value corresponding to the key to be set
        :Complexity: Average-case O(1)
        :return: void
        """
        if self.count == self.size:  # For now, rehash only when full (better to keep it half empty always)
            self.rehash()

        hashed_idx = self._linear_probe(key, "set")  # Get position to put. _probe() takes care of hashing the key
        if self.keys[hashed_idx] != key:  # If _probe() returns a spot that doesn't have this key, then increment count
            self.count += 1
        self.keys[hashed_idx] = key  # Store key in the keys array
        self.values[hashed_idx] = value  # Store value in the values array

    def hash(self, key):
        """
        This method hashes the given key into an index into the table.
        :param key: the key to be hashed
        :return: an integer in the range [0, self.size-1] that represents an index in the table
        :Complexity: Constant-time O(1)
        """
        return self._hash_function(key) % self.size  # Modular hashing

    def rehash(self):
        """
        This method resizes the current hash-table rehashes and reinserts all the current items into a new hashtable
        with the new capacity
        :raises ValueError: via _get_new_capacity()
        :Complexity: O(M) where M is the current table size
        :return: void
        """
        new_cap = self._get_new_capacity()  # Choose not to handle the ValueError thrown by _get_new_capacity()
        new_table = HashTable(new_cap)  # Create a new hash table directly
        for i in range(self.size):
            if self.keys[i] is not None:  # Only put() when there exists a key (no Nones)
                new_table[self.keys[i]] = self.values[i]  # Rehash and insert into the new table

        self.keys = new_table.keys  # Update instance variables
        self.values = new_table.values
        self.size = new_cap  # Update N
        self.count_rehashes += 1  # Increment total rehashes

    def _get_new_capacity(self):
        """
        This method returns a new capacity that is a prime number larger than twice the current size, N
        :raises ValueError: if there is no such prime in the list -> indicates the user wants too big a table
        :return: the new prime capacity
        """
        for prime in primes:
            if prime > 2 * self.size:
                return prime
        raise ValueError("Error: Table size overflow!")

    def __contains__(self, key):
        """
        This method returns a boolean indicating whether or not key exists in the table
        :param key: key to searched for in the table
        :Complexity: O(1)
        :return: T if exists, F otherwise
        """
        return self.keys[self._linear_probe(key, "contains")] is not None

    def _hash_function(self, key):
        """
        This method attempts to hash the key given into a unique integer. The integer is in the range [0, M-1]
        :param key: the key to be hashed
        :Complexity: O(k) where k is the length of the key
        :return: void
        """
        h = 0
        a = 31
        table_size = self.size
        for i in range(len(key)):
            h = (h * a + ord(key[i])) % table_size
        return h

    def get_total_collisions(self):
        """
        Accessor method that returns the total number of collisions that have been encountered
        :return: total collisions in self
        """
        return self.count_collisions

    def get_total_rehashes(self):
        """
        Accessor method that returns the total number of rehashes that has occurred
        :return: total number of rehashes
        """
        return self.count_rehashes

    def get_total_length_of_probe_chains(self):
        """
        Accessor method to get the total length of the probe chains
        :return: total length of the probe chains
        """
        return self.total_probe_length

    def get_longest_probe_chain(self):
        """
        Returns the length of the longest probe chain
        :return: length of the longest probe chain
        """
        return self.longest_probe_chain

    def delete(self, key):
        """
        This method deletes a <K,V> pair in the hash table given a key. Implements a non-lazy deletion.
        :param key: the key to be deleted
        :return: void
        :raises KeyError: via contains if key does not exist in the table
        :Complexity: O(M) worst case, M is the size of the table
        """
        if not self.__contains__(key):
            raise KeyError("Error: Key " + key + " does not exist!")  # Rethrow exception for documentation purposes

        hashed_idx = self._linear_probe(key, 'delete')
        # Clear the spot
        self.keys[hashed_idx] = None
        self.values[hashed_idx] = None
        # Rehash all keys in the same cluster
        start_rehash = (hashed_idx + 1) % self.size
        i = start_rehash
        while self.keys[i] is not None:
            # Save key and value to rehash
            key_to_rehash = self.keys[i]
            val_to_rehash = self.values[i]
            # Clear the spots and re-insert
            self.keys[i] = None
            self.values[i] = None
            self.count -= 1  # decrement count
            self[key_to_rehash] = val_to_rehash  # Simply put() it back into the table
            i = (i + 1) % self.size

        self.count -= 1  # Remember to decrement count again
