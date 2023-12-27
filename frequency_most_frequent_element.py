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


def get_cumulative_increments(increments: List[int]) -> List[int]:
    L = len(increments)
    cumulative_increments = [0] * L
    cumsum = 0
    for i, increment in enumerate(increments):
        cumsum += increment
        cumulative_increments[i] = cumsum
    return cumulative_increments


def get_max_frequency_from_matrix(increment_matrix: List[List[int]], k: int) -> List[int]:
    L = len(increment_matrix)
    for i in range(L):
        increments = increment_matrix[i][::-1]
        increments = [x for x in increments if x > 0]


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        pass


class TestIncrementMatrix(TestCase):
    def test1(self) -> None:
        nums = [1, 2, 4]
        increment_matrix = get_increment_matrix(nums=nums)
        increment_matrix_expected = [[0, 0, 0], [1, 0, 0], [3, 2, 0]]
        self.assertEqual(increment_matrix, increment_matrix_expected)

    def test2(self) -> None:
        increments = [2, 3]
        cumulative_increments = get_cumulative_increments(increments=increments)
        cumulative_increments_expected = [2, 5]
        self.assertEqual(cumulative_increments, cumulative_increments_expected)
