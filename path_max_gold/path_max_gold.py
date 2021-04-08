from typing import List, Set


def getMaximumGold(grid: List[List[int]]) -> int:
    
    # Dimensions of grid
    n = len(grid)
    m = len(grid[0])

    # Depth-first search
    def dfs(i: int, j: int, visited: Set) -> int:
        # Stop at zero
        if grid[i][j] == 0:
            return 0
        # Mark node as visited
        visited.add((i, j))
        moves = []
        # Left 
        if j > 0 and (i, j-1) not in visited and grid[i][j-1] != 0:
            moves += [grid[i][j] + dfs(i, j-1, visited)]
        # Right
        if j < m - 1 and (i, j+1) not in visited and grid[i][j+1] != 0:
            moves += [grid[i][j] + dfs(i, j+1, visited)]
        # Up
        if i > 0 and (i-1, j) not in visited and grid[i-1][j] != 0:
            moves += [grid[i][j] + dfs(i-1, j, visited)]
        # Down
        if i < n - 1 and (i+1, j) not in visited and grid[i+1][j] != 0:
            moves += [grid[i][j] + dfs(i+1, j, visited)]
        # Remove from visited
        visited.remove((i, j))
        # No moves left
        if len(moves) == 0:
            return grid[i][j]
        # Return max gold path
        return max(moves)

    # Iterate over all starting points
    max_gold = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0:
                gold = dfs(i, j, set())
                if gold > max_gold:
                    max_gold = gold

    return max_gold

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        return getMaximumGold(grid)


if __name__ == "__main__":
    grid = [[0,6,0],[5,8,7],[0,9,0]]
    result = getMaximumGold(grid)
    print(result)
    grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
    result = getMaximumGold(grid)
    print(result)
