from typing import Dict, List


class WordTree:

    def __init__(self):
        self.word_tree: Dict = {}

    def add_word(self, word: str) -> None:
        letter = word[0]
        remaining = word[1:]


class WordFilter:

    def __init__(self, words: List[str]):
        

    def f(self, pref: str, suff: str) -> int:
        pass        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)