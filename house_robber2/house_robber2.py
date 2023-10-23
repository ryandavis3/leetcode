import unittest
from typing import Dict, List, Set


def rob(nums: List[int]):
    L = len(nums)
    max_sum = [0] * L
    max_sum_sets: Dict[Set] = {}
    for i, num in enumerate(nums):
        if i == 0:
            max_sum[i] = num
            max_sum_sets[i] = set(i)
            continue
        if i == 1:
            if nums[0] > nums[1]:
                max_sum[i] = nums[0]
                max_sum_sets[i] = set(0)
            else:
                max_sum[i] = nums[1]
                max_sum_sets[i] = set(1)
            continue
        if max_sum[i-2] + num > max_sum[i-1]:
            max_sum_set = max_sum_sets[i-2].copy()
            max_sum_set.add(i)
            max_sum[i] = max_sum[i-2] + num
            max_sum_sets[i] = max_sum_set
        else:
            max_sum_set = max_sum_sets[i-1].copy()
            max_sum_set.add(i-1)
            max_sum[i] = max_sum[i-1] + num
            max_sum_sets[i] = max_sum_set
    return max_sum[-1]


class Solution:
    def rob(self, nums: List[int]) -> int:
        pass


class TestRob(unittest.TestCase):
    def test_rob1(self) -> None:
        nums = [2,3,2]
        max_rob = rob(nums=nums)
        self.assertEqual(max_rob, 3)

    def test_rob2(self) -> None:
        nums = [2,3,2,3]
        max_rob = rob(nums=nums)
        self.assertEqual(max_rob, 6)