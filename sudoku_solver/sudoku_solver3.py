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

def getEmptyCells2(board: List[List[str]]):

    empty = set()
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                index = tuple([i, j])
                empty.add(index)
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

def getCandidateNumbers(board: List[List[int]], rows: Dict, cols: Dict, sub: Dict) -> List:
    """
    Get candidate numbers
    """
    candidates = {}
    n_candidates = {}
    for i in range(9):
        candidates[i] = {}
        for j in range(9):
            if board[i][j] == '.':
                sub_i = SUBINDEX[i]
                sub_j = SUBINDEX[j]
                candidates[i][j] = rows[i] & cols[j] & sub[sub_i][sub_j]
                index = tuple([i, j])
                n_candidates[index] = len(candidates[i][j])
    return [candidates, n_candidates]

def updateCandidates(i: int, j: int, val: str, candidates: Dict, n_candidates: Dict) -> List:
    """
    Update candidate numbers after move.
    """
    # No candidates for (i, j) -> we are adding value
    index = tuple([i, j])
    del n_candidates[index]
    del candidates[i][j]
    # Row constraint
    remove = set()
    for jj in range(9):
        if i in candidates:
            if jj in candidates[i]:
                if val in candidates[i][jj]:
                    index = tuple([i, jj])
                    remove.add(index)
    # Column constraint
    for ii in range(9):
        if ii in candidates:
            if j in candidates[ii]:
                if val in candidates[ii][j]:
                    index = tuple([ii, j])
                    remove.add(index)
    # Sub-board constraint
    sub_i = SUBINDEX[i]
    sub_j = SUBINDEX[j] 
    for ii in range(3*sub_i, 3*(sub_i+1)):
        for jj in range(3*sub_j, 3*(sub_j+1)):
            if ii in candidates:
                if jj in candidates[ii]:
                    if val in candidates[ii][jj]:
                        index = tuple([ii, jj])
                        remove.add(index)
    # Remove values
    for index in remove:
        [ii, jj] = index
        if jj in candidates[ii]:
            candidates[ii][jj].remove(val)
        if index in n_candidates:
            n_candidates[index] -= 1
            if n_candidates[index] == 0:
                del n_candidates[index]
    return [candidates, n_candidates]

class Board:
    """
    Class for Sudoku board.
    """
    def __init__(self, board: List[List[str]], 
            empty: Set, rows: Dict, cols: Dict, sub: Dict, min_row: int,
            candidates: Dict, n_candidates: Dict):
        """
        Constructor.
        """
        self.board = board
        self.empty = empty
        self.rows = rows
        self.cols = cols
        self.sub = sub
        self.min_row = min_row
        self.candidates = candidates
        self.n_candidates = n_candidates

    @classmethod
    def from_board(cls, board: List[List[str]]):
        """
        Instantiate class from only board values.
        """
        # Represent rows, cols, sub-boards, empty
        rows = representRows(board)
        cols = representCols(board)
        sub_boards = representSubBoards(board)
        empty = getEmptyCells2(board)
        min_row = 0 #getMinRow(empty)
        rows = neededValues(rows)
        cols = neededValues(cols)
        sub = neededValuesSubBoard(sub_boards)
        [candidates, n_candidates] = getCandidateNumbers(board, rows, cols, sub)
        return cls(board, empty, rows, cols, sub, min_row, candidates, n_candidates)

    @property
    def isFull(self):
        """
        Return True if Sudoku 
        """
        #return len(self.n_candidates) == 0
        return len(self.empty) == 0

    def makeMove(self, i: int, j: int, val: str):
        """
        Add value val to index (i, j) on board.
        """
        # Update empty cells
        index = tuple([i, j])
        empty = copy.deepcopy(self.empty)
        if index in empty:
            empty.remove(index)
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
        #sub[sub_i][sub_j].remove(val)
        # Update candidates
        candidates = copy.deepcopy(self.candidates)
        n_candidates = copy.deepcopy(self.n_candidates)
        [candidates, n_candidates] = updateCandidates(i, j, val, candidates, n_candidates)
        # Return new board
        kwargs = {
            'board' : board,
            'empty' : empty,
            'rows' : rows,
            'cols' : cols,
            'sub' : sub,
            'min_row' : self.min_row,
            'candidates' : candidates,
            'n_candidates' : n_candidates,
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
    #print(board.n_candidates)
    #print(board.board)
    #print(board.empty)
    if not board.n_candidates:
        return False
    # Choose (i, j) to which to add number
    #[i, j] = findEmptyIndex(board)
    [i, j] = min(board.n_candidates, key=board.n_candidates.get)
    #cand = board.validNumbers(i, j)
    cand = board.candidates[i][j]
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
