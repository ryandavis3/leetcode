from queue import Queue
from typing import Dict, List
from unittest import TestCase


LOWER_CASE_VOWELS = set(['a', 'e', 'i', 'o', 'u'])
UPPER_CASE_VOWELS = set(['A', 'E', 'I', 'O', 'U'])


class CharacterSet:
    def __init__(self):
        self._characters: Dict[str, Set[int]] = {}
        self._all_indices: Set[int] = set()

    def add_char(self, char: str) -> None:
        if char not in self._characters:
            self._characters[char] = 0
        self._characters[char] += 1

    def as_queue(self) -> Queue:
        char_queue = Queue()
        chars_sorted = sorted(list(self._characters.keys()))
        for char in chars_sorted:
            for _ in range(self._characters[char]):
                char_queue.put(char)
        return char_queue


def sort_vowels(s: str) -> str:
    # Character sets for lower and upper case vowels, consonants
    lower_case_vowels = CharacterSet()
    upper_case_vowels = CharacterSet()
    consonants = CharacterSet()
    # Populate character sets
    for i, char in enumerate(s):
        if char in LOWER_CASE_VOWELS:
            lower_case_vowels.add_char(char=char)
        elif char in UPPER_CASE_VOWELS:
            upper_case_vowels.add_char(char=char)
        else:
            consonants.add_char(char=char)


class Solution:
    def sortVowels(self, s: str) -> str:
        pass


class TestCharacterSet(TestCase):
    def test1(self) -> None:
        chars = ['e', 'a', 'i', 'a']
        character_set = CharacterSet()
        for char in chars:
            character_set.add_char(char=char)
        char_queue = character_set.as_queue()
        chars_sorted: List[str] = []
        while not char_queue.empty():
            chars_sorted += [char_queue.get()]
        chars_sorted_expected = ['a', 'a', 'e', 'i']
        self.assertEqual(chars_sorted, chars_sorted_expected)

class TestSortVowels(TestCase):
    def test1(self) -> None:
        pass