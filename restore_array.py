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
    if len(candidates) != 2:
        err_msg = f'There are {len(candidates)} start messages but there should be only two!'
        raise ValueError(err_msg)
    return candidates


def restore_array(adjacent_pairs: List[List[int]]) -> List[int]:
    pairs_dict = get_pairs_dict(adjacent_pairs=adjacent_pairs)
    start_candidates = get_start_candidates(pairs_dict=pairs_dict)
    start = min(start_candidates)
    end = max(start_candidates)
    array = [start]
    seen = set([start])
    num = start
    while num != end:
        adjacent = pairs_dict[num]
        adjacent_available = adjacent - seen
        if len(adjacent_available) > 1:
            err_msg = f'Found {len(adjacent_available)} available adjacent values to {num}!'
            raise ValueError(err_msg)
        num = adjacent_available.pop()
        seen.add(num)
        array += [num]
    return array


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        return restore_array(adjacent_pairs=adjacentPairs)


class TestRestoreArray(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.adjacent_pairs = [[2, 1], [3, 4], [3, 2]]
        cls.pairs_dict = {2: {1, 3}, 1: {2}, 3: {2, 4}, 4: {3}}

    def test_get_pairs_dict1(self) -> None:
        pairs_dict = get_pairs_dict(adjacent_pairs=self.adjacent_pairs)
        self.assertEqual(pairs_dict, self.pairs_dict)

    def test_restore_array(self) -> None:
        array = restore_array(adjacent_pairs=self.adjacent_pairs)
        array_expected = [1, 2, 3, 4]
        self.assertEqual(array, array_expected)

    def test_restore_array2(self) -> None:
        array = restore_array(adjacent_pairs=[[4, -2], [1, 4], [-3, 1]])
        array_expected = [-3, 1, 4, -2]
        self.assertEqual(array, array_expected)