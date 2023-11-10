from unittest import TestCase
from typing import List


def get_longest_increasing_subsequence(nums: List[int]) -> List[int]:
    L = len(nums)
    dp = [1] * L
    for i in range(1, L):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = get_longest_increasing_subsequence(nums=nums)
        return dp[-1]


class TestLIS(TestCase):
    def test1(self) -> None:
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        dp = get_longest_increasing_subsequence(nums=nums)
        self.assertEqual(dp[-1], 4)

    def test2(self) -> None:
        nums = [0, 1, 0, 3, 2, 3]
        dp = get_longest_increasing_subsequence(nums=nums)
        self.assertEqual(dp[-1], 4)

    def test3(self) -> None:
        nums = [7, 7, 7, 7, 7, 7, 7]
        dp = get_longest_increasing_subsequence(nums=nums)
        self.assertEqual(dp[-1], 1)