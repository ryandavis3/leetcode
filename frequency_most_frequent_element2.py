from typing import List
from unittest import TestCase


def get_max_frequency(nums: List[int], k: int) -> int:
    nums = sorted(nums)
    L = len(nums)
    left = 0
    curr_sum = nums[left]
    max_freq = 1
    for right in range(1, L):
        curr_sum += nums[right]
        window_size = (right - left + 1)
        target_sum = window_size * nums[right]
        while target_sum - curr_sum > k:
            curr_sum -= nums[left]
            target_sum -= nums[right]
            left += 1
            window_size = (right - left + 1)
        if window_size > max_freq:
            max_freq = window_size
    return max_freq



class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        return get_max_frequency(nums=nums, k=k)


class TestMaxFreq(TestCase):
    def test1(self) -> None:
        nums = [1, 2, 4]
        max_freq = get_max_frequency(nums=nums, k=5)
        self.assertEqual(max_freq, 3)
        max_freq = get_max_frequency(nums=nums, k=2)
        self.assertEqual(max_freq, 2)

    def test2(self) -> None:
        nums = [1, 1, 2, 4]
        max_freq = get_max_frequency(nums=nums, k=5)
        self.assertEqual(max_freq, 3)

    def test3(self) -> None:
        nums = [1, 4, 8, 13]
        max_freq = get_max_frequency(nums=nums, k=5)
        self.assertEqual(max_freq, 2)

    def test4(self) -> None:
        nums = [3, 9, 6]
        max_freq = get_max_frequency(nums=nums, k=2)
        self.assertEqual(max_freq, 1)

    def test5(self) -> None:
        nums = [3, 3, 3]
        max_freq = get_max_frequency(nums=nums, k=1)
        self.assertEqual(max_freq, 3)