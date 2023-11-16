from typing import List
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


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        pass