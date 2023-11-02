from unittest import TestCase
from dataclasses import dataclass
from typing import Dict, List


class Subsequences:

    def __init__(self):
        self._subsequences: Dict[int, int] = {}

    @staticmethod
    def filter_extraneous(subseq: Dict[int, int], new_subseq: Dict[int, int]) -> Dict[int, int]:
        keys_to_delete = set()
        subseq_ends = sorted(list(subseq.keys()), reverse=True)
        for new_subseq_end, new_subseq_len in new_subseq.items():
            i = 0
            while subseq_ends[i] > new_subseq_end:
                if new_subseq_len > subseq[subseq_ends[i]]:
                    keys_to_delete.add(subseq_ends[i])
                i += 1
        for key in keys_to_delete:
            del subseq[key]
        return subseq


    def add_number(self, num: int) -> None:
        extend_subseq = False
        new_subseq: Dict[int, int] = {}
        for subseq_end, subseq_len in self._subsequences.items():
            if num > subseq_end:
                new_subseq[num] = subseq_len + 1
                extend_subseq = True
        self._subsequences = self.filter_extraneous(subseq=self._subsequences, new_subseq=new_subseq)
        self._subsequences = self._subsequences | new_subseq
        if not extend_subseq:
            self._subsequences[num] = 1

    def get_max_subsequence_length(self) -> int:
        max_subseq_len = 0
        for _, subseq_len in self._subsequences.items():
            if subseq_len > max_subseq_len:
                max_subseq_len = subseq_len
        return max_subseq_len


@dataclass(frozen=True)
class GenerateSubsequencesResults:
    subsequences: Subsequences
    max_subsequence_len: int


def generate_subsequences(nums: List[int]) -> GenerateSubsequencesResults:
    subseqs = Subsequences()
    for num in nums:
        subseqs.add_number(num=num)
    max_subseq_len = subseqs.get_max_subsequence_length()
    results = GenerateSubsequencesResults(subsequences=subseqs, max_subsequence_len=max_subseq_len)
    return results


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

    def test_filter_extraneous(self) -> None:
        subseq = {1: 1, 2: 2, 7: 3}
        new_subseq = {3: 3, 4: 4}
        subseq_filtered = Subsequences.filter_extraneous(subseq=subseq, new_subseq=new_subseq)
        subseq_filtered_expected = {1: 1, 2: 2}
        self.assertEqual(subseq_filtered, subseq_filtered_expected)


class TestILS(TestCase):
    def test1(self) -> None:
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        results = generate_subsequences(nums=nums)
        self.assertEqual(results.max_subsequence_len, 4)

    def test2(self) -> None:
        nums = [0, 1, 0, 3, 2, 3]
        results = generate_subsequences(nums=nums)
        self.assertEqual(results.max_subsequence_len, 4)

    def test3(self) -> None:
        nums = [7, 7, 7, 7, 7, 7, 7]
        results = generate_subsequences(nums=nums)
        self.assertEqual(results.max_subsequence_len, 1)

