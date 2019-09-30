from typing import List

# https://leetcode.com/problems/rotate-image/

def rotate(matrix: List[List[int]]) -> None:
    """
    Rotate n x n 2D matrix by 90 degrees (clockwise).
    """
    # No matrix passed!
    if not matrix:
        return []
    # Dimensions and offset
    n = len(matrix)
    off = 0
    # Rotate perimeter one offset at a time
    while n - 2*off > 1:
        rotatePerimeter(matrix, off)
        off += 1

def rotatePerimeter(matrix: List[List[int]], off: int):
    """
    Rotate perimeter of image by 90 degrees (clockwise).
    """
    # Left and right from offset
    n = len(matrix)
    l = off
    r = n - off
    rng = range(l, r)
    # To row to rightmost column
    vals = [matrix[l][i] for i in rng]
    vals_n = [matrix[i][r-1] for i in rng]
    vals_nn = [matrix[-(l+1)][n-1-i] for i in rng]
    j = 0
    for i in rng:
        matrix[i][r-1] = vals[j]
        j += 1
    vals = vals_n
    vals_n = vals_nn
    # Rightmost column to bottom row
    vals_nn = [matrix[n-1-i][l] for i in rng]
    j = 0
    for i in rng:
        matrix[-(l+1)][n-1-i] = vals[j]
        j += 1
    vals = vals_n
    vals_n = vals_nn
    # Bottom row to leftmost column
    j = 0
    for i in rng:
        matrix[n-1-i][l] = vals[j]
        j += 1
    vals = vals_n
    # Leftmost column to top row
    j = 0
    for i in rng:
        matrix[l][i] = vals[j]
        j += 1

def printMatrix(matrix: List[List[int]]):
    """
    Print matrix line by line.
    """
    for line in matrix:
        print(line)
    print('')

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rotate(matrix)
