import unittest
from dataclasses import dataclass
from typing import List, Tuple


LARGE_NUMBER = 10 ** 10


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


@dataclass(frozen=True)
class MaxSafenessFactorResults:
    grid: Grid
    path_safe_factors: List[List]
    max_safeness_factor: int


def maximum_safeness_factor(grid: List[List[int]]) -> MaxSafenessFactorResults:
    _grid = Grid(grid=grid)
    rows = len(grid)
    columns = len(grid[0])
    path_safe_factors: List[List[int]] = []
    for _ in range(rows):
        row = [LARGE_NUMBER] * columns
        path_safe_factors += [row]
    for i in range(rows):
        for j in range(columns):
            cell_safe_factor = _grid.get_minimum_manhattan_distance_to_thief(i=i, j=j)
            if i == 0 and j == 0:
                path_safe_factors[i][j] = cell_safe_factor
            elif i == 0 and j > 0:
                path_safe_factors[i][j] = min(path_safe_factors[i][j-1], cell_safe_factor)
            elif i > 0 and j == 0:
                path_safe_factors[i][j] = min(path_safe_factors[i-1][j], cell_safe_factor)
            else:
                safest_pre_path = max(path_safe_factors[i-1][j], path_safe_factors[i][j-1])
                path_safe_factors[i][j] = min(safest_pre_path, cell_safe_factor)
    max_safeness_factor_results = MaxSafenessFactorResults(
        grid=_grid,
        path_safe_factors=path_safe_factors,
        max_safeness_factor=path_safe_factors[-1][-1],
    )
    return max_safeness_factor_results


def maximum_safeness_factor2(grid: List[List[int]]) -> MaxSafenessFactorResults:
    _grid = Grid(grid=grid)
    rows = len(grid)
    columns = len(grid[0])
    cell_safe_factors: List[List[int]] = []
    for _ in range(rows):
        row = [None] * columns
        cell_safe_factors += [row]
    for i in range(rows):
        for j in range(columns):
            cell_safe_factor = _grid.get_minimum_manhattan_distance_to_thief(i=i, j=j)
            cell_safe_factors[i][j] = cell_safe_factor
    max_safeness_factor_results = MaxSafenessFactorResults(
        grid=_grid,
        path_safe_factors=path_safe_factors,
        max_safeness_factor=path_safe_factors[-1][-1],
    )
    return max_safeness_factor_results


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        results = maximum_safeness_factor(grid=grid)
        return results.max_safeness_factor


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
        results = maximum_safeness_factor(grid=grid)
        self.assertEqual(results.max_safeness_factor, 2)

    def test3(self) -> None:
        grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]
        results = maximum_safeness_factor(grid=grid)
        self.assertEqual(results.max_safeness_factor, 2)
