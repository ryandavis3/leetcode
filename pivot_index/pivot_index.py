from typing import List

# https://leetcode.com/problems/find-pivot-index/

def pivotIndex(nums: List[int]):
    """
    Given an array of integers nums, return the first 
    "pivot" index of the array. 

    Define a pivot index as an index where the sum of
    the numbers of the left of the index is equal to the
    sum of the numbers to the right of the index.

    O(n)
    """
    if not nums:
        return -1
    # Initialize left sum as zero and right sum as sum
    # of all values in array.
    left = 0
    right = sum(nums)
    prev = 0
    # Iterate over each element in array, update left
    # and right sums
    for i, val in enumerate(nums):
        left += prev
        right -= val
        prev = val
        if left == right:
            return i
    return -1

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        return pivotIndex(nums)

