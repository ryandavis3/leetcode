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
        if key not in self._combinations:
            raise KeyError(f'Key {key} not found!')
        return self._combinations[key]

    def increment_group_size(self) -> None:
        self._group_size += 1

    @property
    def group_size(self) -> int:
        return self._group_size


def increment_groups(nums: List[int], nums_memoize: NumsMemoize) -> None:



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