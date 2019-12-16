"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Input: text = "nlaebolko"
Output: 1

Input: text = "loonbalxballpoon"
Output: 2

@author a.k
"""
from typing import List


def max_number_of_balloons(text: str) -> int:
    """
    Returns the max number of "balloons" able to be formed in text.
    :param text: string of text
    :Time: O(N)
    :Space: O(1)
    :return: maximum times "balloon" can be formed
    """
    occurrences = [0] * 5  # one bucket for each character (b, a, l, o, n)
    for c in text:  # collect occurrences for each character of "balloon"
        if c == "b":
            occurrences[0] += 1
        elif c == "a":
            occurrences[1] += 1
        elif c == "l":
            occurrences[2] += 1
        elif c == "o":
            occurrences[3] += 1
        elif c == "n":
            occurrences[4] += 1
    return get_max(occurrences)


def get_max(occ: List[int]) -> int:
    """
    Returns the maximum number of balloons that can be formed given frequency of its characters.
    :param occ: frequency of characters of "balloon"
    :return: the maximum number of "balloon"s that can be formed
    """
    # Numbers of times "balloon" appears is limited by the least frequently occurring character
    #   B A L O N
    # [x,x,2x,2x,x]
    occ[2], occ[3] = occ[2] // 2, occ[3] // 2  # minimum could be limited by "l" or "o", which occurs twice, so halve it to normalize
    return min(occ)
