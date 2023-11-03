from unittest import TestCase
from typing import Dict, List


def count_couples(nums: List[int]) -> Dict[int, int]:
    n = len(nums)
    couples: Dict[int, int] = {}
    unique_nums = sorted(list(set(nums)))
    max_num = unique_nums[-2]
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j] and nums[i] <= max_num:
                if i not in couples:
                    couples[i] = set()
                couples[i].add(j)
    return couples


def count_triples(nums: List[int], couples: Dict[int, int]):
    pass


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        pass


class TestCountQuadruplets(TestCase):

    def test_count_couples(self) -> None:
        nums = [1, 3, 5, 2, 4, 7]
        couples = count_couples(nums=nums)
        couples_expected = {1: {0}, 2: {0, 1}, 3: {0}, 4: {0, 1, 3}}
        self.assertEqual(couples, couples_expected)