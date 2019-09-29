"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

https://leetcode.com/problems/generate-parentheses/discuss/393341/MUST-READ%3A-Very-Easy-Commented-7-lines-Python

@author a.k
"""


def sol(n):
    ans, curr = [], ""
    generate(n, 0, 0, ans, curr)
    return ans


def generate(n, open, closed, ans, curr):
    """
    Given n, generates all possible and valid combinations n-pairs of parenthesis
    @Algorithm (see my LeetCode post)
    :param n: original n-pair number
    :param open: tracks number of open parens used
    :param closed: tracks number of closed parens used
    :param ans: list that we use to append answers
    :param curr: current string being formed
    :Time: O(X) (perhaps O(2^N)?)
    :Space: O(X)
    :return: none
    """
    if open == n and closed == n:  # done generating, append
        ans.append(curr)
    else:
        if open < n:  # Ensure we can still insert open parens
            generate(n, open + 1, closed, ans, curr + '(')
        if closed < n and closed < open:  # Ensure we can still insert closed parens and we don't invalidate expression
            generate(n, open, closed + 1, ans, curr + ')')  # N.B. expression becomes invalid if we have closed >= open


if __name__ == '__main__':
    print(sol(3))
