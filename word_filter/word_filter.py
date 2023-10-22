import unittest
from typing import Dict, List


def add_word_to_dict(_dict: Dict, word: str, index: int) -> None:
    # Word has only one or zero letters
    if len(word) <= 1:
        _dict[word] = index
        return None
    # First letter
    letter = word[0]
    # Remaining word
    remaining = word[1:]
    # Letter not in dictionary -> add it
    if letter not in _dict:
        _dict[letter]: Dict = {}
    # Recursively move to the next 
    add_word_to_dict(_dict=_dict[letter], word=remaining, index=index)


class WordTree:

    def __init__(self):
        self.word_tree: Dict = {}

    def add_word(self, word: str, index: int) -> None:
        add_word_to_dict(_dict=self.word_tree, word=word, index=index)



class WordFilter:

    def __init__(self, words: List[str]):
        # Instantiate word tree object forward
        self.word_tree_forward = WordTree()
        # Iterate over each word and add it
        for index, word in enumerate(words):
            self.word_tree_forward.add_word(word=word, index=index)
        # Instantiate word tree object backward
        self.word_tree_backward = WordTree()
        # Iterate over each word and add it
        words_backward = words[::-1]
        for index, word in enumerate(words_backward):
            self.word_tree_backward.add_word(word=word, index=index)

    def f(self, pref: str, suff: str) -> int:
        pass        


class TestWordFilter(unittest.TestCase):
    
    def test_1(self):
        words = ['apple']
        word_filter = WordFilter(words=words)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)