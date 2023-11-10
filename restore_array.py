from unittest import TestCase
from typing import Dict, List, Set


def get_pairs_dict(adjacent_pairs: List[List[int]]) -> Dict[int, Set]:
    pairs_dict: Dict[int, Set] = {}
    for adjacent_pair in adjacent_pairs:
        n1, n2 = adjacent_pair
        if n1 not in pairs_dict:
            pairs_dict[n1] = set()
        if n2 not in pairs_dict:
            pairs_dict[n2] = set()
        pairs_dict[n1].add(n2)
        pairs_dict[n2].add(n1)
    return pairs_dict


def get_start_candidates(pairs_dict: Dict[int, Set]) -> int:
    candidates = set()
    for num, adjacent in pairs_dict.items():
        if len(adjacent) < 2:
            candidates.add(num)
    return candidates


def restore_array(adjacent_pairs: List[List[int]]) -> List[int]:
    pass


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        pass


class TestRestoreArray(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.adjacent_pairs = [[2, 1], [3, 4], [3, 2]]
        cls.pairs_dict = {2: {1, 3}, 1: {2}, 3: {2, 4}, 4: {3}}

    def test_get_pairs_dict1(self) -> None:
        pairs_dict = get_pairs_dict(adjacent_pairs=self.adjacent_pairs)
        self.assertEqual(pairs_dict, self.pairs_dict)
