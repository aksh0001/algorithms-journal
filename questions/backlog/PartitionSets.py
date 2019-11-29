"""
Implements algorithms for the partition sets problem.
Determine whether a given set can be partitioned into two subsets such that the sum of elements in both subsets is same.

@author a.k
"""


def naive(G, i, current_sum, sum):
    if i >= len(G):
        return False
    if G[i] + current_sum == sum:
        return True
    if G[i] > sum - current_sum:
        return naive(G, i + 1, current_sum, sum)
    if naive(G, i + 1, current_sum + G[i], sum) or naive(G, i + 1, current_sum, sum):
        return True

    return False


if __name__ == '__main__':
    print("Testing...")
    G = [4, 5, 3, 9, 7]
    G = [2, 26, 6, 20]
    print(naive(G, 0, 0, sum(G) // 2))
