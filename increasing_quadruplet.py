# https://leetcode.com/problems/count-increasing-quadruplets/description/

from unittest import TestCase
from typing import Dict, List, Set, Tuple
from dataclasses import dataclass


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


def count_triples(nums: List[int], couples: Dict[int, int]) -> Dict[int, Set[Tuple[int, int]]]:
    n = len(nums)
    triples: Dict[int, Set[Tuple[int, int]]] = {}
    unique_nums = sorted(list(set(nums)))
    max_num = unique_nums[-3]
    for i in range(2, n-1):
        for j in range(i):
            triples_ij = set()
            if nums[i] < nums[j] and j in couples and nums[i] <= max_num:
                for start_i in couples[j]:
                    if nums[start_i] < nums[i]:
                        triples_ij.add((start_i, j))
            if triples_ij:
                if i not in triples:
                    triples[i] = set()
                triples[i] = triples[i].union(triples_ij)
    return triples


def count_quadruples(nums: List[int], triples: Dict[int, Set[Tuple[int, int]]]) -> List[int]:
    n = len(nums)
    quadruples = [0] * n
    for i in range(n):
        for j in range(i):
            n_quadruples = 0
            if nums[i] > nums[j] and j in triples:
                for triple_prefix in triples[j]:
                    if nums[i] > nums[triple_prefix[1]]:
                        n_quadruples += 1
            quadruples[i] += n_quadruples
    return quadruples


def count_total_quadruples(nums: List[int]) -> int:
    couples = count_couples(nums=nums)
    triples = count_triples(nums=nums, couples=couples)
    quadruples = count_quadruples(nums=nums, triples=triples)
    return sum(quadruples)


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        return count_total_quadruples(nums=nums)


class TestCountQuadruplets(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.nums = [1, 3, 5, 2, 4, 7]

    def test_count_couples(self) -> None:
        couples = count_couples(nums=self.nums)
        couples_expected = {1: {0}, 2: {0, 1}, 3: {0}, 4: {0, 1, 3}}
        self.assertEqual(couples, couples_expected)

    def test_count_triples(self) -> None:
        couples = {1: {0}, 2: {0, 1}, 3: {0}, 4: {0, 1, 3}}
        triples = count_triples(nums=self.nums, couples=couples)
        triples_expected = {3: {(0, 1), (0, 2)}, 4: {(0, 2), (1, 2)}}
        self.assertEqual(triples, triples_expected)

    def test_count_quadruples(self) -> None:
        triples = {3: {(0, 1), (0, 2)}, 4: {(0, 2), (1, 2)}}
        quadruplets = count_quadruples(nums=self.nums, triples=triples)
        print(quadruplets)
        assert False