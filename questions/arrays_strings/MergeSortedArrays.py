"""
Merge two sorted arrays and return it as a new sorted array.

Approaches: 1) Standard merging of two arrays approach

@author a.k
"""
import random, time


def merge(a1: list, a2: list) -> list:
    """
    Returns a sorted, merged array by merging a1 and a2.
    Algorithm: an auxiliary array, a3, is used to selectively copy over elements from a1 and a2.
    Traversing a1 and a2 simultaneously, copy the smaller of the current element into a3 and increment
    the pointer of a3 and the pointer of the array whose element is smaller.
    If there are remaining elements in a1 or a2, copy to a3.
    Edge cases: a1 is none and a2 is none, either are none.
    :param a1: array 1
    :param a2: array 2
    :Time: O(N + M)
    :Space: O(N + M) for aux array
    :return: a sorted array merging a1 and a2
    """
    if a1 is None:
        return a2
    if a2 is None:
        return a1
    n = len(a1)
    m = len(a2)
    a3 = [None] * (n + m)

    i = j = k = 0
    while i < n and j < m:
        if a1[i] < a2[j]:  # If a1[i] is smaller, copy that
            a3[k] = a1[i]
            i += 1
        else:
            a3[k] = a2[j]  # Else, copy a2[j]
            j += 1
        k += 1

    # If elements are remaining in either array, copy those
    while i < n:
        a3[k] = a1[i]
        k += 1
        i += 1

    while j < m:
        a3[k] = a2[j]
        k += 1
        j += 1

    # Post-condition check
    assert a3 == sorted(a1 + a2), "Error! Post-condition failed"
    return a3


if __name__ == "__main__":
    a1 = [5, 8, 9, 11]
    a2 = [4, 7, 8, 10]
    print(merge(a1, a2))
    a1 = None
    a2 = None
    print(merge(a1, a2))
    a1 = None
    a2 = [4, 7, 8, 10]
    print(merge(a1, a2))
    a1 = [5, 8, 9]
    a2 = [4, 7, 8, 10]
    print(merge(a1, a2))
    a1 = [5, 8, 9, 14, 19, 20, 22]
    a2 = [4, 7, 8, 10]
    print(merge(a1, a2))

    a1 = []
    a2 = []
    for i in range(-int(random.random() * 20), int(random.random() * 10)):
        a1.append(random.randint(i, 500))
        # random.seed(time.time())
        a2.append(random.randint(i, 500))
    print(merge(sorted(a1), sorted(a2)))
