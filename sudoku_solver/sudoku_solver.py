from typing import List, Dict

# https://leetcode.com/problems/sudoku-solver/

# Use dict / set representation of board to allow
# O(1) time checking of constraints.

def representRows(board: List[List[str]]) -> Dict:
    """
    Represent rows on board using dict of sets.
    """
    R = {}
    for i in range(9):
        R[i] = set()
        for j in range(9):
            val = board[i][j]
            if val != '.':
                R[i].add(val)
    return R

def representCols(board: List[List[str]]) -> Dict:
    """
    Represent columns on board using dict of sets.
    """
    C = {}
    for j in range(9):
        C[j] = set()
        for i in range(9):
            val = board[i][j]
            if val != '.':
                C[j].add(val)
    return C

def representSubBoards(board: List[List[str]]) -> Dict:
    """
    Represent 3x3 sub-boards using nested dict of sets.
    """
    S = {}
    for i in range(3):
        S[i] = {}
        for j in range(3):
            S[i][j] = set()
            ii = 3 * i
            jj = 3 * j
            for k in range(3):
                for l in range(3):
                    val = board[ii+k][jj+l]
                    if val != '.':
                        S[i][j].add(val)
    return S

def subBoardIndex(k: int) -> List:
    """
    Map row or column index k to a sub-board index 0-2. 
    """
    if k < 3:
        return 0
    elif k < 6:
        return 1
    else:
        return 2

class Board:
    """
    Class for Sudoku board.
    """
    def __init__(self, board: List[List[str]]):
        """
        Constructor.
        """
        self.board = board
        self.rows = representRows(board)
        self.cols = representCols(board)
        self.sub_boards = representSubBoards(board)
    
    def validMove(self, i: int, j: int, val: str) -> bool:
        """
        Return True if we can place val at position (i, j), 
        else return False.
        """
        # Row constraint
        if val in self.rows[i]:
            return False
        # Column constraint
        if val in self.cols[j]:
            return False
        # Sub-board constraint
        sub_i = subBoardIndex(i)
        sub_j = subBoardIndex(j)
        if val in self.sub_boards[sub_i][sub_j]:
            return False
        # All constraints satisfied -> return True!
        return True


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        pass 
