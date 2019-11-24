"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Example 1:
Input: [2,2,1]
Output: 1

@author a.k
"""
from typing import List


def naive(nums: List[int]) -> int:
    """
    Naive approach using hash set.
    :param nums: list of numbers
    :Time: O(N)
    :Space: O(N)
    :return: the single number
    """
    seen = set({})
    for num in nums:
        if num in seen:
            seen.remove(num)
        else:
            seen.add(num)
    return seen.pop()  # that one element remaining is the "one"


def single_number(nums: List[int]) -> int:
    """
     Bit manipulation solution:
     n1 xor 0 = n1;
     n1 xor n1 = 0;
     Therefore xor all the numbers together to get the single number
    :param nums: list of nums
    :Time: O(N)
    :Space: O(1)
    :return: the single numer
    """
    ans = 0
    for num in nums:
        ans ^= num
    return ans
