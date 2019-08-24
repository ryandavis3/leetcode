from typing import List

# https://leetcode.com/problems/maximal-rectangle/

def emptyMatrix(rows: int, cols: int) -> List[List[str]]:
    """
    Create empty matrix of zeros.
    """
    M = []
    for _ in range(rows):
        M += [[0] * cols]
    return M

def consecutive(arr: List[str]) -> List[int]:
    """
    Given list arr of 1's and 0's return a list where element i
    gives the number of consecutive ones in arr ending in position i.
    """
    l = len(arr)
    C = [0] * l
    n = 0
    for i, val in enumerate(arr):
        if arr[i] == "1":
            n += 1
        else:
            n = 0
        C[i] = n
    return C

def transpose(M: List[List[str]]) -> List[List[str]]:
    
    rows = len(M)
    cols = len(M[0])
    MT = emptyMatrix(cols, rows)
    for i in range(rows):
        for j in range(cols)
            MT[j][i] = M[i][j]
    return MT

def printMatrix(matrix: List[List[str]]) -> None:
    """
    Print matrix line by line.
    """
    for line in matrix:
        print(line)

def maximalRectangle(matrix: List[List[str]]) -> int:

    # Dimensions of matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Matrices for length, width, area of maximal rectangles
    L = emptyMatrix(rows, cols)
    H = emptyMatrix(rows, cols)
    A = emptyMatrix(rows, cols)

    # First row
    C = consecutive(matrix[0])
    L[0] = C
    A[0] = C
    for j in range(len(C)):
        if C[j] > 0:
            H[0][j] = 1

    # Rows after first
    for i in range(1, rows):
        C = consecutive(matrix[i])
        for j in range(cols):
            if C[j] > 0: 
                H[i][j] = 1
                L[i][j] = C[j]
                A[i][j] = C[j]
                if A[i][j] > 0:
                    h = H[i-1][j] + 1
                    l = min(L[i-1][j], C[j])
                    a = h * l
                    if a > A[i][j]:
                        A[i][j] = a
                        L[i][j] = l
                        H[i][j] = h
    return [L, H, A]

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        [L, H, A] = maximalRectangle(matrix)
        matrix_T = transpose(matrix)
        [LT, HT, AT] = maximalRectangle(matrix_T)
        return max(max([max(l) for l in A]), max([max(l) for l in AT])
