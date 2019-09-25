"""
An edit between two strings is one of the following changes.
 - Add a character
 - Delete a character
 - Replace a character
Given two string s1 and s2, find if s1 can be converted to s2 with exactly one (or 0) edits.

Expected time complexity is O(m+n) where m and n are lengths of two strings

E.g. ("pale", "ple") -> True
     ("pales", "pale") -> True
     ("pale", "bale") -> True
     ("pale", "bake") -> False
     ("palace", "palace") -> True

Approaches: Modified Edit distance

@author a.k
"""


def one_away(s1: str, s2: str) -> bool:
    """
    Returns True if the two strings, s1 and s2, are one (or 0) edits away. Uses modified EDIT DISTANCE algorithm
    @Algorithm: - Try each operation, where each takes one edit
                - Therefore with no more edits remaining, we simply compare the rest of the strings for equality
    :param s1: string 1
    :param s2: string 2
    :Time: O(min(n,m)) equality comparison
    :Space: O(n + m) slicing TODO! simply equality compare the strings without slicing for O(1) space
    :return: True if one edit (or zero edits) away
    """
    i = len(s1) - 1
    j = len(s2) - 1
    while i >= 0 and j >= 0:
        # Equal
        if s1[i] == s2[j]:
            i -= 1
            j -= 1
        # Unequal
        else:
            # Substitution - check if s1[0..i-1] == s2[0..j-1]
            if s1[0:i] == s2[0:j]:
                return True
            # Addition - check if s1[0..i] == s2[0..j-1]
            if s1[0:i + 1] == s2[0:j]:
                return True
            # Deletion - check if s1[0..i-1] == s2[0..j]
            if s1[0: i] == s2[0:j + 1]:
                return True

            return False
    return True  # 0 edits away


if __name__ == '__main__':
    tests = [("pale", "ple"), ("pales", "pale"), ("pale", "bale"), ("pale", "bake"), ("palace", "palace"), ("ace", "a")]
    for t in tests:
        print(one_away(t[0], t[1]))
