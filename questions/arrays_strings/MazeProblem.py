"""
Module for the basic maze path problem, where given a starting position, a destination, and a maze filled with obstacles,
return whether it is possible to get from the starting position to the destination.

@author a.k
"""


def find_paths(row, column, layout, x, y, marked, path_to: dict):
    """
    Uses standard recursive algorithm to determine if a path exists
    :param row: total rows
    :param column: total columns
    :param layout: matrix grid
    :param x: start position x
    :param y: start position y
    :param marked: 2D boolean array to mark visited cells
    :param path_to: some structure that will allow backtracking to find the actual path taken
    :Time: O(NM) where N is rows and M is columns (we don't revisit cells thanks to our marked array)
    :Cells: O(NM) where N is rows and M is columns
    :return: whether if a path exists
    """
    # If (x,y) outside maze, false
    if x < 0 or x >= row or y < 0 or y >= column:
        return False
    if marked[x][y]:  # If we have been to the cell before, false
        return False
    # If (x, y) is goal, true
    if layout[x][y] == '*':
        return True
    # If (x, y) is closed, false
    if layout[x][y] == 0:
        return False

    marked[x][y] = True
    if find_paths(row, column, layout, x, y - 1, marked, path_to):  # Go north and recurse
        path_to[(x, y - 1)] = (x, y)
        return True
    if find_paths(row, column, layout, x + 1, y, marked, path_to):  # Go east and recurse
        path_to[(x + 1, y)] = (x, y)
        return True
    if find_paths(row, column, layout, x, y + 1, marked, path_to):  # Go south and recurse
        path_to[(x, y + 1)] = (x, y)
        return True
    if find_paths(row, column, layout, x - 1, y, marked, path_to):  # Go west and recurse
        path_to[(x - 1, y)] = (x, y)
        return True

    return False


if __name__ == "__main__":
    test1 = ([[1, 1, 1], [1, 1, 1], [1, 1, '*']], (0, 1))
    test1_ans = True

    test2 = ([[1, 1, 1], ['*', 1, 1], [0, 1, 0]], (0, 0))
    test2_ans = True

    test3 = ([[0, 0, 0], ['*', 1, 1], [0, 1, 1]], (0, 0))
    test3_ans = False

    test4 = ([[1, 0, 1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0],
              [1, 0, 1, 0, '*', 0, 1, 1], [1, 1, 1, 0, 1, 0, 0, 1], [1, 0, 1, 0, 1, 1, 0, 1],
              [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1]], (0, 0))
    test4_ans = True

    # print(find_paths(3, 3, test1[0], test1[1][0], test1[1][1], [[False for x in range(3)] for y in range(3)]))
    # print(find_paths(3, 3, test2[0], test2[1][0], test2[1][1], [[False for x in range(3)] for y in range(3)]))
    # print(find_paths(3, 3, test3[0], test3[1][0], test3[1][1], [[False for x in range(3)] for y in range(3)]))
    path = {}
    print(find_paths(8, 8, test4[0], test4[1][0], test4[1][1], [[False for x in range(8)] for y in range(8)], path))
    print(path)
