# https://leetcode.com/problems/burst-balloons/

import unittest
from typing import List, Dict, Tuple, Set


class NumsMemoize:

    def __init__(self, nums: List[int]):
        self._combinations: Dict = {}
        self._group_size = 0
        self.nums = nums
        self.nums_indices = set(range(len(nums)))

    def add(self, key: Tuple, value: int) -> None:
        L = len(key)
        if L not in self._combinations:
            self._combinations[L]: Dict = {}
        self._combinations[L][key] = value

    def is_key_in_memo(self, key: Tuple) -> bool:
        L = len(key)
        if L not in self._combinations:
            return False
        if key in self._combinations[L]:
            return True
        return False

    def get_remaining_indices(self, key: Tuple) -> Set:
        pass

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
    G = nums_memoize.group_size
    if G == 0:
        for i, value in enumerate(nums):
            key = (i,)
            nums_memoize.add(key=key, value=value)
        nums_memoize.increment_group_size()
        return nums_memoize
    combinations = nums_memoize._combinations[G]
    if G == 1:
        for combination, value in combinations.items():
            combination_index = combination[0]
            for index in range(0, combination_index):
                new_value = value + nums[index] * nums[combination_index]
                key = (index, combination_index)
                nums_memoize.add(key=key, value=new_value)
        return nums_memoize
    for combination, value in combinations.items():
        combination_index = combination[0]




class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        pass


class TestNumsMemoize(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.nums = [3, 1, 5, 8]

    def test_1(self) -> None:
        nums_memoize = NumsMemoize(nums=self.nums)
        nums_memoize.add(key=(1,), value=1)
        nums_memoize.add(key=(2,), value=3)
        nums_memoize.add(key=(1, 2), value=4)
        value = nums_memoize.get(key=(1, 2))
        self.assertEqual(value, 4)
        with self.assertRaises(KeyError):
            _ = nums_memoize.get(key=(3,))

    def test_is_key_in_memo(self) -> None:
        nums_memoize = NumsMemoize(nums=self.nums)
        nums_memoize.add(key=(1,), value=1)
        nums_memoize.add(key=(1, 2), value=4)
        self.assertTrue(nums_memoize.is_key_in_memo(key=(1, 2)))
        self.assertFalse(nums_memoize.is_key_in_memo(key=(1, 3)))

    def test_remaining_indices(self) -> None:
        pass

class TestIncrementGroups(unittest.TestCase):

    def test_increment_groups1(self) -> None:
        nums = [3, 1, 5, 8]
        nums_memoize = NumsMemoize(nums=nums)
        nums_memoize_incremented = increment_groups(nums=nums, nums_memoize=nums_memoize)
        combinations_expected = {1: {(0,): 3, (1,): 1, (2,): 5, (3,): 8}}
        self.assertEqual(combinations_expected, nums_memoize_incremented._combinations)

    def test_increment_groups2(self) -> None:
        nums = [3, 1, 5, 8]
        nums_memoize = NumsMemoize(nums=nums)
        nums_memoize_incremented1 = increment_groups(nums=nums, nums_memoize=nums_memoize)
        nums_memoize_incremented2 = increment_groups(nums=nums, nums_memoize=nums_memoize_incremented1)
        combinations = nums_memoize_incremented2._combinations[2]
        combinations_expected = {(0, 1): 4, (0, 2): 20, (1, 2): 10, (0, 3): 32, (1, 3): 16, (2, 3): 48}
        self.assertEqual(combinations, combinations_expected)