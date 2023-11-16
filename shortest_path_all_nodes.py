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


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        pass


class TestShortestPath(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = [[1,2,3],[0],[0],[0]]

    def test1(self) -> None:
        adjacency_dict = get_adjacency_dict(graph=self.graph)
        adjacency_dict_expected = {0: {1, 2, 3}, 1: {0}, 2: {0}, 3: {0}}
        self.assertEqual(adjacency_dict, adjacency_dict_expected)