from unittest import TestCase


OPEN = '['
CLOSED = ']'


def decode_string(s: str) -> str:
    print(s)
    L = len(s)
    # String is all alphabetic characters -> return it
    if s.isalpha():
        return s
    # Check for leading digits -> if present, use as multiplier
    if s[0].isdigit():
        i = 1
        while s[i].isdigit():
            i += 1
        multiplier = int(s[0:i])
    else:
        i = 0
        multiplier = 1
    # Get open and closed brackets
    if s[i] == OPEN:
        j = i + 1
        while s[j] != CLOSED:
            j += 1
        decoded_in_brackets = decode_string(s=s[i+1:j])
    # Construct decoded substring
    decoded_substring = multiplier * decoded_in_brackets
    # Continue processing remaining string
    if j < L - 2:
        decoded_remainder = decode_string(s=s[j+1:])
    else:
        decoded_remainder = ''
    return decoded_substring + decoded_remainder



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

    def test5(self) -> None:
        s = '5[a]'
        out = decode_string(s=s)
        expected = 'aaaaa'
        self.assertEqual(out, expected)

    def test6(self) -> None:
        s = '2[a]3[b]4[c]'
        out = decode_string(s=s)
        expected = 'aabbbcccc'
        self.assertEqual(out, expected)