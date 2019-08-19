import copy
from typing import List

# https://leetcode.com/problems/word-search/

def search(board: List[List[str]], word: str, i: str, j: str) -> bool:
    """
    Recursively search for word on board. Return True if
    we find word, else return False.
    """
    # Board dimensions
    m = len(board)
    n = len(board[0])
    # Completed word!
    if not word: 
        return True
    # Mark index in board as visited
    board[i][j] = 'XX'
    # Character, word after character
    char = word[0]
    word_next = word[1:]
    result = []
    # Search right
    if j < n - 1:
        if board[i][j+1] == char:
            if search(board, word_next, i, j+1):
                return True
            board[i][j+1] = char
    # Search left 
    if j > 0:
        if board[i][j-1] == char:
            if search(board, word_next, i, j-1):
                return True
            board[i][j-1] = char
    # Search down
    if i < m - 1:
        if board[i+1][j] == char:
            if search(board, word_next, i+1, j):
                return True
            board[i+1][j] = char
    # Search up
    if i > 0:
        if board[i-1][j] == char:
            if search(board, word_next, i-1, j):
                return True
            board[i-1][j] = char
    return False

def exist(board: List[List[str]], word: str) -> bool:
    """
    Given a 2D board and word, find if word exists in grid.
    """
    # Board dimensions
    m = len(board)
    n = len(board[0])
    # Empty word passed!
    if not word:
        return True
    # Character, word
    char = word[0]
    word_next = word[1:]
    # Try each starting position
    for i in range(m):
        for j in range(n):
            # Search further if first character matches
            if board[i][j] == char:
                # Found match - return True!
                char = board[i][j]
                if search(board, word_next, i, j):
                    return True
                board[i][j] = char
    # No match found - return False
    return False

def printBoard(board: List[List[str]]) -> None:
    """
    Print board to stdout.
    """
    for line in board:
        print(line)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return exist(board, word)
