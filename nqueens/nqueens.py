from typing import List

# N-Queens Problem
# https://leetcode.com/problems/n-queens/

def isSafe(board: List[List[int]], row: int, col: int) -> bool:
    """
    Return true if queens can safely be placed on board
    at row, col. Otherwise return False.
    
    This function should be called when queens have been
    placed from column 0 to col-1.
    """
    N = len(board)
    # Queens in same row
    for j in range(col):
        if board[row][j]:
            return False
    # Queens on left lower diagonal
    i = row + 1
    j = col - 1
    while i < N and j >= 0:
        if board[i][j]:
            return False
        i += 1
        j -= 1
    # Queens on left upper diagonal
    i = row + 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1
    return True

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        pass
