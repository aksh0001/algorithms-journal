""""
This module implements an undirected Graph API.

@author a.k
"""
from typing import List, Tuple, Iterable

from data_structures.LinkedList import SinglyLinkedList
from data_structures.graphs.graph_utils import Edge, GeneralGraph, dfs_print


class UGraph(GeneralGraph):
    def __init__(self, V: int):
        self.V = V  # total vertices
        self.E = 0  # total edges
        self.adjacency_list: List[SinglyLinkedList] = [SinglyLinkedList() for i in range(V)]  # adjacency list

    def add_edge(self, v: int, w: int, weight: float = None):
        """
        This method adds an edge into the adjacency list
        :param v: from vertex
        :param w: to vertex
        :param weight: weight of edge if supplied
        :return: void
        """
        if 0 <= v < self.V and 0 <= w < self.V:
            self.adjacency_list[v].insert(Edge(v, w))
            self.adjacency_list[w].insert(Edge(w, v))  # undirected - insert both ways
            self.E += 1
        else:
            raise AssertionError('Invalid edge vertices')

    def adjacent(self, v: int) -> Iterable:
        """
        Returns all the vertices adjacent to vertex, v
        :param v: vertex v
        :return: list of vertices adjacent to vertex v
        """
        if 0 <= v < self.V:
            return self.adjacency_list[v]
        else:
            raise AssertionError('vertex does not exist')

    def total_vertices(self):
        """
        Returns total vertices in this graph
        :return: total vertices
        """
        return self.V

    def total_edges(self):
        """
        Returns total edges in this graph
        :return: total edges
        """
        return self.E

    def assemble(self, edges: List[Tuple[int]]):
        """
        Quickly add edges given by tuples
        :param edges:
        :return: none
        """
        for e in edges:
            self.add_edge(e[0], e[1])

    def __str__(self):
        s = ""
        for v in range(self.V):
            s += str(v) + '||'
            for w in self.adjacent(v):
                s += str(w.get_to()) + "->"
            s += '\n'
        return s


if __name__ == '__main__':
    ug = UGraph(13)
    edges_add = [(0, 1), (0, 2), (6, 0), (0, 5), (4, 6), (3, 4), (5, 3), (5, 4), (7, 8), (9, 10), (9, 12), (9, 11)]
    ug.assemble(edges_add)

    print(ug)
    print('DFS')
    dfs_print(ug, 0)
