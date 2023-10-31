import unittest

from collections import Counter
from typing import List


def get_most_frequent_even(nums: List[int]) -> int:
    counter = Counter(nums)
    most_frequent_even = set()
    most_frequent_count = -1
    for num, count in counter.items():
        if num % 2 == 1:
            continue
        if count > most_frequent_count:
            most_frequent_count = count
            most_frequent_even = set([num])
        elif count == most_frequent_count:
            most_frequent_even.add(num)
    if len(most_frequent_even) == 0:
        return - 1
    return min(most_frequent_even)


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        pass


class TestMostFrequentEven(unittest.TestCase):
    def test1(self) -> None:
        nums = [0, 1, 2, 2, 4, 4, 1]
        result = get_most_frequent_even(nums=nums)
        self.assertEqual(result, 2)

    def test2(self) -> None:
        nums = [4, 4, 4, 9, 2, 4]
        result = get_most_frequent_even(nums=nums)
        self.assertEqual(result, 4)

    def test3(self) -> None:
        nums = [29, 47, 21, 41, 13, 37, 25, 7]
        result = get_most_frequent_even(nums=nums)
        self.assertEqual(result, -1)