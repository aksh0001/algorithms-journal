"""
This module implements the popular 2-sum problem.
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

@author a.k
"""


def two_sum(nums, target, skip=0):
    """
    Returns the indices of the two numbers that add to a target.
    Algorithm: Track a map of each number to its index using a dict.
    Run through nums and for each nums[i] check the dict if its complement exists.
    if it does add it to the answer
    :param nums: array of ints
    :param target: target to add to
    :param skip: Irrelevant for two-sum: indicates the position we should start at for 3-sum to avoid double counting
    :Time: O(N)
    :Space: O(N)
    :return: list of two numbers that add to the target
    """
    ret_val = []
    # A dict will map the element to its corresponding index
    map = {}
    for i in range(skip, len(nums)):
        map[nums[i]] = i  # map[num] = the index of num in the nums array

    for i in range(skip, len(nums)):
        complement = target - nums[i]
        if complement in map and map[complement] != i:  # If the complement exists, then a solution is found
            # Also ensure that the complement is not nums[i] itself (e.g [3,..], target = 6)
            ret_val.append(i)
            ret_val.append(map[complement])
            return ret_val
    return []


def two_sum_naive(nums, target):
    """
    Returns the indices of the two numbers that add to a target.
    Algorithm: For each element in nums, scan the rest of nums to see if its complement exists
    if it does add it to the answer
    :param nums: array of ints
    :param target: target to add to
    :Time: O(N^2)
    :Space: O(1)
    :return: list of two numbers that add to the target
    """
    ret_val = []
    for i in range(len(nums)):
        complement = target - nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] == complement:
                ret_val.append(i)
                ret_val.append(j)
                return ret_val


if __name__ == "__main__":
    test_1 = ([2, 7, 11, 15], 9)
    test_2 = ([3, 2, 4], 6)

    print(two_sum(test_1[0], test_1[1]))
    print(two_sum_naive(test_1[0], test_1[1]))
    print("")
    print(two_sum(test_2[0], test_2[1]))
    print(two_sum_naive(test_2[0], test_2[1]))
