"""
Implement binary search.

@author a.k
"""
from typing import List


def search(A: List[int], target: int) -> int:
    """
    Givens a sorted list, A, returns the index of element target.
    :param A: list of numbers
    :param target: target element
    :Time: O(log(n))
    :return: index of target if exists.
    """
    l, r = 0, len(A) - 1
    while l <= r:  # while pointers do not cross. equalling is ok since they can converge on the same element!
        mid = (l + r) // 2
        if A[mid] == target:
            return mid
        elif target < A[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1


if __name__ == '__main__':
    assert search([-1, 0, 3, 5, 9, 12], target=9) == 4
    print('PASSED')
