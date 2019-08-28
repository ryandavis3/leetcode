from typing import List

# https://leetcode.com/problems/remove-element/

def removeElement(nums: List[int], val: int) -> int:
    """
    Given an array nums and value val, remove all instances
    of the value in-place and return the new length.
    """
    # No array passed!
    if not nums:
        return 0
    # Count number of instances of value
    count = sum([1 if num == val else 0 for num in nums])
    # Remove values from array in place
    for _ in range(count):
        nums.remove(val)
    # Return length of new array
    return len(nums)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        return removeElement(nums, val)
