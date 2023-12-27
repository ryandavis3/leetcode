from unittest import TestCase
from typing import List


def get_increment_matrix(nums: List[int]) -> List[List[int]]:
    L = len(nums)
    increment_matrix: List[List[int]] = []
    for target_num in nums:
        increment_array = [0] * L
        for j, start_num in enumerate(nums):
            if target_num > start_num:
                increment_array[j] = target_num - start_num
        increment_matrix += [increment_array]
    return increment_matrix


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        pass


class TestIncrementMatrix(TestCase):
    def test1(self) -> None:
        nums = [1, 2, 4]
        increment_matrix = get_increment_matrix(nums=nums)
        increment_matrix_expected = [[0, 0, 0], [1, 0, 0], [3, 2, 0]]
        self.assertEqual(increment_matrix, increment_matrix_expected)