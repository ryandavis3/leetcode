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

## TODO: Get faster solution using dynamic programming.

def search(matrix: List[List[str]], i: int, j: int, m: int, n: int, memo: Dict) -> int:
    """
    Use depth-first search to find largest rectangle containing 
    only ones inlcuding 1 at (i, j).
    """
    # If we have memoized solution already, return it! 
    rectangle_id = tuple([i, j, m, n])
    if rectangle_id in memo:
        return [memo[rectangle_id], memo]
    # Dimensions of matrix
    rows = len(matrix)
    cols = len(matrix[0])
    # Set initial max area to area of current rectangle
    max_area = m*n
    # Search right
    j_r = j + n
    if j_r < cols:
        if checkVerticalOnes(matrix, i, j_r, m):
            markVerticalOnes(matrix, i, j_r, m, X=True)
            [max_area_n, memo] = search(matrix, i, j, m, n+1, memo)
            if max_area_n > max_area:
                max_area = max_area_n
            markVerticalOnes(matrix, i, j_r, m, X=False)
    # Search left
    j_l = j - 1
    if j_l > -1:
        if checkVerticalOnes(matrix, i, j_l, m):
            markVerticalOnes(matrix, i, j_l, m, X=True)
            [max_area_n, memo] = search(matrix, i, j_l, m, n+1, memo)
            if max_area_n > max_area:
                max_area = max_area_n
            markVerticalOnes(matrix, i, j_l, m, X=False)
    # Search up 
    i_u = i - 1
    if i_u > -1:
        if checkHorizontalOnes(matrix, i_u, j, n):
            markHorizontalOnes(matrix, i_u, j, n, X=True)
            [max_area_n, memo] = search(matrix, i_u, j, m+1, n, memo)
            if max_area_n > max_area:
                max_area = max_area_n
            markHorizontalOnes(matrix, i_u, j, n, X=False)
    # Search down
    i_d = i + m
    if i_d < rows:
        if checkHorizontalOnes(matrix, i_d, j, n):
            markHorizontalOnes(matrix, i_d, j, n, X=True)
            [max_area_n, memo] = search(matrix, i, j, m+1, n, memo)
            if max_area_n > max_area:
                max_area = max_area_n
            markHorizontalOnes(matrix, i_d, j, n, X=False)
    # Memoize result
    memo[rectangle_id] = max_area
    return [max_area, memo]

def maximalRectangle(matrix: List[List[str]]) -> int:
    """
    Given a 2D binary matrix filled with zeros and ones, find the largest
    rectangle containing only ones and return its area.
    """
    # No matrix passed!
    if not matrix:
        return 0
    # Dimensions of matrix
    rows = len(matrix)
    cols = len(matrix[0])
    # Set initial max area to zero
    max_area = 0
    memo = {}
    # Iterate over each possible start point
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
    """
    Print matrix line by line.
    """
    for line in matrix:
        print(line)

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        [max_area, memo] = maximalRectangle(matrix)
        return max_area
