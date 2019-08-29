from typing import List

# https://leetcode.com/problems/number-of-islands/

def search(grid: List[List[str]], i: int, j: int) -> None:
    """
    Search grid and mark every '1' on island with 'X'
    """
    # Dimensions of grid
    m = len(grid)
    n = len(grid[0])
    # Return None if coordinates off grid
    if i < 0 or i > m - 1 or j < 0 or j > n - 1:
        return None
    # Mark '1' as 'X'
    if grid[i][j] != '1':
        return None
    grid[i][j] = 'X'
    # Search left, right, up, down
    search(grid, i, j-1)
    search(grid, i, j+1)
    search(grid, i-1, j)
    search(grid, i+1, j)

def numIslands(grid: List[List[str]]) -> int:
    """
    Compute number of islands on grid.
    """
    # No grid passed!
    if not grid:
        return 0
    # Dimensions of grid
    m = len(grid)
    n = len(grid[0])
    islands = 0
    # Iterate over each cell in grid
    for i in range(m):
        for j in range(n):
            # New island found
            if grid[i][j] == '1':
                islands += 1
                # Mark all cells in island 
                search(grid, i, j)
    return islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        return numIslands(grid) 
