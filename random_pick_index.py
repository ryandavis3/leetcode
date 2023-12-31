from unittest import TestCase
from typing import Dict, List
from random import randint


class Solution:

    def __init__(self, nums: List[int]):
        self.nums_dict = self.build_dict(nums=nums)

    @staticmethod
    def build_dict(nums: List[int]) -> Dict[int, List[int]]:
        nums_dict: Dict[int, List[int]] = {}
        for i, num in enumerate(nums):
            if num not in nums_dict:
                nums_dict[num] = list()
            nums_dict[num].append(i)
        return nums_dict

    def pick(self, target: int) -> int:
        if target not in self.nums_dict:
            raise KeyError(f'Number {target} not in array!')
        L = len(self.nums_dict[target])
        if L == 1:
            index = 0
        else:
            index = randint(0, L-1)
        return self.self.nums_dict[target][index]


class TestSolution(TestCase):
    def test1(self) -> None:
        pass