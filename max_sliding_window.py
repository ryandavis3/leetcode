from unittest import TestCase
from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pass


def get_max_sliding_window(nums: List[int], k: int) -> List[int]:
    pass


class TestMaxSlidingWindow(TestCase):
    def test1(self) -> None:
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        sliding_window = get_max_sliding_window(nums=nums, k=3)
        expected = [3, 3, 5, 5, 6, 7]
        self.assertEqual(sliding_window, expected)