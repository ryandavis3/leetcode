from typing import List

# https://leetcode.com/problems/3sum-closest/

def twoSumClosest(nums: List[int], target: int) -> int:
    """
    Find two integers in a list such that the sum is 
    closest to a target.
    """
    L = len(nums)
    if L == 2:
        return sum(nums)
    # Set indices at start and end of list
    i = 0
    j = L-1
    # Set initial min diff at large number
    min_diff = 10**10
    close_sum = None
    # Iterate through list
    while i < j and j:
        # Difference between current sum and target
        diff = target - (nums[i] + nums[j])
        # Exact match! 
        if diff == 0:
            close_sum = nums[i] + nums[j]
            break
        # If sign of difference changes, either the current
        # sum or the previous sum is the closest.
        if abs(diff) < abs(min_diff):
            min_diff = diff
            close_sum = nums[i] + nums[j]
        # Need larger sum - remove first element
        if diff > 0:
            i += 1
        # Need smaller sum - remove last element
        else:
            j -= 1
    return close_sum

def threeSumClosest(nums: List[int], target: int) -> int:
    """
    Find three integers in a list such that sum sum is
    closest to a target. 
    """
    # Sort integers in ascending order
    nums = sorted(nums)
    # Large value for initial min difference 
    min_diff = 10**10
    for i, num in enumerate(nums):
        # Copy list and remove one integer
        nums_i = nums.copy()
        nums_i.remove(num)
        # Subtract integer from target to get the
        # two-integer sum target.
        target_small = target - num
        sum_i = twoSumClosest(nums_i, target_small)
        if sum_i == target_small:
            return target
        # Update min difference if we find a closer solution
        diff = target_small - sum_i
        if abs(diff) < abs(min_diff):
            close_sum = sum_i + num
            min_diff = diff
    return close_sum

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        return threeSumClosest(nums, target)
