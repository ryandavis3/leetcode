import unittest


def find_first_instance_word(haystack: str, needle: str) -> int:
    if needle == haystack:
        return 0
    l_needle = len(needle)
    l_haystack = len(haystack)
    for i in range(l_haystack - l_needle + 1):
        if haystack[i:i+l_needle] == needle:
            return i
    return - 1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return find_first_instance_word(haystack=haystack, needle=needle)


class TestFirstInstance(unittest.TestCase):
    def test1(self) -> None:
        haystack = 'abc'
        needle = 'c'
        first = find_first_instance_word(haystack=haystack, needle=needle)
        self.assertEqual(first, 2)

    def test2(self) -> None:
        haystack = 'hello'
        needle = 'll'
        first = find_first_instance_word(haystack=haystack, needle=needle)
        self.assertEqual(first, 2)