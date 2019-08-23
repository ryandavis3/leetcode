from typing import List, Dict

# https://leetcode.com/problems/maximal-rectangle/

def checkVerticalOnes(matrix: List[List[str]], i: int, j: int, l: int) -> bool:
    """
    Return True if vertical column has all ones (and can be used
    to expand rectangle), else return False.
    """
    for k in range(i, i+l):
        if matrix[k][j] != "1":
            return False
    return True

def checkHorizontalOnes(matrix: List[List[str]], i: int, j: int, l: int) -> bool:
    """
    Return True if horizontal row has all ones (and can be used
    to expand rectangle), else return False.
    """
    for k in range(j, j+l):
        if matrix[i][k] != "1":
            return False
    return True

def markVerticalOnes(matrix: List[List[str]], i: int, j: int, l: int, X: bool) -> bool:
    """
    Mark vertical ones with 'X' or '1'.
    """
    if X:
        val = "X"
    else:
        val = "1"
    for k in range(i, i+l):
        matrix[k][j] = val

def markHorizontalOnes(matrix: List[List[str]], i: int, j: int, l: int, X: bool) -> bool:
    """
    Mark horizontal ones with 'X' or '1'.
    """
    if X:
        val = "X"
    else:
        val = "1"
    for k in range(j, j+l):
        matrix[i][k] = val

def inMemo(memo: Dict, i: int, j: int, m: int, n: int) -> bool:
    if i not in memo:
        return False
    if j not in memo[i]:
        return False
    if m not in memo[i][j]:
        return False
    if n not in memo[i][j][m]:
        return False
    return True

def addToMemo(memo: Dict, i: int, j: int, m: int, n: int, val: int) -> None:
    if i not in memo:
        memo[i] = {}
    if j not in memo[i]:
        memo[i][j] = {}
    if m not in memo[i][j]:
        memo[i][j][m] = {}
    memo[i][j][m][n] = val

## TODO: Use nested dict for memoization. Faster lookup. 
## TODO: Prune search directions where we cannot improve on current solution.

def search(matrix: List[List[str]], i: int, j: int, m: int, n: int, memo: Dict) -> int:
    """
    Use depth-first search to find largest rectangle containing 
    only ones inlcuding 1 at (i, j).
    """
    # If we have memoized solution already, return it! 
    if inMemo(memo, i, j, m, n):
        return [memo[i][j][m][n], memo]

    # Dimensions of matrix
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Set initial max area to area of current rectangle
    max_area = m*n

    # Search right
    j_r = j + n
    if j_r < cols:
        if n * (cols - j) > max_area:
            if checkVerticalOnes(matrix, i, j_r, m):
                markVerticalOnes(matrix, i, j_r, m, X=True)
                [max_area_n, memo] = search(matrix, i, j, m, n+1, memo)
                if max_area_n > max_area:
                    max_area = max_area_n
                markVerticalOnes(matrix, i, j_r, m, X=False)

    # Search left
    j_l = j - 1
    if j_l > -1:
        if n * (j + m) > max_area:
            if checkVerticalOnes(matrix, i, j_l, m):
                markVerticalOnes(matrix, i, j_l, m, X=True)
                [max_area_n, memo] = search(matrix, i, j_l, m, n+1, memo)
                if max_area_n > max_area:
                    max_area = max_area_n
                markVerticalOnes(matrix, i, j_l, m, X=False)

    # Search up 
    i_u = i - 1
    if i_u > -1:
        if m * (i + n) > max_area:
            if checkHorizontalOnes(matrix, i_u, j, n):
                markHorizontalOnes(matrix, i_u, j, n, X=True)
                [max_area_n, memo] = search(matrix, i_u, j, m+1, n, memo)
                if max_area_n > max_area:
                    max_area = max_area_n
                markHorizontalOnes(matrix, i_u, j, n, X=False)

    # Search down
    i_d = i + m
    if i_d < rows:
        if m * (rows - i) > max_area:
            if checkHorizontalOnes(matrix, i_d, j, n):
                markHorizontalOnes(matrix, i_d, j, n, X=True)
                [max_area_n, memo] = search(matrix, i, j, m+1, n, memo)
                if max_area_n > max_area:
                    max_area = max_area_n
                markHorizontalOnes(matrix, i_d, j, n, X=False)

    # Memoize result
    addToMemo(memo, i, j, m, n, max_area)
    return [max_area, memo]

def maximalRectangle(matrix: List[List[str]]) -> int:

    # No matrix passed!
    if not matrix:
        return 0

    # Dimensions of matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Set initial max area to zero
    max_area = 0
    memo = {}

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "1":
                matrix[i][j] = "X"
                [max_area_ij, memo] = search(matrix, i, j, 1, 1, memo)
                if max_area_ij > max_area:
                    max_area = max_area_ij
                matrix[i][j] = "1"

    return [max_area, memo]

def printMatrix(matrix: List[List[str]]) -> None:
    for line in matrix:
        print(line)

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        [max_area, memo] = maximalRectangle(matrix)
        return max_area
