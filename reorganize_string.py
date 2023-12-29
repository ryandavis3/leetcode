from unittest import TestCase


class Solution:
    def reorganizeString(self, s: str) -> str:
        pass


def reorganize_string(s: str) -> str:
    pass


class TestReorganizeString(TestCase):
    def test1(self) -> None:
        s = 'aab'
        result = reorganize_string(s=s)
        expected = 'aba'
        self.assertEqual(result, expected)
