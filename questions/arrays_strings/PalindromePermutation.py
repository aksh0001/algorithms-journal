"""
Given a string, write a function to check if it is a permutation of a palindrome.

E.g. "tactcoa" => True (permutation: "tacocat", "atcocta, etc.)

Approach: Simple arithmetic based on character occurrences

@author a.k
"""


def check(s: str) -> bool:
    """
    Returns true if s is a permutation of a palindrome.
    @Algorithm: Because we can permute the string in any way, we simply check if it has the same char occurrences
                needed to form a palindrome.
                Rule: If len is even, each char must have an even number of occurrences
                      If len is odd, each char but one, which is the pivot that must have 1 occurrence, must have an
                            even number of occurrences.
    :param s: string s
    :Time: O(n)
    :Space: O(n)
    :return: True if there is permutation of s that is a palindrome
    """
    occ = [0] * 128  # count occurrences of each char
    for c in s:
        occ[ord(c)] += 1

    # If s is of odd length, then there exists a middle pivot in a palindrome with a freq of 1
    # and the LH and RH side elements of the pivot each have even frequency
    if len(s) % 2 != 0:
        num_pivots = 0
        for o in occ:
            if o != 0:
                if o == 1:  # pivot character
                    num_pivots += 1
                elif o % 2 != 0:
                    return False
        return num_pivots == 1  # there must be only one pivot character (i.e. character of 1 occurrence)
    else:
        for o in occ:
            if o != 0:
                if o % 2 != 0:
                    return False
        return True


if __name__ == '__main__':
    tests = ["tactcoa", "aaaa", "rdaar", "abab", "aaabbb", "geeksforgeeks", "geeksogeeks"]
    ans = [True, True, True, True, False, False, True]
    for t, a in zip(tests, ans):
        assert check(t) == a, "Error!"
    print('PASSED')
