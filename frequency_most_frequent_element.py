from unittest import TestCase
from typing import Dict, List


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


def get_increment_dict(nums: List[int]) -> Dict[int, List[int]]:
    nums = sorted(nums)
    increment_dict: Dict[int, List[int]] = dict()
    for i, target_num in enumerate(nums):
        increment_array = list()
        for j, start_num in enumerate(nums):
            if target_num >= start_num and i != j:
                diff = target_num - start_num
                increment_array.append(diff)
        increment_dict[target_num] = sorted(increment_array)
    return increment_dict


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
    nums = sorted(nums)
    increment_matrix = get_increment_matrix(nums=nums)
    max_freq = get_max_frequency_from_matrix(increment_matrix=increment_matrix, k=k)
    return max_freq


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        return get_max_freq(nums=nums, k=k)


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
        max_freq = get_max_freq(nums=nums, k=11)
        self.assertEqual(max_freq, 3)

    def test7(self) -> None:
        nums = [3, 9, 6]
        max_freq = get_max_freq(nums=nums, k=2)
        self.assertEqual(max_freq, 1)
        max_freq = get_max_freq(nums=nums, k=3)
        self.assertEqual(max_freq, 2)
        max_freq = get_max_freq(nums=nums, k=9)
        self.assertEqual(max_freq, 3)

    def test8(self) -> None:
        nums = [9922, 9980, 9990, 9922, 9932, 9989, 9929, 9938, 9941, 9966, 9985, 9906, 9964, 9903, 9995, 9963, 10000, 9950,
         9939, 9985, 9944, 9960, 9989, 9977, 9901, 9923, 9997, 9971, 9909, 9985, 9979, 9906, 9955, 9988, 9996, 9995,
         9901, 9996, 9924, 9967, 9991, 9981, 9914, 9933, 9946, 9928, 9975, 9990, 9968, 9985, 9963, 9927, 9946, 9919,
         9931, 9955, 9979, 9943, 9905, 9918, 9962, 9970, 9939, 9901, 9940, 9933, 9917, 9988, 9935, 9941, 9947, 9971,
         9901, 9926, 9908, 9969, 9978, 9984, 9952, 9945, 9958, 9958, 9930, 9923, 9950, 9993, 9938, 9976, 9942, 9946,
         9990, 9951, 9971, 9980, 9966, 9944, 9976, 9954, 9970, 9984, 9939, 9961, 9996, 9993, 9935, 9949, 9975, 9952,
         9998, 9956, 9957, 9949, 9902, 9946, 9979, 9904, 9925, 9948, 9952, 9961, 9948, 9982, 9922, 9958, 9956]
        max_freq = get_max_freq(nums=nums, k=1911)
        #self.assertEqual(max_freq, 75)

    def test9(self) -> None:
        nums = [3, 3, 3]
        max_freq = get_max_freq(nums=nums, k=1)
        #self.assertEqual(max_freq, 3)

    def test10(self) -> None:
        nums = [1, 2, 4]
        increment_dict = get_increment_dict(nums=nums)
        increment_dict_expected = {1: [], 2: [1], 4: [2, 3]}
        self.assertEqual(increment_dict, increment_dict_expected)

    def test11(self) -> None:
        nums = [1, 1, 2, 4]
        increment_dict = get_increment_dict(nums=nums)
        increment_dict_expected = {1: [0], 2: [1, 1], 4: [2, 3, 3]}
        self.assertEqual(increment_dict, increment_dict_expected)