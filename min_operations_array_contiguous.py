from typing import List
from unittest import TestCase


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        pass


def get_min_operations(nums: List[int]) -> int:
    nums = sorted(nums)
    max_subseq_len = 1
    curr_subseq_len = 1
    L = len(nums)
    for i in range(1, L):
        if nums[i] == nums[i-1] + 1:
            curr_subseq_len += 1
            if curr_subseq_len > max_subseq_len:
                max_subseq_len = curr_subseq_len
        else:
            curr_subseq_len = 1
    return L - curr_subseq_len


class TestMinOps(TestCase):
    def test1(self) -> None:
        nums = [4, 2, 5, 3]
        min_ops = get_min_operations(nums=nums)
        self.assertEqual(min_ops, 0)

    def test2(self) -> None:
        nums = [1, 2, 3, 5, 6]
        min_ops = get_min_operations(nums=nums)
        self.assertEqual(min_ops, 1)

    def test3(self) -> None:
        nums = [1, 10, 100, 1000]
        min_ops = get_min_operations(nums=nums)
        self.assertEqual(min_ops, 3)