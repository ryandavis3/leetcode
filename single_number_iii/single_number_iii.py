from typing import List
from collections import Counter

# https://leetcode.com/problems/single-number-iii/

def singleNumber(nums: List[int]) -> List[int]:
    """
    Given an array of numbers in which exactly two elements
    appear only once and all other elements appear exactly 
    twice, return the two elements that appear once.
    """
    num_count = Counter(nums)
    appear_once = []
    for num, count in num_count.items():
        if count == 1:
            appear_once += [num]
    return appear_once

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        return singleNumber(nums)
