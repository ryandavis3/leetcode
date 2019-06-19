from typing import List

def swap(A: List[int], i: int, j: int) -> None:
    """
    Swap elements i and j in list A in place.
    """
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

def sortColors(A: List[int]) -> None:
    """
    Sort numbers in place. Numbers are {0,1,2}. Use one pass
    with constant space.
    """
    # If array is length zero or one, return it
    if not A:
        return
    if len(A) == 1:
        return
    # i as left pointer, j as right pointer
    i = 0
    j = len(A) - 1
    # k holds the place of the first 1
    k = None
    # Iterate while left and right pointers do not cross
    while i <= j:
        # Value is 0. Swap with first 1 appearing before
        # 0. If no preceding 1s, just increment left pointer.
        if A[i] == 0:
            if k is not None:
                swap(A, i, k)
                k += 1
                # Find new first 1
                while A[k] != 1:
                    k += 1
                    if k == i:
                        k = None
                        break
            i += 1
        # Value is 2. Swap with value at right pointer.
        # Decrement right pointer.
        elif A[i] == 2:
            swap(A, i, j)
            j -= 1
        # Value is 1. If next value is 0, swap with it. Else,
        # increment counter.
        elif A[i] == 1:
            # Found first 1
            if k is None:
                k = i
            if i == j:
                i += 1
                continue
            if A[i+1] == 0:
                swap(A, i, i+1)
            else:
                i += 1

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        sortColors(nums)
