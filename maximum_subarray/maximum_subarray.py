from typing import List

# https://leetcode.com/problems/maximum-subarray/

def maxSubArray(nums: List[int]) -> int:
    """
    Given an integer array nums, find the contiguous
    subarray (containing at least one number) which has the 
    largest sum and return the sum.
    """
    for i, val in enumerate(nums):
        # Set max value and max contiguous value on first
        # iteration.
        if i == 0:
            max_val = val
            max_cont = val
            continue
        # Positive value and negative contiguous sum -> reset 
        # contiguous sum to include only value.
        if val > 0 and max_cont <= 0:
            max_cont = val
        # Value (not necessarily positive) greater than existing 
        # max value -> reset contiguous sum.
        elif val > max_val and max_cont <= 0:
            max_cont = val
        # Add value to contiguous sum.
        else:
            max_cont += val
        # Update max contiguous sum for full array.
        if max_cont > max_val:
            max_val = max_cont
    return max_val

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return maxSubArray(nums)
