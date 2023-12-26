from unittest import TestCase


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        pass


def remove_duplicate_letters(s: str) -> str:
    pass


class TestDuplicateLetters(TestCase):
    def test1(self) -> None:
        test_cases = {
            'bcabc': 'abc',
            'cbacdcbc': 'acdb',
        }
        for s, expected in test_cases.items():
            result = remove_duplicate_letters(s=s)
            self.assertEqual(result, expected)