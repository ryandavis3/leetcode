from typing import Dict, List


def add_word_to_dict(_dict: Dict, word: str, index: int):
    # Word has only one or zero letters
    if len(word) <= 1:
        _dict[word] = index
    # First letter
    letter = word[0]
    # Remaining word
    remaining = word[1:]
    # Letter not in dictionary -> add it
    if letter not in _dict:
        _dict[letter]: Dict = {}
    # Recursively move to the next 
    add_word_to_dict(_dict=_dict[letter], word=remaining)


class WordTree:

    def __init__(self):
        self.word_tree: Dict = {}

    def add_word(self, word: str, index: int) -> None:
        add_word_to_dict(_dict=self.word_tree, word=word, index=index)



class WordFilter:

    def __init__(self, words: List[str]):
        

    def f(self, pref: str, suff: str) -> int:
        pass        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)