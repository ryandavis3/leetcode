import unittest
from collections import Counter
from math import floor
from typing import List


def get_majority_element(nums: List[int]) -> int:
    counter = Counter(nums)
    n = len(nums)
    min_count = floor(n / 2)
    for element, count in counter.items():
        if count > min_count:
            return element


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return get_majority_element(nums=nums)


class TestMajorityElement(unittest.TestCase):

    def test1(self) -> None:
        nums = [3, 2, 3]
        majority_element = get_majority_element(nums=nums)
        self.assertEqual(majority_element, 3)

    def test2(self) -> None:
        nums = [2, 2, 1, 1, 1, 2, 2]
        majority_element = get_majority_element(nums=nums)
        self.assertEqual(majority_element, 2)


