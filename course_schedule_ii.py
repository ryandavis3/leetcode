from queue import Queue
from unittest import TestCase
from typing import Dict, List, Set


class Courses:
    def __init__(self, prerequisites: List[List[int]]):
        # Keys are prerequisites. Values are later courses
        # for which the key is a prerequisite.
        prerequisites_dict: Dict[int, Set] = {}
        for prerequisite in prerequisites:
            # b is the prerequisite for a
            a, b = prerequisite
            if b not in prerequisites_dict:
                prerequisites_dict[b] = set()
            prerequisites_dict[b].add(a)
        self.prerequisites_dict = prerequisites_dict

    def get_subsequent_courses(self, prerequisite: int) -> Set:
        if prerequisite not in self.prerequisites_dict:
            return set()
        return self.prerequisites_dict[prerequisite]


class CourseGraph:
    def __init__(self, courses: Courses):
        self.courses = courses
        self.visited = set()


def dfs(courses: Courses, root: int, visited: Set, in_stack: Set) -> bool:
    if root in in_stack:
        return True
    if root in visited:
        return False
    visited.add(root)
    in_stack.add(root)
    prereqs = courses.get_prerequisites(course=root)
    for prereq in prereqs:
        found_cycle = dfs(courses=courses, root=prereq, visited=visited, in_stack=in_stack)
        if found_cycle:
            return True
    in_stack.remove(root)
    return False


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    courses = Courses(num_courses=num_courses, prerequisites=prerequisites)
    visited = set()
    for root in range(num_courses):
        if root in visited:
            continue
        found_cycle = dfs(courses=courses, root=root, visited=visited, in_stack=set())
        if found_cycle:
            return False
    return True


class TestCourses(TestCase):
    def test1(self) -> None:
        courses = Courses(prerequisites=[[1, 0]])
        prerequisites_dict_expected = {0: {1}}
        self.assertEqual(courses.prerequisites_dict, prerequisites_dict_expected)

    def test2(self) -> None:
        prerequisites = [[1, 0], [2, 0], [2, 1], [3, 2]]
        courses = Courses(prerequisites=prerequisites)
        prerequisites_dict_expected = {0: {1, 2}, 1: {2}, 2: {3}}
        self.assertEqual(courses.prerequisites_dict, prerequisites_dict_expected)