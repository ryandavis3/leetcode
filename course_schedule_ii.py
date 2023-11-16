from queue import Queue
from unittest import TestCase
from typing import Dict, List, Set


class Adjacency:
    def __init__(self, prerequisites: List[List[int]]):
        # Keys are prerequisites. Values are later courses
        # for which the key is a prerequisite.
        prereq_dict: Dict[int, Set] = {}
        follow_dict: Dict[int, Set] = {}
        for prerequisite in prerequisites:
            # b is the prerequisite for a
            a, b = prerequisite
            if a not in prereq_dict:
                prereq_dict[a] = set()
            prereq_dict[a].add(b)
            if b not in follow_dict:
                follow_dict[b] = set()
            follow_dict[b].add(a)
        self.prereq_dict = prereq_dict
        self.follow_dict = follow_dict

    def apply_prereq(self, course: int, prereq: int) -> bool:
        if course not in self.prereq_dict:
            err_msg = f'Course {course} not in prereq dictionary!'
            raise ValueError(err_msg)
        if prereq not in self.prereq_dict[course]:
            err_msg = f'Prereq {prereq} not listed for course {course}!'
            raise ValueError(err_msg)
        self.prereq_dict[course].remove(prereq)
        if not self.prereq_dict[course]:
            del self.prereq_dict[course]
            return True
        return False


def find_order():
    pass


class TestAdjacency(TestCase):
    def test1(self) -> None:
        adjacency = Adjacency(prerequisites=[[1, 0]])
        follow_dict_expected = {0: {1}}
        self.assertEqual(adjacency.follow_dict, follow_dict_expected)

    def test2(self) -> None:
        prerequisites = [[1, 0], [2, 0], [2, 1], [3, 2]]
        adjacency = Adjacency(prerequisites=prerequisites)
        follow_dict_expected = {0: {1, 2}, 1: {2}, 2: {3}}
        self.assertEqual(adjacency.follow_dict, follow_dict_expected)
        prereq_dict_expected = {2: {0, 1}, 1: {0}, 3: {2}}
        self.assertEqual(adjacency.prereq_dict, prereq_dict_expected)
        available = adjacency.apply_prereq(course=1, prereq=0)
        self.assertTrue(available)





