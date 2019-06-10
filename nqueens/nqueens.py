from typing import List

# N-Queens Problem
# https://leetcode.com/problems/n-queens/

def emptyBoard(N: int) -> List[List[int]]:
    """
    Build empty NxN board.
    """
    board = []
    for _ in range(N):
        board += [[0]*N]
    return board

def printBoard(board: List[List[int]]) -> None:
    for line in board:
        print(line)

def isSafe(board: List[List[int]], row: int, col: int, N: int) -> bool:
    """
    Return true if queens can safely be placed on board
    at row, col. Otherwise return False.
    
    This function should be called when queens have been
    placed from column 0 to col-1.
    """
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
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1
    return True

def solve(board: List[List[int]], col: int, N: int):
    """
    Recursively solve N-Queens problem by placing a 
    queen in column col.
    """
    # If all queens are placed, return True
    if col >= N:
        return True
    # Try to place queen in all rows one by one
    for i in range(N):
        if isSafe(board, i, col, N):
            board[i][col] = 1
            if solve(board, col+1, N):
                return True
            board[i][col] = 0
    return False

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        pass
