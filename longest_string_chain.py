from unittest import TestCase
from typing import Dict, List, Set


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
    def build_successor_dict(words: List[str]) -> Dict[str, Set[str]]:
        successor_dict: Dict[str, Set[str]] = {}
        for word in words:
            word_successors = set()
            for potential_successor in words:
                if WordsManager.is_successor(word=word, word_successor=potential_successor):
                    word_successors.add(potential_successor)
            if word_successors:
                successor_dict[word] = word_successors
        return successor_dict


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

    def test_build_successor_dict(self) -> None:
        words = ["a", "b", "ba", "bca", "bda", "bdca"]
        successor_dict = WordsManager.build_successor_dict(words=words)
        successor_dict_expected = {'a': {'ba'}, 'b': {'ba'}, 'ba': {'bda', 'bca'}, 'bca': {'bdca'}, 'bda': {'bdca'}}
        self.assertEqual(successor_dict, successor_dict_expected)

