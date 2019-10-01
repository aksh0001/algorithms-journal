"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai),
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water,
and return the AREA.

Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49

@author a.k
"""
from typing import List


def naive(H: List[int]) -> int:
    """
    Naive solution to problem involving generating all doubles, then choosing the largest.
    :param H: list of heights
    :Time: O(N^2)
    :Space: O(1)
    :return: max area
    """
    # NAIVE: O(N^2) - go through each pairs (try each double)
    max_area = float('-inf')
    for i in range(len(H)):
        for j in range(i + 1, len(H)):
            area = (j - i) * min(H[i], H[j])  # calc area
            max_area = max(max_area, area)  # update max seen so far
    return max_area


def most_water(H: List[int]) -> int:
    """
    Efficient solution to the problem that involves chopping off smaller endpoints.
    @Algorithm: Note that the area of any two intervals is limited by the height of the smaller one.
                Therefore, instead of redundantly checking each double, we can start with the widest container.
                - Start at l = 0 and r = n - 1. If H[l] < H[r] then this is the largest area that we can form with l
                - Move to the next l since there is no point considering it again - vice-versa if H[r] > H[l]
                - Return the max rea seen
    :param H: list of heights
    :Time: O(N)
    :Space: O(1)
    :return: max area
    """
    l, r, max_area = 0, len(H) - 1, float('-inf')
    while l <= r:
        area = (r - l) * min(H[l], H[r])
        max_area = max(area, max_area)
        # Chop off the smaller of the two since we've already obtained the maximum possible area using the smaller one
        if H[l] < H[r]:
            l += 1
        else:
            r -= 1
    return max_area


if __name__ == '__main__':
    test = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert naive(test) == 49, 'ERROR!'
    assert most_water(test) == 49, 'ERROR!'
    print('PASSED')
