from queue import Queue
from unittest import TestCase
from typing import Dict, List, Set


class Courses:
    def __init__(self, num_courses: int, prerequisites: List[List[int]]):
        self.num_courses = num_courses
        prerequisites_dict: Dict[int, Set] = {}
        for prerequisite in prerequisites:
            a, b = prerequisite
            if a not in prerequisites_dict:
                prerequisites_dict[a] = set()
            prerequisites_dict[a].add(b)
        self.prerequisites_dict = prerequisites_dict

    def get_prerequisites(self, course: int) -> Set:
        if course not in self.prerequisites_dict:
            return set()
        return self.prerequisites_dict[course]


class CourseGraph:
    def __init__(self, courses: Courses):
        self.courses = courses
        self.visited = set()



class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pass


class TestCourses(TestCase):
    def test1(self) -> None:
        courses = Courses(num_courses=2, prerequisites=[[1, 0]])
        prerequisites_dict_expected = {1: {0}}
        self.assertEqual(courses.prerequisites_dict, prerequisites_dict_expected)

    def test2(self) -> None:
        prerequisites = [[1, 0], [2, 0], [2, 1], [3, 2]]
        courses = Courses(num_courses=4, prerequisites=prerequisites)
        prerequisites_dict_expected = {1: {0}, 2: {0, 1}, 3: {2}}
        self.assertEqual(courses.prerequisites_dict, prerequisites_dict_expected)