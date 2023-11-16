from queue import Queue
from unittest import TestCase
from typing import Dict, List, Set


class Adjacency:
    def __init__(self, prerequisites: List[List[int]]):
        # Keys are prerequisites. Values are later courses
        # for which the key is a prerequisite.
        adjacency_dict: Dict[int, Set] = {}
        prereq_dict: Dict[int, Set] = {}
        for prerequisite in prerequisites:
            # b is the prerequisite for a
            a, b = prerequisite
            if a not in adjacency_dict:
                adjacency_dict[a] = set()
            adjacency_dict[a].add(b)
            if b not in prereq_dict:
                prereq_dict[b] = set()
            prereq_dict[b].add(a)
        self.adjacency_dict = adjacency_dict
        self.prereq_dict = prereq_dict

    def apply_prereq(self, course: int, prereq: int) -> None:
        if course not in self.adjacency_dict:
            err_msg = f'Course {course} not in adjacency dictionary!'
            raise ValueError(err_msg)
        if prereq not in self.adjacency_dict[course]:
            err_msg = f'Prereq {prereq} not listed for course {course}!'
            raise ValueError(err_msg)
        self.adjacency_dict[course].remove(prereq)



class TestAdjacency(TestCase):
    def test1(self) -> None:
        courses = Adjacency(prerequisites=[[1, 0]])
        prerequisites_dict_expected = {0: {1}}
        self.assertEqual(courses.prereq_dict, prerequisites_dict_expected)

    def test2(self) -> None:
        prerequisites = [[1, 0], [2, 0], [2, 1], [3, 2]]
        courses = Adjacency(prerequisites=prerequisites)
        prerequisites_dict_expected = {0: {1, 2}, 1: {2}, 2: {3}}
        self.assertEqual(courses.prereq_dict, prerequisites_dict_expected)
