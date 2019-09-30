from math import floor
from typing import List

# https://leetcode.com/problems/search-insert-position/

def searchInsert(nums: List[int], target: int) -> int:
    """
    Given a sorted array and a target value, return the index 
    where the target is found. If not, return the index where
    it would be inserted in order. Use binary search.
    """
    # Length of array and midpoint index
    L = len(nums)
    mid = int(floor(L/2))
    # Match at beginning, end, midpoint
    if nums[0] >= target:
        return 0
    if nums[mid] == target:
        return mid
    if nums[L-1] == target:
        return L-1
    if nums[L-1] < target:
        return L
    # Recursively call on subarray to left or right of midpoint
    if nums[0] < target and nums[mid] > target:
        return searchInsert(nums[0:mid], target)
    if nums[mid] < target and nums[L-1] > target:
        return mid + searchInsert(nums[mid:], target)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return searchInsert(nums, target)
