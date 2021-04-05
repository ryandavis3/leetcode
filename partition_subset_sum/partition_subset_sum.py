from typing import List
from math import floor

def canPartition(nums: List[int]) -> bool:
    L = len(nums)
    index = floor(L / 2)
    nums = sorted(nums)
    # Left and right subsets
    left = sum(nums[:index])
    right = sum(nums[index:])
    # Return True if midpoint parition works
    if left == right:
        return True
    # Left subset larger
    while left < right:
        left += nums[index]
        right -= nums[index]
        index += 1
        if left == right:
            return True
        if left > right:
            return False
    # Right subset larger
    while left > right:
        left -= nums[index]
        right += nums[index]
        index -= 1
        if left == right:
            return True
        if left < right:
            return False


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        return canPartition(nums)


if __name__ == "__main__":
    nums = [2,2,1,1]
    result = canPartition(nums)
    print(result)
    nums = [1,5,11,5]
    result = canPartition(nums)
    print(result)
    nums = [1,2,3,5]
    result = canPartition(nums)
    print(result)
    nums = [1]*200 + [200]
    result = canPartition(nums)
    print(result)
    nums = [1]*200 + [300]
    result = canPartition(nums)
    print(result)
