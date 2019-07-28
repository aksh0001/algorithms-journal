"""
This module implements the solution to the happy number problem on leetcode
A happy number is a number defined by the following process: Starting with any positive integer,
replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1
(where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

@author a.k
"""


def is_happy(n: int) -> bool:
    """
    Returns whether the number, n, is happy or not.
    Algorithm: Track each sum_square_digits() computation. If a number is re-computed, then we know that
    no solution exists and the number is not happy.
    :param n: the number
    :Time: O(K), some unknown parameter, K TODO: Work out the complexity
    :Space: O(K)
    :return: True if happy; false, otherwise.
    """
    seen = {}
    computation = n
    while computation != 1:
        if computation in seen:  # Re-occurrence of a computation; no solution
            return False
        seen[computation] = True
        computation = sum_square_digits(computation)

    return True  # we have a happy number


def sum_square_digits(n):
    """
    A utility function to help sum the square of the digits.
    :param n: the number
    :Time: O(len(N))
    :Space: O(1)
    :return: sum of square of digits of n
    """
    result = 0
    for c in str(n):
        result += int(c) ** 2

    return result


if __name__ == "__main__":
    test_1 = [19, True]
    assert is_happy(test_1[0]), "Error!"

    test_2 = [4, False]
    assert not is_happy(test_2[0]), "Error!"
