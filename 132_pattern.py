from unittest import TestCase
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        return find_pattern(nums=nums)


def find_pattern(nums: List[int]) -> bool:
    i = nums[0]
    j = None
    for num in nums[1:]:
        if num < i:
            i = num
        if j is not None:
            if num < j and num > i:
                return True
            if num > j:
                j = num
        if j is None and num > i:
            j = num
    return False


class TestPattern(TestCase):
    def test1(self) -> None:
        nums = [1, 2, 3, 4]
        pattern = find_pattern(nums=nums)
        self.assertFalse(pattern)

    def test2(self) -> None:
        nums = [3, 1, 4, 2]
        pattern = find_pattern(nums=nums)
        self.assertTrue(pattern)

    def test3(self) -> None:
        nums = [-1, 3, 2, 0]
        pattern = find_pattern(nums=nums)
        self.assertTrue(pattern)

    def test4(self) -> None:
        nums = [5, 2, 4, 3]
        pattern = find_pattern(nums=nums)
        self.assertTrue(pattern)

    def test5(self) -> None:
        nums = [1, 2, 3, 2, 1]
        pattern = find_pattern(nums=nums)
        self.assertTrue(pattern)

    def test6(self) -> None:
        nums = [1, 0, 1, -4, -3]
        pattern = find_pattern(nums=nums)
        self.assertFalse(pattern)