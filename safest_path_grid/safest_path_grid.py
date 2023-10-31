import unittest
from typing import List, Tuple


class Grid:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.thief_coordinates: List[Tuple] = []
        rows = len(grid)
        columns = len(grid[0])
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    self.thief_coordinates += [(i, j)]

    def get_minimum_manhattan_distance_to_thief(self, i: int, j: int) -> int:
        min_distance = 10 ** 10
        for coordinates in self.thief_coordinates:
            a, b = coordinates
            distance = abs(a-i) + abs(b-j)
            if distance < min_distance:
                min_distance = distance
        return min_distance


def maximum_safeness_factor(grid: List[List[int]]) -> int:
    _grid = Grid(grid=grid)
    rows = len(grid)
    columns = len(grid[0])
    path_safe_factors: List[List[int]] = []
    for _ in range(rows):
        row = [0] * columns
        path_safe_factors += [row]
    for i in range(rows):
        for j in range(columns):
            cell_safe_factor = grid.get_minimum_manhattan_distance_to_thief(i=i, j=j)
            if i == 0 and j == 0:
                path_safe_factors[i][j] = cell_safe_factor
            elif i == 0 and j > 0:
                path_safe_factors[i][j] = min(path_safe_factors[i][j-1], cell_safe_factor)
            elif i > 0 and j == 0:
                path_safe_factors[i][j] = min(path_safe_factors[i-1][j], cell_safe_factor)
            else:
                safest_pre_path = max(path_safe_factors[i-1][j], path_safe_factors[i-1][j])
                path_safe_factors[i][j] = min(safest_pre_path, cell_safe_factor)
    return path_safe_factors[-1][-1]


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        pass


class TestGrid(unittest.TestCase):
    def test_init(self) -> None:
        grid = [[0, 0, 1], [0, 0, 0], [0, 0, 0]]
        _ = Grid(grid=grid)

    def test_get_minimum_manhattan_distance_to_thief(self) -> None:
        grid = [[0, 0, 1], [0, 0, 0], [0, 0, 0]]
        grid_class = Grid(grid=grid)
        test_cases = {
            (0, 0): 2,
            (1, 0): 3,
            (2, 0): 4,
            (0, 1): 1,
        }
        for coordinates, min_distance_expected in test_cases.items():
            i, j = coordinates
            min_distance = grid_class.get_minimum_manhattan_distance_to_thief(i=i, j=j)
            self.assertEqual(min_distance, min_distance_expected)


class TestSafestPath(unittest.TestCase):

    def test2(self) -> None:
        grid = [[0, 0, 1], [0, 0, 0], [0, 0, 0]]