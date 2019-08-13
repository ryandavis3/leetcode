from typing import List, Dict

# https://leetcode.com/problems/valid-sudoku/

def validSudoku(board: List[List[str]]) -> bool:
    """
    Return True if Sudoku board is valid, else
    return False.
    """
    # Row constraint
    for i in range(9):
        row_vals = set()
        for j in range(9):
            val = board[i][j]
            if val in row_vals:
                return False
            if val != '.':
                row_vals.add(val)
    # Column constraint
    for j in range(9):
        col_vals = set()
        for i in range(9):
            val = board[i][j]
            if val in col_vals:
                return False
            if val != '.':
                col_vals.add(val)
    # Sub-board constraint
    for i in range(3):
        for j in range(3):
            ii = 3 * i
            jj = 3 * j
            sub_vals = set()
            for k in range(3):
                for l in range(3):
                    val = board[ii+k][jj+l]
                    if val in sub_vals:
                        return False
                    if val != '.':
                        sub_vals.add(val)
    # All constraints satisfied!
    return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return validSudoku(board)
