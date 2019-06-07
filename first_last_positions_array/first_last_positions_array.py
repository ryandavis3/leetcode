import math
from typing import List

# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

def searchFirst(nums: List[int], target: int) -> List[int]:
    """
    Search for first position of element in sorted array. Return -1 
    if element not found.
    """
    L = len(nums)
    i = math.floor(L/2)
    N = 2
    while True:
        # Step size halves on each iteration
        step = max(1, math.floor(L / (2*N)))
        # Found first at beginning of array
        if nums[i] == target and i == 0:
            break
        # First element in array larger than target;
        # target not in array.
        if nums[i] > target and i == 0:
            return -1
        # Last element in array smaller than target; 
        # target not in array.
        if nums[i] < target and i == L-1:
            return -1
        # Found target!
        if nums[i] == target and nums[i-1] != target:
            break
        if nums[i] > target and nums[i-1] < target:
            return -1
        # Move index using binary search
        if nums[i] >= target:
            i -= step
        else:
            i += step
        N += 1
        # Make sure index within array boundaries
        i = max(i, 0)
        i = min(i, L-1)
    return i

def searchLast(nums: List[int], target: int) -> List[int]:
    """
    Search for last position of element in sorted array. Return -1
    if element not found.
    """
    L = len(nums)
    i = math.floor(L/2)
    N = 2
    while True:
        step = max(1, math.floor(L / (2*N)))
        if nums[i] > target and i == 0:
            return -1
        if nums[i] == target and i == L-1:
            break
        if nums[i] < target and i == L-1:
            return -1
        if nums[i] == target and nums[i+1] != target:
            break
        if nums[i] < target and nums[i+1] > target:
            return -1
        if nums[i] <= target:
            i += step
        else:
            i -= step
        i = min(i, L-1)
        i = max(i, 0)
        N += 1
    return i

def searchRange(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers sorted in ascending order, find the
    starting and ending position of a given target value. If the
    target is not found in the array, return [-1, 1]. 

    Use binary search to run in O(log n) time.
    """
    if not nums:
        return [-1, -1]
    first = searchFirst(nums, target)
    last = searchLast(nums, target)
    return [first, last]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return searchRange(nums, target)
