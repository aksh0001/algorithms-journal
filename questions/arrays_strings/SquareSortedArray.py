"""
Given an array of integers A sorted in non-decreasing order,
return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
"""
from typing import List


def naive(A: List[int]) -> List[int]:
    """
    Brute-force.
    :param A: List
    :Time: O(n*log(n))
    :Space: O(N)
    :return: sorted list of squares
    """
    return sorted([x ** 2 for x in A])


# Two-pointer approach
def sorted_squares(A: List[int]) -> List[int]:
    """
    Returns a list of sorted squares of the numbers.
    @Algorithm: motivation - elements toward the end should have larger squares, but not the case due to negative
                numbers since they could have larger squares. Therefore set up two pointers at the ends
                Choose the larger one and shift the pointer to compare to the next one.
                This works because we know the relative order of larger elements compared to the smaller ones.
    :param A: list of ints
    :Time: O(N)
    :Space: O(N)
    :return: sorted list of squared ints
    """
    i, j, k = 0, len(A) - 1, len(A) - 1
    ret_val = [0] * (len(A))
    while i <= j:
        if A[j] ** 2 > A[i] ** 2:
            ret_val[k] = A[j] ** 2
            j -= 1
        else:
            ret_val[k] = A[i] ** 2
            i += 1
        k -= 1
    return ret_val


if __name__ == '__main__':
    print('TESTING')
    print(naive([-4,-1,0,3,10]))
    print(sorted_squares([-4,-1,0,3,10]))
