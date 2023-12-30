from unittest import TestCase
from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pass


def get_max_sliding_window(nums: List[int], k: int) -> List[int]:
    # First window
    dq = deque()
    n = len(nums)
    res = [0] * (n - k + 1)
    for i in range(k):
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
        dq.append(i)
    res[0] = nums[dq[0]]
    # Sliding window
    for i in range(k, n):
        print(dq)
        if dq[0] == i - k:
            dq.popleft()
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
        dq.append(i)
        res[i-k+1] = nums[dq[0]]
    return res


class TestMaxSlidingWindow(TestCase):
    def test1(self) -> None:
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        sliding_window = get_max_sliding_window(nums=nums, k=3)
        expected = [3, 3, 5, 5, 6, 7]
        self.assertEqual(sliding_window, expected)