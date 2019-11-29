"""

@author a.k
"""
from typing import List


def naive(S: List, n: int, k):
    if k == 0:
        return True
    if n < 0:
        return False
    include = exclude = False
    if k - S[n] >= 0:  # Ensure that taking n'th item won't overfill
        include = naive(S, n - 1, k - S[n])
    exclude = naive(S, n - 1, k)
    return include or exclude


if __name__ == '__main__':
    print('Testing...')
    test = ([3, 34, 4, 12, 5, 2], 41)
    print(naive(test[0], 5, test[1]))
