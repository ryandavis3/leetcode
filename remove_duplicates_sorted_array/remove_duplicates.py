from typing import List

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicates(nums: List[int]) -> int:
    """
    Remove duplicates from sorted array in place.
    """
    i = 1
    # Iterate
    while i < len(nums):
        # Same as previous value - pop!
        if nums[i] == nums[i-1]:
            nums.pop(i)
        else:
            i += 1
    return len(nums)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return removeDuplicates(nums)
