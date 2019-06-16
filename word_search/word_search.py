from typing import List, Set
from collections import Counter

# https://leetcode.com/problems/word-search/

def search(board: List[List[str]], word: str, used: Set, i: int, j: int, m: int, n: int) -> bool:
    """
    Recursively search for word on board.
    """
    used = used.copy()
    # Word is empty string - done!
    if not word:
        return True
    # Cannot use the same letter cell more than once
    if tuple([i, j]) in used:
        return False
    # Character to find
    char = word[0]
    # Indices must be in bounds
    if i < 0 or i >= m:
        return False
    if j < 0 or j >= n:
        return False
    # If board value not character, return False. Else, search
    # for a new word with the first character removed.
    if board[i][j] != char:
        return False
    word = word[1:]
    used.add(tuple([i, j]))
    # Search horizontal and vertical moves.
    left = search(board, word, used, i, j-1, m, n)
    right = search(board, word, used, i, j+1, m, n)
    up = search(board, word, used, i-1, j, m, n)
    down = search(board, word, used, i+1, j, m, n)
    # If one of the directions work, our search is succesful.
    return max([left, right, up, down]) 

def flatten_board(board: List[List[str]]) -> List[str]:
    """
    Flatten board from list of list of int to list of int.
    """
    _flat = []
    for line in board:
        _flat += line
    return _flat

def exist(board: List[List[str]], word: str):
    """
    Search for full word on board. Try each letter on board as 
    a starting letter.
    """
    if not word:
        return True
    if not board:
        return False
    m = len(board)
    n = len(board[0])
    if len(word) > m * n:
        return False
    for i in range(m):
        for j in range(n):
            if search(board, word, set(), i, j, m, n):
                return True
    return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return exist(board, word)
