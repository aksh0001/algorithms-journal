"""
Given a string s1 and a string s2, write a snippet to say whether s2 is a rotation of s1?
(eg given s1 = ABCD and s2 = CDAB, return true, given s1 = ABCD, and s2 = ACBD , return false)

@author a.k
"""


def solution(s1: str, s2: str) -> bool:
    """
    Returns whether s2 is a rotation of s1 (using only one call to isSubstring()"
    @Algorithm: Idea is that if s2 is a rotation of s1, s2 must be a substring of s1 + s1
    E.g. A = "abcde", B = "cdeab": “abcdeabcde” (A + A)
                                     “cdeab” (B)
    :param s1: string 1
    :param s2: string 2
    :Time: O(N) + O(X) X = space complexity of "in" operator
    :Space: O(N) + O(X)
    :return:  whether s2 is a rotation of s1
    """
    if len(s1) != len(s2):  # if not the same length discard straightaway
        return False

    return s2 in s1 + s1  # concatenate s1 to itself and check if s2 is a substring of it


if __name__ == '__main__':
    test = [("ABCD", "CDAB", True), ("ABCD", "ACBD", False), ("erbottlewat", "waterbottle", True)]
    for t in test:
        assert solution(t[0], t[1]) == t[2], 'Error'
