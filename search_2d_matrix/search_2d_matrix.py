import math
from typing import List

## Binary search to find correct row, then binary search to 
## find correct column. O(log(m+n))

def findRow(M: List[List[int]], target: int) -> int:
    """
    Find row where target integer could be. If there is no row
    where target could be, return None. Use binary search.
    """
    # Missing data -> return None
    if not M:
        return None
    if not M[0]:
        return None
    m = len(M)
    # Only one row -> return it
    if m == 1:
        return 0
    i = math.floor(m/2)
    N = 2
    step = i
    while True:
        if not i:
            return None
        # Update step length
        step = max(1, math.floor(step/2))
        # Found candidate row
        if M[i][0] > target and M[i-1][0] <= target:
            return i-1
        elif i == m-1 and M[i][0] <= target:
            return i
        elif i == 0 and M[i][0] > target:
            return None
        # Halve search space and iterate
        elif M[i-1][0] > target:
            i = max(0, i-step)
        elif M[i][0] <= target:
            i = min(m-1, i+step)
        N += 1
    return None

def findValue(L: List[int], target: int) -> bool:
    """
    Return True if target in list L, else return False. Use
    binary search.
    """
    if not L:
        return False
    n = len(L)
    i = math.floor(n/2)
    step = i
    N = 2
    # For small case n=2, check each value
    if n == 2:
        if target in L:
            return True
        return False
    while True:
        # Found target!
        if L[i] == target:
            return True
        # If we are at left or right end of list and 
        # endpoint value not equal to target, return False
        if i == 0 and L[i] != target:
            return False
        if i == n-1 and L[i] != target:
            return False
        # If target "between" two adjacent values, return False
        if L[i] > target and L[i-1] < target:
            return False
        if L[i] < target and L[i+1] > target:
            return False
        # Halve search space
        step = max(1, math.floor(step/2))
        if L[i] > target:
            i -= step
        else: # L[i] < target
            i += step
        N += 1
    return False

def searchMatrix(M: List[List[int]], target: int) -> bool:
    """
    Search matrix M for target value. Use binary search.
    """
    # Find candidate row. If no candidate row, return False.
    row = findRow(M, target)
    if row is None:
        return False
    # Try to find value in candidate row.
    return findValue(M[row], target)

class Solution:
    def searchMatrix(self, M: List[List[int]], target: int) -> bool:
        return searchMatrix(M, target)
