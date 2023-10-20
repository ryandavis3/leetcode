import unittest


def reverse_words(s: str) -> str:
    s_stripped = s.strip()
    s_splitted = s_stripped.split(" ")
    s_splitted = [s for s in s_splitted if len(s) > 0]
    s_split_reversed = s_splitted[::-1]
    s_reversed = " ".join(s_split_reversed)
    return s_reversed


class Solution:
    def reverseWords(self, s: str) -> str:
        pass


class ReverseTests(unittest.TestCase):

    def test_1(self) -> None:
        s = "the sky is blue"
        output = reverse_words(s=s)
        expected_output = "blue is sky the"
        self.assertEqual(output, expected_output)

    def test_2(self) -> None:
        s = "  hello world  "
        output = reverse_words(s=s)
        expected_output = "world hello"
        self.assertEqual(output, expected_output)

    def test_3(self) -> None:
        s = "a good   example"
        output = reverse_words(s=s)
        expected_output = "example good a"
        self.assertEqual(output, expected_output)