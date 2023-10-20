import unittest

def simplify_path(path: str) -> str:
    pass


class Solution:
    def simplifyPath(self, path: str) -> str:
        pass


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
