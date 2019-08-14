from typing import List

# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

def removeDuplicates(nums: List[int]) -> int:
    """
    Given a sorted array nums, remove duplicates in place
    such that duplicates appear at most twice.
    """
    if len(nums) > 2:
        i = 2
        while i < len(nums):
            if nums[i-2] == nums[i-1] and nums[i-1] == nums[i]:
                nums.pop(i)
            else:
                i += 1
    return len(nums)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return removeDuplicates(nums)
