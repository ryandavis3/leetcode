from typing import List

# https://leetcode.com/problems/maximum-product-subarray/

def maxProductPass(nums: List[int]) -> int:
    """
    Given an integer array nums, find the contiguous 
    subarray within an array which has the largest 
    product. Do one pass from left to right.
    """
    maxProd = -100
    currProd = 1
    for num in nums:
        # "Reset" current product
        if num == 0:
            if 0 > maxProd:
                maxProd = 0
            currProd = 1
            continue
        # Update current product
        currProd = currProd * num
        if currProd > maxProd:
            maxProd = currProd
    return maxProd

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Perform a left to right pass and right to left pass.
        Take the max product between them.
        """
        mp = maxProductPass(nums)
        mpr = maxProductPass(list(reversed(nums)))
        return max(mp, mpr)
