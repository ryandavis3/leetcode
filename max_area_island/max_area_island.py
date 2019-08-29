from typing import List

# https://leetcode.com/problems/number-of-islands/

def search(grid: List[List[str]], i: int, j: int) -> None:
    """
    Search grid and get area of island.
    """
    # Dimensions of grid
    m = len(grid)
    n = len(grid[0])
    # Return None if coordinates off grid
    if i < 0 or i > m - 1 or j < 0 or j > n - 1:
        return 0
    # Mark '1' as 'X'
    if grid[i][j] != 1:
        return 0
    grid[i][j] = 'X'
    # Search left, right, up, down
    left = search(grid, i, j-1)
    right = search(grid, i, j+1)
    up = search(grid, i-1, j)
    down = search(grid, i+1, j)
    return 1 + left + right + up + down

def maxAreaIsland(grid: List[List[str]]) -> int:
    """
    Compute maximum area of an island on the grid.
    """
    # No grid passed!
    if not grid:
        return 0
    # Dimensions of grid
    m = len(grid)
    n = len(grid[0])
    # Iterate over each cell in grid
    max_area = 0
    for i in range(m):
        for j in range(n):
            # New island found
            if grid[i][j] == 1:
                # Mark all cells in island
                area = search(grid, i, j)
                if area > max_area:
                    max_area = area
    return max_area

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        pass
