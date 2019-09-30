"""
A permutation, also called an “arrangement number” or “order,” is a rearrangement of the elements of an ordered list S
into a one-to-one correspondence with S itself. A string of length n has n! permutation.
Below are the permutations of string ABC.
ABC ACB BAC BCA CBA CAB.

Given a unique string return all its possible permutations.

N.B. approaches will be different depending on subproblem configuration
Approaches: 1) "Fix and recur" approach; 2) "Mad Insert" approach

@author a.k
"""
from math import factorial
from typing import List


def solution(s: str) -> List[str]:
    """
    Straightforward way to return all permutations of a string.
    @Algorithm:  Consider fixing each character, c of s, as the first character.
                - Recursively get all permutations of the rest of the string
                - Prepending the fixed char onto each of the above permutations will give you
                    all the permutations of s starting with that fixed char
                - Therefore, if we repeat this, trying to fix all characters of s as the first character,
                    and adding each result to our answer will give us all permutations of s.
    :param s: string to get permutations of
    :Time: O(n*n!) todo: check and find space (and use indices instead of slicing!)
    :Space: O(X)
    :return:
    """
    if len(s) == 0:
        return [""]
    ret_val = []
    for i in range(len(s)):
        s = swap(s, 0, i)  # "try" each char as the first character
        fix = s[0]  # fix the first character
        more_perms = solution(s[1:])  # recur on the rest
        ret_val += [fix + perm for perm in more_perms]  # prepend the fixed char onto each permutation and add to result
    return ret_val


def swap(s: str, i: int, j: int):
    """
    Strings are, unfortunately, immutable in python. Hence, this swaps the two chars of s and returns a new string
    with the swapped values
    :param s: string s
    :param i: index i to be swapped with j
    :param j: index j to be swapped with i
    :return: new string with swapped values
    """
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)


class StringPermutations:
    # This class uses an alternate approach to finding string permutations
    def get_permutations(self, s: str) -> List[str]:
        """
        Returns all permutations of s.
        :param s: string s
        :return: all permutations of s.
        """
        return self.permute(s, len(s) - 1)

    def permute(self, s: str, n: int) -> List[str]:
        """
        Returns all permutations of s using simply alternate algorithm
        @Algorithm: We can get P(s[0..n]) using subproblem P(s[0..n-1]) by the following:
                    - Using P(s[0..n-1]), for perm in that result set, insert s[n] at every location in that perm
                    - At the end, our result set will have P(s[0..n]) -- EASY!!
        :param s: string s
        :param n: length of string; pointer to indicate where we are in the string
        :Time: O(n*n!)?
        :Space: O(X)
        :return: all perms of s
        """
        if n < 0:
            return [""]
        else:
            ret_val = []
            more_permutations = self.permute(s, n - 1)  # get P(s[0..n-1])
            for perm in more_permutations:  # go through each perm
                for i in range(n + 1):  # Insert s[n] at each position of each perm and append to answer
                    ret_val.append(StringPermutations.insert_character(perm, i, s[n]))
            return ret_val

    @staticmethod
    def insert_character(s: str, i: int, c: chr):
        """
        This method is for inserting char, c, at index, i, into string s.
        :param s: string s
        :param i: index to insert c
        :param c: char to be inserted
        :return: new string containing the above modification
        """
        if i == len(s):
            return s + c
        aux = ""
        for j in range(len(s)):
            if j == i:
                aux += c
            aux += s[j]
        return aux


class IntegerPermutations:
    # This class uses the alternate approach for string permutations on a list of integers
    def get_permutations(self, nums: List[int]) -> List[List[int]]:
        return self.permute_ints(nums, len(nums) - 1)

    def permute_ints(self, nums, n):
        if n < 0:
            return [[]]
        else:
            ret_val = []
            more_permutations = self.permute_ints(nums, n - 1)
            for p in more_permutations:
                for i in range(n + 1):
                    ret_val.append(p[:i] + [nums[n]] + p[i:])
            return ret_val


if __name__ == '__main__':
    sp = StringPermutations()
    assert len(sp.get_permutations('ABC')) == factorial(3), 'ERROR'  # no. permutations = n!
    assert len(sp.get_permutations('ABCD')) == factorial(4), 'ERROR'
    assert len(sp.get_permutations('ABCDE')) == factorial(5), 'ERROR'
    print('PASSED ALTERNATE')
    assert len(solution('ABC')) == factorial(3), 'ERROR'  # no. permutations = n!
    assert len(solution('ABCD')) == factorial(4), 'ERROR'
    assert len(solution('ABCDE')) == factorial(5), 'ERROR'
    print('PASSED SOLUTION')
