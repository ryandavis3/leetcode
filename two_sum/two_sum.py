from typing import List

# https://leetcode.com/problems/two-sum/

def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers, return indices of the two
    numbers such that they add to a specific target.
    
    Use single O(n) pass with hash table (dictionary).
    """
    D = {}
    for i, num in enumerate(nums):
        if target-num in D:
            return [D[target-num], i]
        D[num] = i
    return None


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return twoSum(nums, target)
