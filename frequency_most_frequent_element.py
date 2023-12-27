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


def get_max_freq_cumulative_increments(cumulative_increments: List[int], k: int) -> int:
    if not cumulative_increments:
        return 1
    if cumulative_increments[-1] <= k:
        return len(cumulative_increments) + 1
    for i, cumulative_increment in enumerate(cumulative_increments):
        if cumulative_increment > k:
            return i + 1


def get_max_frequency_from_matrix(increment_matrix: List[List[int]], k: int) -> List[int]:
    L = len(increment_matrix)
    max_freq = 0
    for i in range(L):
        increments = increment_matrix[i][::-1]
        increments = [x for x in increments if x > 0]
        cumulative_increments = get_cumulative_increments(increments=increments)
        max_freq_i = get_max_freq_cumulative_increments(cumulative_increments=cumulative_increments, k=k)
        if max_freq_i > max_freq:
            max_freq = max_freq_i
    return max_freq


def get_max_freq(nums: List[int], k: int) -> int:
    increment_matrix = get_increment_matrix(nums=nums)
    max_freq = get_max_frequency_from_matrix(increment_matrix=increment_matrix, k=k)
    return max_freq


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

    def test3(self) -> None:
        cumulative_increments = [2, 5, 10]
        max_freq = get_max_freq_cumulative_increments(cumulative_increments=cumulative_increments, k=5)
        self.assertEqual(max_freq, 3)
        max_freq = get_max_freq_cumulative_increments(cumulative_increments=cumulative_increments, k=20)
        self.assertEqual(max_freq, 4)

    def test4(self) -> None:
        increment_matrix = [[0, 0, 0], [1, 0, 0], [3, 2, 0]]
        max_freq = get_max_frequency_from_matrix(increment_matrix=increment_matrix, k=5)
        self.assertEqual(max_freq, 3)

    def test5(self) -> None:
        increment_matrix = [[0, 0, 0], [1, 0, 0], [3, 2, 0]]
        max_freq = get_max_frequency_from_matrix(increment_matrix=increment_matrix, k=5)
        self.assertEqual(max_freq, 3)

    def test6(self) -> None:
        nums = [1, 4, 8, 13]
        max_freq = get_max_freq(nums=nums, k=5)
        self.assertEqual(max_freq, 2)

