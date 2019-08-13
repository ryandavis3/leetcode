import copy
from typing import List, Dict, Set

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

def getEmptyCells(board: List[List[str]]) -> Set:
    """
    Return set of empty cells from board.
    """
    empty = set()
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                empty.add(tuple([i, j]))
    return empty

## TODO: Initialize list of empty cells. Update list when
## number is added. 
## TODO: Member function to make move (add number) on board.
## TODO: Backtracking to find solution. 

class Board:
    """
    Class for Sudoku board.
    """
    def __init__(self, board: List[List[str]], rows: Dict, 
            cols: Dict, sub_boards: Dict, empty: Set):
        """
        Constructor.
        """
        self.board = board
        # Rows
        if not rows:
            self.rows = representRows(board)
        else:
            self.rows = rows
        # Columns
        if not cols:
            self.cols = representCols(board)
        else:
            self.cols = cols
        # Sub-boards
        if not sub_boards:
            self.sub_boards = representSubBoards(board)
        else:
            self.sub_boards = sub_boards
        # Empty cells
        if not empty:
            self.empty = getEmptyCells(board)
        else:
            self.empty = empty

    @classmethod
    def from_board(cls, board: List[List[str]]):
        rows = representRows(board)
        cols = representCols(board)
        sub_boards = representSubBoards(board)
        empty = getEmptyCells(board)
        return cls(board, rows, cols, sub_boards, empty)

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

    def makeMove(self, i: int, j: int, val: str):
        """
        Add value val to index (i, j) on board.
        """
        # Update row sets
        rows = copy.deepcopy(self.rows)
        rows[i].add(val)
        # Update column sets
        cols = copy.deepcopy(self.cols)
        cols[j].add(val)
        # Update sub-boards
        sub_i = subBoardIndex(i)
        sub_j = subBoardIndex(j)
        sub_boards = copy.deepcopy(self.sub_boards)
        sub_boards[sub_i][sub_j].add(val)
        # Update empty cells
        empty = self.empty - set([tuple([i, j])])
        # Update board
        board = copy.deepcopy(self.board)
        board[i][j] = val
        # Return new board
        kwargs = {
            'board' : board,
            'rows' : rows,
            'cols' : cols,
            'sub_boards' : sub_boards,
            'empty' : empty
        }
        return Board(**kwargs)

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        pass 
