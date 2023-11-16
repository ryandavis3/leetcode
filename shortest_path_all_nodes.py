from typing import Dict, List, Set
from unittest import TestCase


def get_adjacency_dict(graph: List[List[int]]) -> Dict[int, Set]:
    adjacency_dict: Dict[int, Set] = {}
    for i, adjacent in enumerate(graph):
        adjacency_dict[i] = set(adjacent)
    return adjacency_dict


def get_empty_visited_dict(n: int) -> Dict[int, int]:
    visited_dict: Dict[int, int] = {}
    for i in range(n):
        visited_dict[i] = 0
    return visited_dict


def remove_node_adjacency_dict(adjacency_dict: Dict[int, Set], node: int) -> Dict[int, Set]:
    adjacent_nodes = adjacency_dict[node]
    for adjacent_node in adjacent_nodes:
        adjacency_dict[adjacent_node].remove(node)
    del adjacency_dict[node]


def find_next_node(adjacency_dict: Dict[int, Set], node: int) -> int:
    adjacent_nodes = adjacency_dict[node]
    candidates = set()
    min_degree = 10 ** 10
    for adjacent_node in adjacent_nodes:
        degree = len(adjacency_dict[adjacent_node])
        if degree == min_degree:
            candidates.add(adjacent_node)
        elif degree < min_degree:
            min_degree = degree
            candidates = set([adjacent_node])
    if len(candidates) == 1:
        return candidates.pop()


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        pass


class TestShortestPath(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = [[1, 2, 3], [0], [0], [0]]

    def test1(self) -> None:
        adjacency_dict = get_adjacency_dict(graph=self.graph)
        adjacency_dict_expected = {0: {1, 2, 3}, 1: {0}, 2: {0}, 3: {0}}
        self.assertEqual(adjacency_dict, adjacency_dict_expected)

    def test2(self) -> None:
        adjacency_dict = {0: {1, 2, 3}, 1: {0}, 2: {0}, 3: {0}}
        remove_node_adjacency_dict(adjacency_dict=adjacency_dict, node=1)
        adjacency_dict_expected = {0: {2, 3}, 2: {0}, 3: {0}}
        self.assertEqual(adjacency_dict, adjacency_dict_expected)