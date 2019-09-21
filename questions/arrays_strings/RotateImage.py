"""
Solves the image/matrix rotation problem:
Given an square matrix, turn it by 90 degrees in anti-clockwise direction without using any extra space.
Input
 1  2  3
 4  5  6
 7  8  9

Output:
 3  6  9
 2  5  8
 1  4  7

 @author a.k
"""
from typing import List


def rotate(matrix: List[List[int]]):
    """
    This function rotates the matrix by 90 degrees clockwise.
    Algorithm:
        - In order to not use any additional structures, we must rely on "smart swaps"
        - We can replicate a rotation of the entire matrix 90 degrees by rotating layer by layer
        - At each layer we swap elements at all four corners
        - Repeat for all the layers (total N//2)
    :param matrix: image matrix, N*N
    :Time: O(N^2)
    :Space: O(1)
    :return: none--inplace algorithm
    """
    N = len(matrix)
    for i in range(N // 2):
        for j in range(i, N - 1 - i):
            swap_corners(matrix, (i, j), (j, N - 1 - i), (N - 1 - j, i), (N - 1 - i, N - 1 - j))


def swap_corners(img, a: tuple, b: tuple, c: tuple, d: tuple):
    """
    This function is used to swap corners in the matrix.
    :param img: the image matrix
    :param a: corner a
    :param b: corner b
    :param c: corner c
    :param d: corner d
    :Time: O(1)
    :Space: O(1)
    :return: none
    """
    img[a[0]][a[1]], img[b[0]][b[1]] = img[b[0]][b[1]], img[a[0]][a[1]]
    img[c[0]][c[1]], img[a[0]][a[1]] = img[a[0]][a[1]], img[c[0]][c[1]]
    img[d[0]][d[1]], img[c[0]][c[1]] = img[c[0]][c[1]], img[d[0]][d[1]]


if __name__ == '__main__':
    test = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in test]))
    rotate(test)
    print("\n")
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in test]))
