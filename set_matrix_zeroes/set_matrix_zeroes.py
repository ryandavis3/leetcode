from typing import List

# https://leetcode.com/problems/set-matrix-zeroes/

def setZeroes(matrix: List[List[int]]) -> None:
    """
    Given a m x n matrix, if an element is zero, set
    its entire row and column to zero.
    """
    # Shape of matrix
    m = len(matrix)
    n = len(matrix[0])
    # Get unique row and column indices with zero
    R = set()
    C = set()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                R.add(i)
                C.add(j)
    # Set rows and cols to zero
    for row in R:
        for j in range(n):
            matrix[row][j] = 0
    for col in C:
        for i in range(m):
            matrix[i][col] = 0

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        setZeroes(matrix) 
