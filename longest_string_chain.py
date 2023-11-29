from unittest import TestCase
from typing import Dict, List, Set


class WordsManager:
    def __init__(self, words: List[str]):
        self.words = words
        self.successor_dict = self.build_successor_dict(words=words)
        self.words_with_successors = set(self.successor_dict.keys())

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


def dfs(word: str, predecessors: Set, words_manager: WordsManager, memo: Dict[str, int]) -> int:
    if word in memo:
        return memo[word]
    if word not in words_manager.successor_dict:
        memo[word] = 1
        return 1
    successors = words_manager.successor_dict[word] - predecessors
    longest_chain = 0
    predecessors.add(word)
    for successor in successors:
        len_chain = dfs(word=successor, predecessors=predecessors.copy(), words_manager=words_manager, memo=memo)
        if len_chain > longest_chain:
            longest_chain = len_chain
    memo[word] = 1 + longest_chain
    return 1 + longest_chain


def longest_str_chain(words: List[str]) -> int:
    memo: Dict[str, int] = {}
    words_manager = WordsManager(words=words)
    words = sorted(words)
    max_len = 0
    for word in words:
        len_starting_word = dfs(word=word, predecessors=set(), words_manager=words_manager, memo=memo)
        if len_starting_word > max_len:
            max_len = len_starting_word
    return max_len


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        pass


class TestWordsManager(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.words = ["a", "b", "ba", "bca", "bda", "bdca"]

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
        successor_dict = WordsManager.build_successor_dict(words=self.words)
        successor_dict_expected = {'a': {'ba'}, 'b': {'ba'}, 'ba': {'bda', 'bca'}, 'bca': {'bdca'}, 'bda': {'bdca'}}
        self.assertEqual(successor_dict, successor_dict_expected)

    def test_init(self) -> None:
        _ = WordsManager(words=self.words)


class TestLongestStrChain(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.words = ["a", "b", "ba", "bca", "bda", "bdca"]

    def test_dfs1(self) -> None:
        words = ["a", "b", "ba", "bca"]
        words_manager = WordsManager(words=words)
        len_longest = dfs(word='a', predecessors=set(), words_manager=words_manager, memo=dict())
        self.assertEqual(len_longest, 3)
        len_longest = dfs(word='b', predecessors=set(), words_manager=words_manager, memo=dict())
        self.assertEqual(len_longest, 3)

    def test_dfs2(self) -> None:
        words_manager = WordsManager(words=self.words)
        len_longest = dfs(word='bca', predecessors=set(), words_manager=words_manager, memo=dict())
        self.assertEqual(len_longest, 2)
        len_longest = dfs(word='a', predecessors=set(), words_manager=words_manager, memo=dict())
        self.assertEqual(len_longest, 4)

    def test_dfs3(self) -> None:
        words = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]
        words_manager = WordsManager(words=words)
        len_longest = dfs(word='xb', predecessors=set(), words_manager=words_manager, memo=dict())
        self.assertEqual(len_longest, 5)

    def test_dfs4(self) -> None:
        words = ["abcd", "dbqca"]
        words_manager = WordsManager(words=words)
        len_longest = dfs(word='abcd', predecessors=set(), words_manager=words_manager, memo=dict())
        self.assertEqual(len_longest, 1)

    def test_longest_str_chain1(self) -> None:
        max_len = longest_str_chain(words=self.words)
        self.assertEqual(max_len, 4)