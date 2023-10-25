import unittest
from typing import List


def longest_increasing_subsequence(nums: List[int]) -> int:
    longest_increasing = 1
    current_length_increasing = 1
    prev = 0
    for num in nums:
        if num > prev:
            current_length_increasing += 1
        else:
            current_length_increasing = 1
        prev = num
        if current_length_increasing > longest_increasing:
            longest_increasing = current_length_increasing
    return longest_increasing


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        pass


class TestLIS(unittest.TestCase):
    def test_longest_increasing_subsequence(self) -> None:
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        lis = longest_increasing_subsequence(nums=nums)
        self.assertEqual(lis, 4)