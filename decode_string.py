from unittest import TestCase


def decode_string(s: str) -> str:
    if s.isalpha():
        return s


class Solution:
    def decodeString(self, s: str) -> str:
        pass


class TestDecodeString(TestCase):
    def test1(self) -> None:
        s = "3[a]2[bc]"
        expected = "aaabcbc"

    def test2(self) -> None:
        s = "3[a2[c]]"
        expected = "accaccacc"

    def test3(self) -> None:
        s = "2[abc]3[cd]ef"
        expected = "abcabccdcdcdef"

    def test4(self) -> None:
        s = 'abc'
        out = decode_string(s=s)
        expected = 'abc'
        self.assertEqual(out, expected)