import unittest
from typing import List, Set


DOUBLE_DOT = '..'


def _resolve_double_dot(strings: List[str]) -> List[str]: 
    # resolve "internal" double dots
    i = 0
    while i < len(strings):
        if i + 1 < len(strings) and strings[i + 1] == DOUBLE_DOT:
            strings = strings[:i] + strings[i+2:]
            i = max(0, i - 2)
        else:
            i += 1
    # remove leading double dot
    if len(strings) > 0:
        while strings[0] == DOUBLE_DOT:
            strings = strings[1:]
    return strings


def simplify_path(path: str) -> str:
    strings = path.split('/')
    strings = [s for s in strings if s != '' and s != '.']
    if strings[0] == '..':
        strings = strings[1:]
    strings = _resolve_double_dot(strings=strings)
    path_new = "/".join(strings)
    path_new = "/" + path_new
    return path_new


class Solution:
    def simplifyPath(self, path: str) -> str:
        return simplify_path(path=path)


class TestSimplify(unittest.TestCase):

    def test_1(self) -> None:
        path = "/home/"
        expected_output = "/home"
        output = simplify_path(path=path)
        self.assertEqual(output, expected_output)

    def test_2(self) -> None:
        path = "/../"
        expected_output = "/"
        output = simplify_path(path=path)
        self.assertEqual(output, expected_output)

    def test_3(self) -> None:
        path = "/home//foo/"
        expected_output = "/home/foo"
        output = simplify_path(path=path)
        self.assertEqual(output, expected_output)

    def test_4(self) -> None:
        path = "/a/./b/../../c/"
        expected_output = "/c"
        output = simplify_path(path=path)
        self.assertEqual(output, expected_output)

    def test_5(self) -> None:
        path = "/a/../../b/../c//.//"
        expected_output = "/c"
        output = simplify_path(path=path)
        self.assertEqual(output, expected_output)