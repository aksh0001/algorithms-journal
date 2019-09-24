"""
Zero matrix problem
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
E.g.
Input:
  [1,1,1]
  [1,0,1]
  [1,1,1]
Output:
  [1,0,1]
  [0,0,0]
  [1,0,1]
@author a.k
"""
from typing import List


def set_zeroes(A: List[List[int]]) -> None:
    """
    If A[i][j] = 0, sets entire row i and col j to 0.
    @Algorithm:  - use input to track which rows and which columns to set to 0
                        i.e. use first row to check which column to set and first column to check which row to set
                - first check if the first row or first column contains a 0; if so, flag variables to indicate to
                  nullify it later
                - loop over A; if A[i][j]=0, set A[0][j] & A[i][0] to 0 to indicate to set entire row i and col j to 0
                - loop over rest of A; and set A[i][j] to 0 if A[0][j] = 0 or A[i][0] = 0
                - finally nullify first row and col depending on our flags
    :param A: n x m matrix
    :Time: O(n*m)
    :Space:  O(1)
    :return: none
    """
    # Make use of the input to track which rows and columns we need to set to 0
    # i.e. use first row of matrix to track which column to set to 0 and first column to track which row to set to 0
    first_row_set = first_col_set = False  # track if we need to set the first row and first col to 0
    for i in range(len(A[0])):
        if A[0][i] == 0:
            first_row_set = True
    for j in range(len(A)):
        if A[j][0] == 0:
            first_col_set = True

    # pre-process and find the zeros
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 0:
                A[0][j] = 0  # mark that we need to set col j to 0
                A[i][0] = 0  # mark that we need to set row i to 0

    # Loop through A again and set A[i]][j] to 0 if row i OR row j need to be set
    for i in range(1, len(A)):
        for j in range(1, len(A[0])):
            if A[0][j] == 0 or A[i][0] == 0:
                A[i][j] = 0

    # Now check our flags, first_row_set and first_col_set to see if they need to be set to 0
    if first_row_set:
        for i in range(len(A[0])):
            A[0][i] = 0
    if first_col_set:
        for j in range(len(A)):
            A[j][0] = 0


if __name__ == '__main__':
    test = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(test)
    set_zeroes(test)
    print(test)
