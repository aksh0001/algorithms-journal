"""
Given an integer x, find square root of it. If x is not a perfect square, then return floor(√x).
You cannot use in-built function.

Approaches: 1) Naive O(√x) 2) BinarySearch (log(x))
"""


def naive(x: int) -> int:
    """
    Naive solution: try numbers starting from 1, until the square of the number becomes >= x.
    Check if the number we've stopped at is the number itself. If  so, we have found a perfect square-return it.
    Else, return that number - 1 since we need to find the floor of it.
    :param x: the value
    :Time: O(√x)
    :Space: O(1)
    :return: sqrt(x)
    """
    # base cases
    if x == 0 or x == 1:
        return x

    i = 1
    result = i ** 2
    while result <= x:
        i += 1
        result = i ** 2

    if result == x:
        return i
    else:
        return i - 1


if __name__ == '__main__':
    tests = [(4, 2), (1, 1), (0, 0), (81, 9), (25, 5), (100, 10)]
    for t in tests:
        assert naive(t[0]) == t[1], 'Error!'
