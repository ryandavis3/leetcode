# https://leetcode.com/problems/burst-balloons/

import unittest
from typing import List, Dict, Tuple


class NumsMemoize:

    def __init__(self):
        self._combinations: Dict = {}
        self._group_size = 0

    def add(self, key: Tuple, value: int) -> None:
        L = len(key)
        if L not in self._combinations:
            self._combinations[L]: Dict = {}
        self._combinations[L][key] = value

    def get(self, key: Tuple) -> int:
        err_msg = f'Key {key} not found!'
        L = len(key)
        if L not in self._combinations:
            raise KeyError(err_msg)
        if key not in self._combinations[L]:
            raise KeyError(err_msg)
        return self._combinations[L][key]

    def increment_group_size(self) -> None:
        self._group_size += 1

    @property
    def group_size(self) -> int:
        return self._group_size


def increment_groups(nums: List[int], nums_memoize: NumsMemoize) -> NumsMemoize:
    if nums_memoize.group_size == 0:
        for i, value in enumerate(nums):
            key = (i,)
            nums_memoize.add(key=key, value=value)
        nums_memoize.increment_group_size()
    return nums_memoize


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        pass


class TestNumsMemoize(unittest.TestCase):
    def test_1(self) -> None:
        nums_memoize = NumsMemoize()
        nums_memoize.add(key=(1,), value=1)
        nums_memoize.add(key=(2,), value=3)
        nums_memoize.add(key=(1, 2), value=4)
        value = nums_memoize.get(key=(1, 2))
        self.assertEqual(value, 4)
        with self.assertRaises(KeyError):
            _ = nums_memoize.get(key=(3,))


class TestIncrementGroups(unittest.TestCase):

    def test_increment_groups1(self) -> None:
        nums = [3, 1, 5, 8]
        nums_memoize = NumsMemoize()
        nums_memoize_incremented = increment_groups(nums=nums, nums_memoize=nums_memoize)
        print(nums_memoize_incremented)
        assert False