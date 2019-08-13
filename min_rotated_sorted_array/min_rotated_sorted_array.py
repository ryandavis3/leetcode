import math
from typing import List

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

def findMin(nums: List[int]) -> int:
    """
    Suppose an array is sorted in ascending order at some pivot 
    unknown to us beforehand. Find the minimum element.
    """
    # Edge cases -> three or less elements
    L = len(nums)
    if L <= 3:
        return min(nums)
    # Compute midpoint
    mid = math.ceil(L/2)
    # Found pivot!
    if nums[mid-1] > nums[mid] and nums[mid+1] < nums[mid]:
        return nums[mid+1]
    # Array is sorted -> return first element
    if nums[0] < nums[mid] and nums[mid] < nums[-1]:
        return nums[0]
    # Search left subarray. There must be one pair of consecutive 
    # elements that is decreasing.
    if nums[0] > nums[mid]:
        return findMin(nums[0:mid+1])
    # Search right subarray
    else:
        return findMin(nums[mid:])

class Solution:
    def findMin(self, nums: List[int]) -> int:
        return findMin(nums)
