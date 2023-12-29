from collections import Counter
from unittest import TestCase


class Solution:
    def minDeletions(self, s: str) -> int:
        return get_min_deletions(s=s)


def get_min_deletions(s: str) -> int:
    # Initialize array of frequencies
    counter = Counter(s)
    frequency = [0] * 26
    for char, char_freq in counter.items():
        i = ord(char) - ord('a')
        frequency[i] = char_freq
    # Delete one character at a time
    frequency_set = set()
    n_deletions = 0
    for freq in frequency:
        if not freq:
            continue
        while freq in frequency_set and freq > 0:
            freq -= 1
            n_deletions += 1
        if freq > 0:
            frequency_set.add(freq)
    return n_deletions


class TestMinDeletions(TestCase):
    def test1(self) -> None:
        s = "aaabbbcc"
        n_deletions = get_min_deletions(s=s)
        self.assertEqual(n_deletions, 2)

    def test2(self) -> None:
        s = "ceabaacb"
        n_deletions = get_min_deletions(s=s)
        self.assertEqual(n_deletions, 2)

    def test3(self) -> None:
        s = "aab"
        n_deletions = get_min_deletions(s=s)
        self.assertEqual(n_deletions, 0)