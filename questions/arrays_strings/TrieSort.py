"""
Implements string sorting using Tries.

Standard merge sort: O(n*log(n)*m) m for the string comparison
Trie sort: O(n*m)
Alternate: radix string sort: O(n*m)

@author a.k
"""
from typing import List
from data_structures.tries.PrefixTrie import Trie


def standard(strings: List[str]):
    """
    Sorts strings using standard built-in function
    :param strings: string list to sort
    :Time: O(n*log(n)*m) where n is the length of the list and m is the maximal word size
    :return: sorted string list
    """
    return sorted(strings)


def trie_sort(strings: List[str]):
    """
    Sorts list of strings by using a Prefix Trie.
    Algorithm: First construct a trie using the list of strings O(n*m) time and space
                Pre-order traverse the trie from the root and append key trace of all complete nodes. O(n*m)
    :param strings: string list to sort
    :Time: O(n*m)
    :Space: O(n*m)
    :return: sorted string list
    """
    trie = Trie.build_trie(strings)
    sorted_list = trie.get_all_keys(trie.root)
    return sorted_list


if __name__ == '__main__':
    test = ['app', 'apple', 'banana', 'c', 'b', 'carrot', 'car', 'dog', 'door']
    assert standard(test) == trie_sort(test)
    print('PASSED')
