from collections import Counter
from unittest import TestCase


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        pass


def remove_duplicate_letters(s: str) -> str:
    if s == '':
        return ''
    counter = Counter(s)
    pos = 0
    for i, char in enumerate(s):
        if char < s[pos]:
            pos = i
        counter[char] -= 1
        if counter[char] == 0:
            break
    letter = s[pos]
    s_remain = s[pos+1:].replace(letter, '')
    return letter + remove_duplicate_letters(s=s_remain)


class TestDuplicateLetters(TestCase):
    def test1(self) -> None:
        test_cases = {
            'bcabc': 'abc',
            'cbacdcbc': 'acdb',
        }
        for s, expected in test_cases.items():
            result = remove_duplicate_letters(s=s)
            self.assertEqual(result, expected)