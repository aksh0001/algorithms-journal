"""
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.
To flip an image horizontally means that each row of the image is reversed.
    For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
    For example, inverting [0, 1, 1] results in [1, 0, 0].

@author a.k
"""
from typing import List


def flipAndInvertImage(A: List[List[int]]) -> List[List[int]]:
    """
    Linear-time algorithm to flip and invert an image.
    :param A: matrix
    :return: resulting matrix, modified ***in place***
    """
    # 1'st pass: reverse every row
    for r in range(len(A)):
        reverse_row(r, A)
    # 2'nd pass: flip every row
    for r in range(len(A)):
        flip_row(r, A)
    return A


def reverse_row(r, A: List[List[int]]):
    """
    Reverses a row with constant space using swaps.
    E.g. [1, 1, 0] results in [0, 1, 1] by having L-R pointers swapping repeatedly
    :param r: row id
    :param A: matrix
    :Time: O(N)
    :Space: O(1)
    :return: none
    """
    row = A[r]
    # Two pointer repeated swap approach
    i, j = 0, len(row) - 1
    while i <= j:  # cant swap if pointing to the same element
        row[i], row[j] = row[j], row[i]
        i, j = i + 1, j - 1


def flip_row(r, A: List[List[int]]):
    """
    Flips a row: every 1 becomes 0 and every 0 becomes 1
    :param r: row id
    :param A: matrix
    :return: none
    """
    row = A[r]
    for i, elem in enumerate(row):
        row[i] = 1 if elem == 0 else 0


if __name__ == '__main__':
    test = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    expected = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
    assert flipAndInvertImage(test) == expected, 'ERROR!'
    print('PASSED!')
