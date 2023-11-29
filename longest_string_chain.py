from unittest import TestCase
from typing import Dict, List


class WordsManager:
    def __init__(self, words: List[str]):
        pass

    @staticmethod
    def is_successor(word, word_successor) -> bool:
        if len(word) + 1 != len(word_successor):
            return False
        L = len(word_successor)
        is_inserted = False
        offset = 0
        for i in range(L):
            if i - offset > len(word) - 1:
                return True
            if word[i - offset] != word_successor[i]:
                if is_inserted:
                    return False
                is_inserted = True
                offset = 1
        return True

    @staticmethod
    def build_successor_dict(words: List[str]) -> Dict:
        pass


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        pass


class TestWordsManager(TestCase):
    def test_is_successor1(self) -> None:
        test_cases = {
            ('a', 'ab'): True,
            ('abde', 'abcde'): True,
            ('aaa', 'aaa'): False,
            ('abcde', 'abde'): False,
        }
        for words, expected in test_cases.items():
            word, word_successor = words
            result = WordsManager.is_successor(word=word, word_successor=word_successor)
            self.assertEqual(result, expected)

