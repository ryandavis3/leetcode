from typing import List

# https://leetcode.com/problems/minimum-path-sum/

def emptyTable(m: int, n: int) -> List[List[int]]:
    """
    Make empty m x n table full of zeros.
    """
    T = []
    for _ in range(m):
        T += [[0] * n]
    return T

def minPathSum(G: List[List[int]]) -> int:
    """
    Given a m x n grid filled with non-negative numbers (G), find a 
    path from top left to bottom right which minimizes the sum of all 
    numbers along its path.
    """
    m = len(G)
    n = len(G[0])
    T = emptyTable(m, n)
    for i in range(m):
        for j in range(n):
            # Top left corner; starting point
            if not i and not j:
                T[i][j] = G[i][j]
                continue
            # Can arrive from left or top
            if i == 0:
                T[i][j] = T[i][j-1] + G[i][j]
            elif j == 0:
                T[i][j] = T[i-1][j] + G[i][j]
            else:
                T[i][j] = min([T[i][j-1], T[i-1][j]]) + G[i][j]
    return T[-1][-1]

class Solution:
    def minPathSum(self, G: List[List[int]]) -> int:
        return minPathSum(G)
