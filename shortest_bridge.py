from dataclasses import dataclass
from typing import List, Set, Tuple
from unittest import TestCase


def get_empty_matrix(n: int) -> List[List[int]]:
    matrix: List[int] = []
    for _ in range(n):
        matrix += [[0] * n]
    return matrix


def dfs(grid: List[List[int]], visited: List[List[int]], i: int, j: int) -> None:
    if grid[i][j] == 0:
        return None
    if visited[i][j] == 1:
        return None
    visited[i][j] = 1
    n = len(grid)
    if i > 0:
        dfs(grid=grid, visited=visited, i=i-1, j=j)
    if j > 0:
        dfs(grid=grid, visited=visited, i=i, j=j-1)
    if i < n - 1:
        dfs(grid=grid, visited=visited, i=i+1, j=j)
    if j < n - 1:
        dfs(grid=grid, visited=visited, i=1, j=j+1)


@dataclass(frozen=True)
class Islands:
    island_1: Set[Tuple]
    island_2: Set[Tuple]


def get_coordinates_from_visited(visited: List[List[int]]) -> Set[Tuple]:
    n = len(visited)
    coordinates = set()
    for i in range(n):
        for j in range(n):
            coordinates.add((i, j))
    return coordinates


def find_islands(grid: List[List[int]]) -> Islands:
    n = len(grid)
    islands_found = 0
    visited_first = get_empty_matrix(n=n)
    visited_second = get_empty_matrix(n=n)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1 and visited_first[i][j] == 0 and visited_second[i][j] == 0:
                if islands_found == 0:
                    dfs(grid=grid, visited=visited_first, i=i, j=j)
                    island_1 = get_coordinates_from_visited(visited=visited_first)
                    islands_found += 1
                elif islands_found == 1:
                    dfs(grid=grid, visited=visited_second, i=i, j=j)
                    island_2 = get_coordinates_from_visited(visited=visited_second)
                    islands_found += 1
                else:
                    raise ValueError('Already found two islands!')
    islands = Islands(island_1=island_1, island_2=island_2)
    return islands



class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        pass


class TestShortestBridge(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.grid = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

    def test1(self) -> None:
        visited = get_empty_matrix(n=3)
        dfs(grid=self.grid, visited=visited, i=0, j=0)
        visited_expected = [[1, 1, 0], [1, 1, 0], [0, 0, 0]]
        self.assertEqual(visited, visited_expected)
        visited = get_empty_matrix(n=3)
        dfs(grid=self.grid, visited=visited, i=2, j=2)
        visited_expected = [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
        self.assertEqual(visited, visited_expected)

    def test2(self) -> None:
        islands = find_islands(grid=self.grid)