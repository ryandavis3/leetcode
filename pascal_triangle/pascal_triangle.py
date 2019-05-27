from typing import List

# https://leetcode.com/problems/pascals-triangle/

def buildTriangle(numRows: int) -> List[List[int]]: 
    """
    Build Pascal's triangle with numRows rows.
    """
    # Degenerate case
    if not numRows:
        return []
    # Initialize first three rows of list
    L = list()
    L.append([1])
    L.append([1, 1])
    L.append([1, 2, 1])
    if numRows <= 3:
        return L[:numRows]
    # Iterate over rows
    prev = L[-1]
    N = 4
    while N <= numRows:
        row = [None] * N
        row[0] = 1
        row[-1] = 1
        for i in range(1, N-1):
            row[i] = prev[i-1] + prev[i]
        prev = row
        L.append(row)
        N += 1
    return L

def printTriangle(L : List[List[int]]):
    """
    Print each row of Pscal's triangle at a time.
    """
    for line in L:
        print(line)

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return buildTriangle(numRows)
