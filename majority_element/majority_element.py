# https://leetcode.com/problems/majority-element-ii/

from typing import List
from collections import Counter
import math

def majorityElement(nums: List[int]) -> List[int]:
    """
    Given an integer array of size n, find all elements
    that appear more than floor(n/3) times.

    Run in linear time and O(1) space (if we treat the 
    set of possible elements as a constant).
    """
    n = len(nums)
    ct = Counter(nums)
    size = math.floor(n/3)
    L = list()
    for element in ct:
        if ct[element] > size:
            L.append(element)
    return L

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return majorityElement(nums)
