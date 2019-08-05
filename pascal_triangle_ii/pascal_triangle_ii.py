from typing import List

# https://leetcode.com/problems/pascals-triangle-ii/

def nextRow(row: List[int]) -> List[int]:
    """
    Compute next row of Pascal's triangle given row.
    """
    L = len(row)
    row_next = [None] * (L+1)
    row_next[0] = 1
    for i in range(L-1):
        row_next[i+1] = row[i] + row[i+1]
    row_next[L] = 1
    return row_next

def getRow(rowIndex: int) -> List[int]:
    """
    Return row of Pascal's triangle given index.
    """
    if rowIndex == 0:
        return [1]
    row = [1,1]
    if rowIndex == 1:
        return row
    k = 1
    while k < rowIndex:
        row = nextRow(row)
        k += 1
    return row

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return getRow(rowIndex)
