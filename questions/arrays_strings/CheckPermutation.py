"""
Module for checking if one string is a permutation of the other.
@author a.k
"""


def check_permutation_naive(a: str, b: str):
    """
    True if a is a permutation of string b
    :param a: string a
    :param b: string b
    :return: true if a is a permutation of b
    :Time: O(N*logN)
    """
    return sorted(a) == sorted(b)  # Sort & compare


def check_permutation(a: str, b: str):
    """
    True if a is a permutation of string b
    :param a: string a
    :param b: string b
    :return: true if a is a permutation of b
    :Time: O(N)
    :Space: O(N)
    """
    if len(a) != len(b):
        return False
    map_a = [0] * 256  # map_a[i] = number of occurrences of character i
    map_b = [0] * 256
    for c in a:
        map_a[ord(c)] += 1  # Increment occurrence
    for c in b:
        map_b[ord(c)] += 1

    return map_a == map_b  # Equality compare our "buckets"


if __name__ == "__main__":
    print(check_permutation("cabk", "abkc"))
