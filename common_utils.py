"""
Common util functions
"""
from typing import List

from data_structures.trees.utils import pretty_print_tree

print_tree = pretty_print_tree


def print_matrix(A: List[List[object]]):
    """
    Pretty print for matrix
    :param A: matrix
    :return: none
    """
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in A]))


if __name__ == '__main__':
    test = [[i + j for i in range(10)] for j in range(4)]
    print_matrix(test)
