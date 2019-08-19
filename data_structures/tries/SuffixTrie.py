"""
This module implements suffix trees (non-compressed) using prefix tries.

Important note: A substring of s is always a prefix of some suffix of s.

Possible ways to build a suffix trie:
1) Naive: Consider all suffixes and insert into the tree  O(N^2) time
2) Ukkonen's algorithm: O(N) time
Alternate: Convert from suffix array

Note: Since each suffix of a string of length N has length O(N), and each insert takes O(N) space,
      the non-compressed version takes O(N^2) space. Compressed suffix tries (or suffix trees) take O(N) space.
      Achieving O(N) space requires compressing the trie into a tree, but also requires referring to each substring
      by its position in the original string-->e.g. "na$" in "banana$" would be represented as [3,4]
"""
from data_structures.tries.PrefixTrie import Trie


class SuffixTrie(Trie):
    def __init__(self, s: str):
        Trie.__init__(self)
        self.naive_construction(s)

    def pattern_matching(self, pattern: str) -> bool:
        return self.prefix_match(pattern) != []

    def naive_construction(self, s: str):
        """
        Constructs a suffix trie using all suffixes of string s.
        :param s: string to build suffix trie on
        :Time: O(N^2)--each suffix has length O(N) and takes O(N) to insert
        :Space: O(N^2)--we are using non-compressed suffix tries
        :return: none
        """
        suffix = ""
        for i in range(len(s) - 1, -1, -1):
            suffix = s[i] + suffix  # order of concatenation matters
            self.insert(suffix, 1)  # the key, 1, marks a complete node/suffix


if __name__ == "__main__":
    test = SuffixTrie("banana")
    print(test.get_all_keys(test.root))
    print(test.pattern_matching("banana"))
