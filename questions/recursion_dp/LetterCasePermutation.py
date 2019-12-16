"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]

Approach: Standard recursion approach

@author a.k
"""

from typing import List


def letter_case_permutation(S: str) -> List[str]:
    return get_permutations(S, len(S) - 1)


# Recursive function to get the permutations
def get_permutations(s: str, n: int) -> List[str]:
    """
    Returns all the letter case permutations of s.
    :param s: string to get permutations
    :param n: length of s
    :Time: O(2^n)
    :return: list of strings of letter case permutations
    """
    # BC: Empty string means no permutations
    if n < 0:
        return [""]
    rest_perms = get_permutations(s, n - 1)
    # RC1: If s[n] is a digit, leave as is and concat with result of s[n-1]
    if s[n].isdigit():
        return [p + s[n] for p in rest_perms]
    else:
        # RC2: If s[n] is a char, concat its upper and lower case versions with result of s[n-1]
        return [p + s[n].upper() for p in rest_perms] + [p + s[n].lower() for p in rest_perms]


if __name__ == '__main__':
    print(letter_case_permutation("a1b2"))
