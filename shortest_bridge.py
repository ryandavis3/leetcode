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
            if visited[i][j]:
                coordinates.add((i, j))
    return coordinates


def find_islands(grid: List[List[int]]) -> Islands:
    n = len(grid)
    islands_found = 0
    visited_first = get_empty_matrix(n=n)
    visited_second = get_empty_matrix(n=n)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1 and not visited_first[i][j] and not visited_second[i][j]:
                if islands_found == 0:
                    dfs(grid=grid, visited=visited_first, i=i, j=j)
                    island_1 = get_coordinates_from_visited(visited=visited_first)
                    print(island_1)
                    islands_found += 1
                elif islands_found == 1:
                    dfs(grid=grid, visited=visited_second, i=i, j=j)
                    island_2 = get_coordinates_from_visited(visited=visited_second)
                    islands_found += 1
                else:
                    raise ValueError('Already found two islands!')
    islands = Islands(island_1=island_1, island_2=island_2)
    return islands


def find_shortest_bridge_from_islands(islands: Islands) -> int:
    shortest_bridge = 10 ** 10
    for coordinates_1 in islands.island_1:
        x_1, y_1 = coordinates_1
        for coordinates_2 in islands.island_2:
            x_2, y_2 = coordinates_2
            bridge_len = abs(x_1 - x_2) + abs(y_1 - y_2) - 1
            if bridge_len < shortest_bridge:
                shortest_bridge = bridge_len
    return shortest_bridge


def find_shortest_bridge_from_grid(grid: List[List[int]]) -> int:
    islands = find_islands(grid=grid)
    shortest_bridge = find_shortest_bridge_from_islands(islands=islands)
    return shortest_bridge


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        pass


class TestShortestBridge(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.grid = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
        cls.visited_expected_1 = [[1, 1, 0], [1, 1, 0], [0, 0, 0]]
        cls.visited_expected_2 = [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
        island_1 = {(0, 0), (0, 1), (1, 0), (1, 1)}
        island_2 = {(2, 2)}
        cls.islands = Islands(
            island_1=island_1,
            island_2=island_2,
        )

    def test1(self) -> None:
        visited = get_empty_matrix(n=3)
        dfs(grid=self.grid, visited=visited, i=0, j=0)
        self.assertEqual(visited, self.visited_expected_1)
        visited = get_empty_matrix(n=3)
        dfs(grid=self.grid, visited=visited, i=2, j=2)
        self.assertEqual(visited, self.visited_expected_2)

    def test2(self) -> None:
        islands = find_islands(grid=self.grid)
        self.assertEqual(islands, self.islands)

    def test3(self) -> None:
        shortest_bridge = find_shortest_bridge_from_islands(islands=self.islands)
        self.assertEqual(shortest_bridge, 1)

    def test4(self) -> None:
        shortest_bridge = find_shortest_bridge_from_grid(grid=self.grid)
        self.assertEqual(shortest_bridge, 1)

    def test5(self) -> None:
        grid = [[0, 1], [1, 0]]
        shortest_bridge = find_shortest_bridge_from_grid(grid=grid)
        self.assertEqual(shortest_bridge, 1)