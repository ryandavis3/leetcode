from typing import List
from collections import Counter

# https://leetcode.com/problems/largest-number/solution/

## MY SOLUTION

def largestNumber(nums: List[int]) -> str:
    """
    Given a list of non-negative integers, arrange them 
    such that they form the largest number.
    """
    # Edge cases!
    if not nums:
        return ""
    if len(nums) == 1:
        return str(nums[0])
    # Convert to string
    nums = list(map(str, nums))
    # Count unique strings
    count = Counter(nums)
    # Max length
    max_len = max(list(map(len, nums)))
    # Pad with zeros to make all numbers same length
    nums = [n + '0'*(max_len - len(n)) for n in nums]
    # Sort numbers
    nums = sorted(nums, reverse=True)
    # Iterate over each number
    for i, num in enumerate(nums):
        # Find least padded representation available
        if "0" in num:
            nz = num.replace("0","")
            while True:
                # Found number!
                if nz in count:
                    nums[i] = nz
                    count[nz] -= 1
                    if count[nz] == 0:
                        del count[nz]
                    break
                # Add zero
                nz += "0"
    return "".join(nums)

## LEETCODE SOLUTION - SORTING VIA CUSTOM COMPARATOR

class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

def largestNumberLC(nums: List[int]) -> str:
    nums = map(str, nums)
    largest_num = "".join(sorted(nums, key=LargerNumKey))
    if largest_num[0] == "0":
        return "0"
    return largest_num

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return largestNumberLC(nums)
