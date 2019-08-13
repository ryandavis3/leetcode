import copy
from typing import List, Dict, Set

# https://leetcode.com/problems/sudoku-solver/

# Use dict / set representation of board to allow
# O(1) time checking of constraints.

ALL_VALS = set(['1','2','3','4','5','6','7','8','9'])
SUBINDEX = {0:0, 1:0, 2:0, 3:1, 4:1, 5:1, 6:2, 7:2, 8:2}

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

def neededValues(vals: Dict) -> Dict:
    """
    Get needed values for rows and columns.
    """
    needed = {}
    for i in range(9):
        needed[i] = ALL_VALS - vals[i]
    return needed

def neededValuesSubBoard(vals: Dict) -> Dict:
    """
    Get needed values for sub-board.
    """
    needed = {}
    for i in range(3):
        needed[i] = {}
        for j in range(3):
            needed[i][j] = ALL_VALS - vals[i][j]
    return needed

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

def getEmptyCells(board: List[List[str]]):
    """
    Get empty cells on board.
    """
    # Populate dictionary on first pass
    empty = {}
    for i in range(9):
        empty[i] = set()
        for j in range(9):
            if board[i][j] == '.':
                empty[i].add(j)
    # Remove empty values
    for i in range(9):
        if not empty[i]:
            del empty[i]
    return empty

def getMinRow(empty: Dict) -> int:
    """
    Get minimum index of empty rows.
    """
    if not empty:
        return -1
    return min(empty.keys())

## TODO: Modify items directly rather than using deep copy,
## then undo if it does not work. Add function undoMove. 
## TODO: Maintain set of possible numbers for each empty cell.
## Update set when new number is added. Search space of numbers
## first with the cells with the fewest possible numbers.
## Should be able to get rid of needed rows, cols, sub-board
## and only maintain possible numbers.

class Board:
    """
    Class for Sudoku board.
    """
    def __init__(self, board: List[List[str]], 
            empty: Set, rows: Dict, cols: Dict, sub: Dict, min_row: int):
        """
        Constructor.
        """
        self.board = board
        self.empty = empty
        self.rows = rows
        self.cols = cols
        self.sub = sub
        self.min_row = min_row

    @classmethod
    def from_board(cls, board: List[List[str]]):
        """
        Instantiate class from only board values.
        """
        # Represent rows, cols, sub-boards, empty
        rows = representRows(board)
        cols = representCols(board)
        sub_boards = representSubBoards(board)
        empty = getEmptyCells(board)
        min_row = getMinRow(empty)
        rows = neededValues(rows)
        cols = neededValues(cols)
        sub = neededValuesSubBoard(sub_boards)
        return cls(board, empty, rows, cols, sub, min_row)

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
        sub_i = SUBINDEX[i]
        sub_j = SUBINDEX[j]
        if val in self.sub_boards[sub_i][sub_j]:
            return False
        # All constraints satisfied -> return True!
        return True

    @property
    def isFull(self):
        """
        Return True if Sudoku 
        """
        return len(self.empty) == 0

    def makeMove(self, i: int, j: int, val: str):
        """
        Add value val to index (i, j) on board.
        """
        # Update empty cells
        empty = copy.deepcopy(self.empty)
        min_row = self.min_row
        empty[i].remove(j)
        if not empty[i]:
            del empty[i]
            min_row = getMinRow(empty)
        # Update board
        board = copy.deepcopy(self.board)
        board[i][j] = val
        # Update needed rows
        rows = copy.deepcopy(self.rows)
        rows[i].remove(val)
        # Update needed columns
        cols = copy.deepcopy(self.cols)
        cols[j].remove(val)
        # Update sub-boards
        sub_i = SUBINDEX[i]
        sub_j = SUBINDEX[j]
        sub = copy.deepcopy(self.sub)
        sub[sub_i][sub_j].remove(val)
        # Return new board
        kwargs = {
            'board' : board,
            'empty' : empty,
            'rows' : rows,
            'cols' : cols,
            'sub' : sub,
            'min_row' : min_row,
        }
        return Board(**kwargs)

    def validNumbers(self, i: int, j: int):
        """
        Get valid numbers for index (i, j) that satisfy constraints.
        """
        sub_i = SUBINDEX[i]
        sub_j = SUBINDEX[j]
        return self.rows[i] & self.cols[j] & self.sub[sub_i][sub_j]

def findEmptyIndex(board: Board) -> List[int]:
    """
    Find earliest (i, j) pair on board with unassigned number.
    """
    j = min(board.empty[board.min_row])
    return [board.min_row, j]

def solve(board: Board):
    """
    Solve sudoku using backtracking.
    """
    # Finished sudoku board!!
    if board.isFull:
        return board
    # Choose (i, j) to which to add number
    [i, j] = findEmptyIndex(board)
    cand = board.validNumbers(i, j)
    # Consider each possible number to add 
    for val in cand:
        # Make move and recursively solve
        board_next = board.makeMove(i, j, val)
        board_next = solve(board_next)
        # Valid board return it!
        if board_next is not False:
            return board_next
    # No valid board found - return False
    return False

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        boardC = Board.from_board(board)
        boardC = solve(boardC)
        for i in range(9):
            for j in range(9):
                board[i][j] = boardC.board[i][j]
