"""
This module implements the Jump Game III solution (on leetcode)
@author a.k
"""


def solution(nums):
    return aux(nums, 0, {}, len(nums) - 1)


def aux(nums, i, memo, n):
    if i in memo:
        return memo[i]
    if i == n:
        memo[i] = 0
    else:
        min_jump = float("inf")
        for jump in range(1, nums[i] + 1):  # Go through each jump candidate of a[i]
            if i + jump <= n:  # Ensure we don't address overflows
                candidate = aux(nums, i + jump, memo, n)
                if candidate != -1:  # Handle the -1 returned if no solution
                    min_jump = min(1 + candidate, min_jump)  # Add 1 here since there is a jump from i to i + jump

        memo[i] = min_jump

    if memo[i] != float("inf"):
        return memo[i]
    else:
        return -1


if __name__ == "__main__":
    test = [2, 3, 1, 1, 4]
    print(solution(test))
