from unittest import TestCase
from typing import List, Tuple
from collections import Counter


def do_frequency_sort(s: str) -> str:
    counter = Counter(s)
    letter_freqs: List[Tuple] = []
    for letter, count in counter.items():
        letter_freq = (letter, count)
        letter_freqs += [letter_freq]
    letter_freqs_sorted = sorted(letter_freqs, key=lambda x: x[1], reverse=True)
    freq_sorted_s = ''
    for letter_freq in letter_freqs_sorted:
        letter, freq = letter_freq
        freq_sorted_s += letter * freq
    return freq_sorted_s


class Solution:
    def frequencySort(self, s: str) -> str:
        return do_frequency_sort(s=s)


class TestFrequencySort(TestCase):
    def test1(self) -> None:
        pass