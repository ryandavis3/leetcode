from typing import Set, List

def uniquePathsIII(grid: List[List[int]]) -> int:
    
    # Initialize unvisited set
    unvisited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] in {0, 1}:
                unvisited.add((i, j))
            if grid[i][j] == 1:
                starti = i
                startj = j

    # Dimensions
    n = len(grid)
    m = len(grid[0])

    def backtrack(i: int, j: int, visited: Set, unvisited: Set) -> int:
   
        # Reached the end
        if grid[i][j] == 2:
            if len(unvisited) == 0:
                return 1
            else:
                return 0
        # Reached obstacle
        if grid[i][j] == -1:
            return 0
        # Mark as visited
        visited = visited.union({(i, j)})
        unvisited = unvisited - {(i, j)}
        moves = 0
        # Left
        if j > 0 and (i, j - 1) not in visited:
            moves += backtrack(i, j - 1, visited, unvisited)
        # Right
        if j < m - 1 and (i, j + 1) not in visited:
            moves += backtrack(i, j + 1, visited, unvisited)
        # Up
        if i > 0 and (i - 1, j) not in visited:
            moves += backtrack(i - 1, j, visited, unvisited)
        # Down
        if i < n - 1 and (i + 1, j) not in visited:
            moves += backtrack(i + 1, j, visited, unvisited)

        return moves

    return backtrack(starti, startj, set(), unvisited) 
        

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        return uniquePathsIII(grid)


if __name__ == "__main__":
    grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    result = uniquePathsIII(grid)
    print(result)
    grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
    result1 = uniquePathsIII(grid)
    print(result1)
