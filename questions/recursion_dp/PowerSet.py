"""
Given a set of elements, return the power set, i.e. set of all subsets of that set.

Ref: (alternate, but equivalent, implementation) https://www.youtube.com/watch?v=bGC2fNALbNU
Ref: https://www.geeksforgeeks.org/recursive-program-to-generate-power-set/

@author a.k
"""
from typing import List
from copy import deepcopy


def solution(S: list):
    return aux(S, len(S))


def aux(S: list, n: int) -> List[List[int]]:
    """
    Returns the power set of a set, S.
    Algorithm: Q: How can we get the P([a,b,c]) using the P([a,b])
    A: We use P([a,b]) and concatenate it with 'c' appended to each subset in P([a,b]) -- very elegant.
    Therefore, P([a, b, c]) = P([a, b]) + P([a,b]).append_all(c)
    :param S: the set, S.
    :param n: initialized to len(S), but used as an index to refer to a particular element that is being considered.
    :Time: O(N*2^N) todo -- understand why it is N*2^N
    :Space: O(N*2^N)
    :return: a set containing all subsets of S
    """
    ps = []
    if n == 0:  # BC: empty set of length 0
        ps.append([])
    else:
        ps = aux(S, n - 1)  # Recur over the remaining and get the power set of S[0..n-1] recursively
        copy = deepcopy(ps)  # Copy the P(S[0..n-1])
        for subset in ps:
            subset.append(S[n - 1])  # For every subset in P(S[0..n-1]), append the current element being considered
        ps = ps + copy  # Concat recursive call result--copy--and ps, containing current element appended to each subset

    return ps


def alternate(S: list) -> List[List[int]]:
    ps = []

    def aux(S: list, n: int, prefix: list):
        """
        Returns the power set of a set using the include/exclude pattern (like knapsack).
        Algorithm: Two choices for each S[n]:
            1) include S[n] and recur over the rest while using S[n] as the prefix
            2) Exclude S[n] and recur over the rest (not updating the prefix)
        :param S: set, S
        :param n: refers to the element being considered for the two choices
        :param prefix: a crucial parameter that represents the current solution being built.
        :Time: O(N*2^N)
        :Space: O(N*2^N)
        :return:
        """
        if n == 0:
            if [] not in ps:  # kind of messy but solution includes too many empty sets
                ps.append([])
        else:
            # 1'st rec call-INCLUDE-: recur with prefix set to the current item + old prefix
            # Add current item + prefix we're looking at
            ps.append([S[n - 1]] + prefix)
            aux(S, n - 1, prefix + [S[n - 1]])
            # 2'nd rec call-EXCLUDE-: recur without updating prefix, i.e. leave as current
            aux(S, n - 1, prefix)

    aux(S, len(S), [])
    return ps


if __name__ == '__main__':
    print('Testing...')
    tests = [[1, 7, -3], [], [9], [1, -2, 7, 5]]
    ans = []
    for test in tests:
        print(solution(test))
    print("PASSED SOLUTION")
    for test in tests:
        print(alternate(test))
    print("PASSED ALTERNATE")
