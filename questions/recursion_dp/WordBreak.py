"""
Implements a naive and DP solution to the word break problem.
Given an input string and a dictionary of words, find out if the input string can be
segmented into a space-separated sequence of dictionary words.

FOLLOW-UP: Return the space-separated sequence of dictionary words

Q&a:
Q: What if there are multiple valid segmentations?
A: Just return any valid segmentation if there is one.

Ref: https://thenoisychannel.com/2011/08/08/retiring-a-great-interview-problem
Ref: https://www.geeksforgeeks.org/word-break-problem-dp-32/

@author a.k
"""
from typing import Dict, List
import time


class Naive:
    def __init__(self):
        pass

    def segment_string(self, s: str, dictionary: set):
        """
        Uses a naive recursive backtracking approach to return the segmented string (if possible), else None.
        Algorithm: Consider each prefix of the string s. As soon as a 'valid' prefix--i.e. a prefix that matches
                    a dictionary word--is found, recursively segment the suffix. If the result of the recursively
                    segmented suffix is not None, combine it with the prefix with a ' ' whitespace character.
                    Else, the suffix is not segmentable and hence the entire string is not segmentable; return None.
        :param s: string to be segmented
        :param dictionary: dictionary of allowed words
        :Time: O(2^N)
        :Space: O(2^N)
        :return: a space-separated sequence of dictionary words
        """
        # First check if s is itself a dictionary word - special case
        if s in dictionary:
            return s
        if s is None or s == '':
            return None

        for i in range(1, len(s)):
            prefix = s[0:i]  # Consider prefixes
            if prefix in dictionary:  # If prefix is valid, then we have a chance to successfully segment the suffix
                suffix = s[i:len(s)]
                segmented_suffix = self.segment_string(suffix, dictionary)  # Recursively segment suffix
                if segmented_suffix is not None:  # If suffix successfully segmented, combine with prefix and return
                    return prefix + ' ' + segmented_suffix
        return None  # Not segmentable

    def segmentable(self, s: str, dictionary: set) -> bool:
        """
        Returns whether the string is segmentable. see above algorithm
        :param s: string to check if segmentable
        :param dictionary: dictionary of allowed words
        :Time: O(2^N)
        :Space: O(2^N)
        :return: true if it can be segmented
        """
        if s in dictionary:
            return True
        if s is None or s == '':
            return False

        for i in range(1, len(s)):
            prefix = s[0:i]  # Consider prefixes
            if prefix in dictionary:  # If prefix is valid, then we have a chance to successfully segment the suffix
                suffix = s[i:len(s)]
                segmented_suffix = self.segment_string(suffix, dictionary)  # Recursively segment suffix
                if segmented_suffix:  # If suffix successfully segmented, entire string is segmentable bc prefix & suffix are both segmentable
                    return True
        return False  # Not segmentable


class Solution:
    def __init__(self):
        pass

    def segment_string(self, s: str, dictionary: set, memo: Dict[str, str]):
        """
        This time we memoize repeated subproblems to avoid re-computation.
        Naive solution has exponential runtime. Consider the string 'aaab' and dictionary=['a','aa','aaa'] to see why.
        -Also notice the repeated subproblem calculations in the example.
        :param s: string to be segmented
        :param dictionary: dictionary of allowed words
        :param memo: dict that stores subsolutions; memo[s]=ss; the solution for string 's' is 'ss'.
        :Time: O(N^2)
        :Space: O(N^2)
        :return: a space-separated sequence of dictionary words
        """
        if s in dictionary:
            return s
        if s is None or s == '':
            return None
        if s in memo:  # If problem s is solved, retrieve the solution
            return memo[s]

        for i in range(1, len(s)):
            prefix = s[0:i]
            if prefix in dictionary:
                suffix = s[i:len(s)]
                segmented_suffix = self.segment_string(suffix, dictionary, memo)
                if segmented_suffix is not None:
                    solution = prefix + ' ' + segmented_suffix
                    memo[s] = solution
                    return solution
        memo[s] = None
        return memo[s]


if __name__ == '__main__':
    print('Testing...')
    dictionaries = [{'apple', 'pie', 'app'},
                    {'i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream', 'icecream', 'man', 'go', 'mango'},
                    {"cats", "dog", "sand", "and", "cat"}]
    tests = [('applepie', dictionaries[0]), ('ilike', dictionaries[1]), ('ilikesamsung', dictionaries[1]),
             ('goicesamman', dictionaries[1]), ('samsung', dictionaries[1]), (None, dictionaries[1]),
             ('banana', dictionaries[0]), ("catsandog", dictionaries[2])]

    naive = Naive()
    sol = Solution()
    for t in tests:
        print(naive.segmentable(t[0], t[1]), end=" | naive: ")
        print(naive.segment_string(t[0], t[1]), end=" | solution: ")
        print(sol.segment_string(t[0], t[1], {}))
        print(" ")

    stress = 'aaaaaaaaaaaaaaaaaaaab'  # to try all combinations, append an invalid token at the end, 'b'
    dictionary = {'a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa'}
    t1 = time.time()
    print(naive.segment_string(stress, dictionary))
    t2 = time.time()
    print(sol.segment_string(stress, dictionary, {}))
    t3 = time.time()

    print('Stress Test:\n Naive = ', t2 - t1, '\n DP = ', t3 - t2)
    print(sol.segment_string('aaaab', {'a', 'aa', 'aaa', 'aaaa'}, {}))
