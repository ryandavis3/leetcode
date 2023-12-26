from unittest import TestCase


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        pass


class StringChars:
    def __init__(self, s: str):
        chars: Dict[s, Set] = {}
        for i, char in enumerate(s):
            if char not in chars:
                chars[char] = set()
            chars[char].add(i)
        self.chars = chars
        self.unique_chars = sorted(list(set(s)), reverse=True)
        self.index = -1

    def pop_letter(self) -> str:
        letter = self.unique_chars.pop()
        letter_index = self.chars[letter]
        valid_letter_index = [index for index in letter_index if index > self.index]


def remove_duplicate_letters(s: str) -> str:
    pass


class TestStringChars(TestCase):
    def test1(self) -> None:
        string_chars = StringChars(s='bcabc')
        chars_expected = {'a': set([2]), 'b': set([0, 3]), 'c': set([1, 4])}
        unique_chars_expected = ['c', 'b', 'a']
        self.assertEqual(string_chars.chars, chars_expected)
        self.assertEqual(string_chars.unique_chars, unique_chars_expected)


class TestDuplicateLetters(TestCase):
    def test1(self) -> None:
        return None
        test_cases = {
            'bcabc': 'abc',
            'cbacdcbc': 'acdb',
        }
        for s, expected in test_cases.items():
            result = remove_duplicate_letters(s=s)
            self.assertEqual(result, expected)