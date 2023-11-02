from unittest import TestCase
from typing import List


class Subsequences:

    def __init__(self):
        self._subsequences: Dict[int, int] = {}

    @staticmethod
    def filter_extraneous(subseq: Dict[int, int], new_subseq: Dict[int, int]) -> Dict[int, int]:
        keys_to_delete = set()
        subseq_ends = sorted(list(subseq.keys()), reversed=True)
        for new_subseq_end, new_subseq_len in new_subseq.items():
            i = 0
            while subseq_ends[i] > new_subseq_end:
                if new_subseq_len > subseq[subseq_ends[i]]:
                    keys_to_delete.add(subseq_ends[i])
        for key in keys_to_delete:
            del subseq[key]
        return subseq


    def add_number(self, num: int) -> None:
        extend_subseq = False
        new_subseq: Dict[int, int] = {}
        for subseq_end, subseq_len in self._subsequences.items():
            if num > subseq_end:
                # Check if already in subseq and only add if larger.
                new_subseq[num] = subseq_len + 1
                extend_subseq = True
        self._subsequences = self._subsequences | new_subseq
        if not extend_subseq:
            self._subsequences[num] = 1



class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        pass


class TestSubsequences(TestCase):
    def test1(self) -> None:
        subsequences = Subsequences()
        subsequences.add_number(num=1)
        subsequences.add_number(num=7)
        subsequences.add_number(num=2)
        subsequences.add_number(num=3)


class TestILS(TestCase):
    def test1(self) -> None:
        nums = [10, 9, 2, 5, 3, 7, 101, 18]

    def test2(self) -> None:
        nums = [0, 1, 0, 3, 2, 3]

    def test3(self) -> None:
        nums = [7, 7, 7, 7, 7, 7, 7]

