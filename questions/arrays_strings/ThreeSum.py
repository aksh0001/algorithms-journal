"""
This module implements the 3-sum problem.
Given an array of integers, return indices of the three numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

@author a.k
"""
from questions.arrays_strings.TwoSum import two_sum


def three_sum_naive(nums, target):
    """
    Returns the three elements that add to the target.
    We look at all possible triplets and find if a combination of triplets adds to target
    :param nums: list of numbers
    :param target: target to be reached
    :return: a list of three numbers
    :Time: O(N^3)
    :Space: O(1)
    """
    ret_val = []
    for i in range(len(nums) - 2):  # i pointer needs to stop at the third-list element
        for j in range(i + 1, len(nums) - 1):  # j pointer needs to stop at the second-last element
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    ret_val.append(i)
                    ret_val.append(j)
                    ret_val.append(k)
    return ret_val


def three_sum(nums, target):
    """
    Returns the three elements that add to the target.
    Algorithm: Consider each nums[i] and call 2-sum on the new target - nums[i]. If a 2-sum call is successful
    then solution found, else if no 2-sum call is successful, no solution
    :param nums: list of numbers
    :param target: target to be reached
    :Time: O(N^2)
    :Space: O(N) -- Note: This is interesting that it is not N^2. Each 2-sum call takes O(N) space and we need N calls
                    but at any given time we only use N space; i.e. the used space is cleared after each call
    :return: a list of three numbers
    """
    ret_val = []
    for i in range(len(nums)):
        check_two_sum = two_sum(nums, target - nums[i], skip=i + 1)  # Avoid double count: skip element already seen
        if check_two_sum != []:
            ret_val.append(i)
            ret_val += check_two_sum
            return ret_val
    return []


if __name__ == "__main__":
    test_1 = ([1, 4, 45, 6, 10, 8], 22)
    print(three_sum_naive(test_1[0], test_1[1]))
    print(three_sum(test_1[0], test_1[1]))

    test_2 = ([3, 6, 9, 11, 1, 8], 12)
    print(three_sum_naive(test_2[0], test_2[1]))
    print(three_sum(test_2[0], test_2[1]))
