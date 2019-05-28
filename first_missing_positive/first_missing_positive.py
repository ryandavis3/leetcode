from typing import List

def firstMissingPositive(nums: List[int]) -> int:
    """
    Find first missing positive number in unsorted 
    integer array.

    Runs in O(n) time.
    """
    if not nums:
        return 1
    max_val = max(nums)
    if max_val < 1:
        return 1
    slots = set()
    for num in nums:
        if num > 0:
            slots.add(num)
    for num in range(1, max_val+1):
        if num not in slots:
            return num
    return max_val + 1

def firstMissingPositiveCS(nums: List[int]) -> int:
    """
    Find first missing positive number in unsorted
    integer array.

    Runs in O(n) time. Try to make run in constant space.
    
    Make use of swapping indices.
    """
    if not nums:
        return 1
    max_val = max(nums)
    if max_val < 1:
        return 1
    L = len(nums)
    for i in range(len(nums)):
        num = nums[i]
        if num > 0 and num-1 < L:
            tmp = nums[num-1]
            nums[num-1] = num
            nums[i] = tmp
    return nums
    for i, num in enumerate(nums):
        if num != i+1:
            return i+1
    return max_val + 1

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        return firstMissingPositive(nums)
