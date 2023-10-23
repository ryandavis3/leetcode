import unittest
from typing import Dict, List, Set


def rob(nums: List[int]):
    L = len(nums)
    max_sum = [0] * L
    max_sum_sets: Dict[Set] = {}
    for i, num in enumerate(nums):
        if i == 0:
            max_sum[i] = num
            max_sum_sets[i] = set([i])
            continue
        if i == 1:
            if nums[0] > nums[1]:
                max_sum[i] = nums[0]
                max_sum_sets[i] = set([0])
            else:
                max_sum[i] = nums[1]
                max_sum_sets[i] = set([1])
            continue
        if i == L - 1:
            if 0 in max_sum_sets[i-2]:
                max_possible_value = max(max_sum[i-2], num)
            else:
                max_possible_value = max_sum[i-2] + num 
        else:
            max_possible_value = max_sum[i-2] + num
        if max_possible_value > max_sum[i-1]:
            max_sum_set = max_sum_sets[i-2].copy()
            max_sum_set.add(i)
            max_sum[i] = max_possible_value
            max_sum_sets[i] = max_sum_set
        else:
            max_sum_set = max_sum_sets[i-1].copy()
            max_sum[i] = max_sum[i-1]
            max_sum_sets[i] = max_sum_set
    return max_sum[-1]


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_forward = rob(nums=nums)
        rob_backward = rob(nums=nums[::-1])
        return max(rob_forward, rob_backward)


class TestRob(unittest.TestCase):
    def test_rob1(self) -> None:
        nums = [2,3,2]
        max_rob = rob(nums=nums)
        self.assertEqual(max_rob, 3)

    def test_rob2(self) -> None:
        nums = [2,3,2,3]
        max_rob = rob(nums=nums)
        self.assertEqual(max_rob, 6)

    def test_rob3(self) -> None:
        nums = [5, 1, 4]
        max_rob = rob(nums=nums)
        self.assertEqual(max_rob, 5)

    def test_rob4(self) -> None:
        nums = [1, 2, 3]
        max_rob = rob(nums=nums)
        self.assertEqual(max_rob, 3)

    def test_rob5(self) -> None:
        nums = [1,1,3,6,7,10,7,1,8,5,9,1,4,4,3]
        max_rob = rob(nums=nums)
        self.assertEqual(max_rob, 41)   