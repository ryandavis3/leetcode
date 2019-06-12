from typing import List

# https://leetcode.com/problems/unique-paths-ii

def emptyTable(m: int, n: int) -> List[List[int]]:
    """
    Make empty m x n table full of zeros.
    """
    T = []
    for _ in range(m):
        T += [[0] * n]
    return T

def uniquePathsWithObstacles(G: List[List[int]]) -> int:
    """
    Find number of unique paths robot can take from top left to
    bottom right of grid.

    Args:
        G (m x n list of list of int): At (i,j), 1 if obstacle
            at (i,j), else 0. 

    Returns:
        int: Number of unique paths.
    """
    m = len(G)
    n = len(G[0])
    T = emptyTable(m, n)
    for i in range(m):
        for j in range(n):
            # Obstacle at (i,j); zero paths to get to (i,j)
            if G[i][j]:
                continue
            # Top left corner; starting point
            if not i and not j:
                T[i][j] = 1
                continue
            # Can arrive from left or top
            paths = 0
            if i > 0:
                paths += T[i-1][j]
            if j > 0:
                paths += T[i][j-1]
            T[i][j] = paths
    return T[-1][-1]


class Solution:
    def uniquePathsWithObstacles(self, G: List[List[int]]) -> int:
        return uniquePathsWithObstacles(G)
