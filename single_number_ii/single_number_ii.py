from typing import List

# https://leetcode.com/problems/single-number-ii/

def singleNumber(nums: List[int]) -> int:
    """
    Given an aray of integers, every element appears three times
    except for one, which appears exactly once -> return that element. 
    """
    return int((3 * sum(set(nums)) - sum(nums)) / 2)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return singleNumber(nums)
