from typing import List

# https://leetcode.com/problems/single-number/

def singleNumber(nums: List[int]) -> int:
    """
    In an array, every element appears twice except 
    for one -> return this element.
    """
    return 2 * sum(set(nums)) - sum(nums)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return singleNumber(nums)
