import unittest
from typing import Dict, List, Union


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


def get_indices_in_tree(tree: Union[Dict, int]) -> List[int]:
    if isinstance(tree, int):
        return [tree]
    indices: List[int] = []
    for _, subtree in tree.items():
        indices_subtree = get_indices_in_tree(tree=subtree)
        indices += indices_subtree
    return indices


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
        for index, word in enumerate(words):
            word_backward = word[::-1]
            self.word_tree_backward.add_word(word=word_backward, index=index)

    def f(self, pref: str, suff: str) -> int:
        pass        


class TestTree(unittest.TestCase):
    def test_1(self) -> None:
        tree = {'a': {'b': 0, 'c': 1, 'd': {'e': 2}}}
        indices = get_indices_in_tree(tree=tree)
        indices_expected = [0, 1, 2]
        self.assertEqual(indices, indices_expected)

class TestWordFilter(unittest.TestCase):
    def test_1(self) -> None:
        words = ['apple']
        word_filter = WordFilter(words=words)
        word_tree_forward_expected = {'a': {'p': {'p': {'l': {'e': 0}}}}}
        word_tree_forward = word_filter.word_tree_forward.word_tree
        self.assertEqual(word_tree_forward, word_tree_forward_expected)
        word_tree_backward = word_filter.word_tree_backward.word_tree
        word_tree_backward_expected = {'e': {'l': {'p': {'p': {'a': 0}}}}}
        self.assertEqual(word_tree_backward, word_tree_backward_expected)        

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)