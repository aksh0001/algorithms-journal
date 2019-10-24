"""
Common graph processing functions

@author a.k
"""
import abc
from typing import List
from data_structures.Queue import Queue


class Edge:
    def __init__(self, v: int, w: int, weight: float = None):
        self.v = v
        self.w = w
        self.weight = weight

    def get_from(self):
        """
        Returns the from vertex of this edge (v->w) which is v
        :return: from vertex
        """
        return self.v

    def get_to(self):
        """
        Returns the to vertex of this edge (v->w) which is w
        :return: to vertex
        """
        return self.w

    def get_weight(self):
        """
        Returns the weight of this edge
        :return: weight of edge
        """
        return self.weight

    def __str__(self):
        return str(self.v) + '->' + str(self.w) + ' (' + str(self.weight) + ')'


class GeneralGraph(abc.ABC):

    @abc.abstractmethod
    def total_vertices(self):
        pass

    @abc.abstractmethod
    def total_edges(self):
        pass

    @abc.abstractmethod
    def adjacent(self, v: int) -> iter:
        """
        Returns all the vertices adjacent to vertex, v
        :param v: vertex v
        :return: list of vertices adjacent to vertex v
        """
        pass

    @abc.abstractmethod
    def add_edge(self, v: int, w: int, weight: float = None):
        """
        This method adds an edge into the adjacency list
        :param v: from vertex
        :param w: to vertex
        :param weight: weight of edge if supplied
        :return: void
        """
        pass


def dfs_print(G: GeneralGraph, s: int):
    """
    Prints graphs from source s in dfs fashion
    :param G: graph
    :param s: source
    :Time: O(V + E)
    :Space: O(V)
    :return: none
    """
    visited = [False for _ in range(G.total_vertices())]

    def dfs(s: int, visited: List[bool]):
        visited[s] = True
        print(s)
        for w in G.adjacent(s):
            if not visited[w.get_to()]:
                dfs(w.get_to(), visited)

    dfs(s, visited)


def bfs_print(G: GeneralGraph, s: int):
    """
    Prints graphs from source s in bfs fashion
    :param G: graph
    :param s: source
    :Time: O(V + E)
    :Space: O(V)
    :return: none
    """
    bfs_queue, visited = Queue(), [False for _ in range(G.total_vertices())]
    # Mark source as visited and enqueue
    visited[s] = True
    bfs_queue.enqueue(s)

    while not bfs_queue.is_empty():
        # dequeue and print
        removed = bfs_queue.dequeue()
        print(removed)
        # process adjacent vertices
        for w in G.adjacent(removed):
            if not visited[w.get_to()]:  # If not visited mark as visited and enqueue
                visited[w.get_to()] = True
                bfs_queue.enqueue(w.get_to())
