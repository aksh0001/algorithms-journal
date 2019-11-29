"""
Given an integer array A, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
E.g.
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow-Up: Return the subarray that contains this max sum

TODO: REF: https://www.youtube.com/watch?v=2MmGzdiKR9Y https://en.wikipedia.org/wiki/Maximum_subarray_problem
TODO: https://afshinm.name/2018/06/24/why-kadane-algorithm-works/

@author a.k
"""
from typing import List


def naive(A: List):
    """
    Naive solution; consider all subarrays and pick the one with the highest sum
    :param A: list of values
    :Time: O(N^3) -- N for sum * (Sum of first N numbers for generating all subarrays) = O(N^3)
            N.B. Can reduce to O(N^2) by avoiding recomputing sum for every new subarray by using already computed sum
    :Space: O(1)
    :return: max subarray sum
    """
    max_sum = float('inf')
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            max_sum = max(max_sum, sum(A[i:j + 1]))

    return max_sum


def better_naive(A: List):
    """
    Better Naive solution; consider all subarrays and pick the one with the highest sum.
    :param A: list of values
    :Time: O(N^2) Avoid unnecessary recomputing sums each time by adding onto previously calculate sum
    :Space: O(1)
    :return: max subarray sum
    """
    max_sum = float('-inf')
    for i in range(len(A)):
        sum_so_far = 0
        for j in range(i + 1, len(A)):
            sum_so_far += A[j]  # optimized summing el  ements
            max_sum = max(max_sum, sum_so_far)

    return max_sum


def attempt(A: List, i):
    if i < 0:
        return float('-inf')

    prev = attempt(A, i - 1)
    # If prev is negative, no point adding
    if prev < 0:
        return A[i]
    else:
        return max(A[i] + prev, A[i])


if __name__ == '__main__':
    print('TESTING')
    test = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(better_naive(test))
