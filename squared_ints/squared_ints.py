from typing import List

# https://leetcode.com/problems/squares-of-a-sorted-array/

def sortedSquares(A: List[int]) -> List[int]:
    """
    Given an array of integers A sorted in non-decreasing 
    order, return an array of the squares of each number, also
    sorted in non-decreasing order.
    """
    A = [x**2 for x in A]
    A = sorted(A)
    return A

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sortedSquares(A)
