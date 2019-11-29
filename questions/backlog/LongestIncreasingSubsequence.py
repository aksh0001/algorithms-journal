"""
https://leetcode.com/problems/longest-increasing-subsequence/
todo
"""
from typing import List


def lengthOfLIS(self, nums: List[int]) -> int:
    return LIS(nums, 0, float('-inf'))  # -inf symbolizes no constraint


def LIS(A, i, current_constraint):
    if i > len(A) - 1:
        return 0

    include = exclude = float('-inf')

    if A[i] > current_constraint:
        include = 1 + LIS(A, i + 1, A[i])

    exclude = LIS(A, i + 1, current_constraint)
    return max(exclude, include)
