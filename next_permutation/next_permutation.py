from typing import List

# https://leetcode.com/problems/next-permutation

def swap(a: List[int], i: int, j: int) -> None:
    """
    Swap elements i and j of list in-place.
    """ 
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def reverse(a: List[int], i: int, j: int) -> None:
    """
    Reverse in place elements of a list between indices 
    i and j.
    """
    while i <= j:
        swap(a, i, j)
        i += 1
        j -= 1

def nextPerm(a: List[int]) -> None:
    """
    Imeplement list of numbers into the lexicographically 
    next greater permutation of numbers.
    """
    N = len(a)
    i = N-1
    # Find first decreasing element
    while i > 0:
        if a[i-1] < a[i]:
            break
        i -= 1
    # No decreasing element found; sort array in ascending
    # order
    if not i:
        reverse(a, 0, N-1)
    else:
        # Find number just larger than a[i-1] and swap with 
        # a[i-1].
        j = i
        while j < N-1:
            if a[j+1] <= a[i-1]:
                break
            j += 1
        swap(a, i-1, j)
        # a[i:] is increasing from right to left. Reverse elements
        # in substring so a[i:] is minimized.
        reverse(a, i, N-1)

class Solution:
    def nextPermutation(self, a: List[int]) -> None:
        nextPerm(a)
