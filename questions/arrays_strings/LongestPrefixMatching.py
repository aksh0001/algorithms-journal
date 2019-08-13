"""
Given a dictionary of words and an input string, find the longest prefix of the string
which is also a word in dictionary.

Let the dictionary contain the following words:
{are, area, base, cat, cater, children, basement}

Below are some input/output examples:
--------------------------------------
Input String            Output
--------------------------------------
caterer                 cater
basemexy                base
child                   < Empty >

Approach1: Naive/Brute-force
Approach2: Prefix Tries

@author.ak
"""
from typing import List
from data_structures.tries.PrefixTrie import Trie


def naive(s: str, dictionary: List) -> str:
    """
    Considers each prefix and checks if that exists in the dictionary, if so we take the max of the previous
    ret_val and the current prefix based on length.
    :param s: input string of length k
    :param dictionary: dictionary of words of size n with maximal word size m
    :Time: O(n*k^2) N.B. comparing length k prefix with length m word takes O(k) since we stop comparing after k chars
    :Space: O(1)
    :return: the longest matching prefix of s in the dictionary
    """
    ret_val = ""
    prefix = ''
    # Go through entire dictionary and continue to update our longest prefix found
    for c in s:  # O(k)
        prefix += c
        if prefix in dictionary:  # O(k*n) comparing largest prefix (which is length k) to a word (length m) takes O(k)
            ret_val = max(ret_val, prefix, key=len)
    return ret_val


def solution(s: str, dictionary: List[str]) -> str:
    """
    Uses a Prefix Trie to solve the longest prefix matching problem.
    Algorithm: Construct a Trie of all dictionary words; then, walk down the Trie using the input string.
                Each time we encounter a complete node, update our longest to reflect that we have seen a longer prefix.
                As soon as you encounter a None node, return whatever longest stores--which will either be the longest
                matching prefix or empty indicating no solution exists.
    Advantages:
                - Obviously better Time Complexity
                - Once Trie is constructed for a particular dictionary, different queries take
                  only O(k) time. Therefore, very optimal if you have a list of words to find the longest prefix from
                - Therefore, with a list of input queries, very optimal to use.
    Disadvantages:
                - Uses a lot more space; but trade-off is that future queries on same Trie are crazy fast
    :param s: input string of length k
    :param dictionary: dictionary of words of size n with maximal word size m
    :Time: O(n*m + k) for the first query; but, O(k) for every query thereafter if operating on same Trie/dictionary
    :Space: O(n*m) to store the Trie
    :return: the longest matching prefix of s in the dictionary
    """
    # Construct a Trie of all dictionary words -- O(n*m) todo: to avoid reconstructing, we use global - find better way
    global dict_trie
    if not dict_trie:
        dict_trie = Trie.build_trie(dictionary)
    longest = ''
    curr = dict_trie.root
    for i in range(len(s)):  # -- O(k)
        idx = ord(s[i])  # Get index of path trace
        if curr.children[idx] is None:  # If we can no longer match characters, return the longest that is stored
            return longest
        if curr.children[idx].get_values() != []:  # If we have reached a complete node, update longest
            longest = s[0:i + 1]
        curr = curr.children[idx]  # Move down Trie
    return longest


if __name__ == '__main__':
    d1 = ['are', 'area', 'base', 'cat', 'cater', 'children', 'basement']
    w1 = 'caterer'
    w2 = 'basemexy'
    w3 = 'child'
    w4 = 'area51'
    assert naive(w1, d1) == 'cater', 'Error!'
    assert naive(w2, d1) == 'base', 'Error!'
    assert naive(w3, d1) == '', 'Error!'
    assert naive(w4, d1) == 'area', 'Error!'

    dict_trie = None
    assert solution(w1, d1) == 'cater', 'Error!'  # As soon as the Trie is constructed, other queries are O(k) time
    dict_trie = Trie.build_trie(d1)
    assert solution(w2, d1) == 'base', 'Error!'
    assert solution(w3, d1) == '', 'Error!'
    assert solution(w4, d1) == 'area', 'Error!'

    print('PASSED')
