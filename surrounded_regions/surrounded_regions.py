from typing import List, Set

# https://leetcode.com/problems/surrounded-regions/

def surroundedRegions(board: List[List[str]]):
    """
    Given a 2D board containing 'X' and 'O', capture all regions
    surrounded by 'X'. A region is captured by flipping all 'O' 
    into 'X' for the region.
    """
    # No board passed!
    if not board:
        return None
    # Number of rows, columns
    n = len(board)
    m = len(board[0])
    # Set region counter and edge set
    N = 1
    edge = set()
    # First pass over board: do DFS for 'O'
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'O':
                edge = dfsVisit(board, i, j, N, edge)
                N += 1
    # Second pass over board: flip non-edge to 'X', 
    # edge to 'O'
    for i in range(n):
        for j in range(m):
            if board[i][j] != 'X':
                if int(board[i][j]) in edge:
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

def dfsVisit(board: List[List[str]], i: int, j: int, N: int, edge: Set) -> Set:
    """
    Perform depth-first search on board at index (i, j).
    """
    # Number of rows, columns
    n = len(board)
    m = len(board[0])
    # Index must be on board
    if i < 0 or j < 0 or i >= n or j >= m:
        return edge
    # Value must be 'O'
    if board[i][j] != 'O':
        return edge
    # Mark index as part of region
    board[i][j] = str(N)
    # If index on edge, record it
    if i == 0 or j == 0 or i == n - 1 or j == m - 1:
        edge.add(N)
    # Visit adjacent values
    edge = dfsVisit(board, i-1, j, N, edge)
    edge = dfsVisit(board, i+1, j, N, edge)
    edge = dfsVisit(board, i, j-1, N, edge)
    edge = dfsVisit(board, i, j+1, N, edge)
    return edge

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        surroundedRegions(board)
