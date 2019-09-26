"""
Given n friends, each can remain single or can be paired up with some other friend. Each friend can be paired only once.
Find out the total number of ways in which friends can remain single or can be paired up.
Input  : n = 3
Output : 4

Explanation
{1}, {2}, {3} : all single
{1}, {2, 3} : 2 and 3 paired but 1 is single.
{1, 2}, {3} : 1 and 2 are paired but 3 is single.
{1, 3}, {2} : 1 and 3 are paired but 2 is single.
Note that {1, 2} and {2, 1} are considered same.

Approaches: DP (O(n) space and time) Bottom-up (O(n) time O(1) space)

@author a.k
"""
from typing import List


def count_pairings(n: int, dp: List[int]):
    """
    @Algorithm:
            - Consider friend, A.
                - If A was single, we can recursively calculate the total ways for n-1, i.e. recur(n-1)
                - If A was paired up, we can recursively calculate the total ways for n-2, i.e. recur(n-2)
                    ***however, A can be paired up with any of the remaining n-1 friends.
                    Therefore, if we stipulated that A had to be paired up, then the total ways = (n-1)*recur(n-2)
    Recurrence: recur(n-1) + (n-1)*recur(n-2)
    :param n: number of friends
    :param dp: dp array
    :Time: O(N)
    :Space: O(N)
    :return: total ways friends can be single or paired up
    """
    if dp[n]:
        return dp[n]
    if n == 1:
        return 1
    if n == 2:
        return 2

    dp[n] = count_pairings(n - 1, dp) + (n - 1) * count_pairings(n - 2, dp)
    return dp[n]


# Iterative version - O(1) space
def countFriendsPairings(n):
    a, b, c = 1, 2, 0
    if (n <= 2):
        return n
    for i in range(3, n + 1):
        c = b + (i - 1) * a
        a = b
        b = c
    return c


if __name__ == '__main__':
    tests = [1, 2, 3, 4, 5, 6]
    ans = [1, 2, 4, 10, 26, 76]
    for t, a in zip(tests, ans):
        assert count_pairings(t, dp=[0 for i in range(t + 1)]) == a, 'ERROR!'

    print('PASSED')
