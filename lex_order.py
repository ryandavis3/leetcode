# https://leetcode.com/problems/verifying-an-alien-dictionary/

from typing import Dict, List


class LexOrder:

    def __init__(self, order: str) -> None:
        self._order: Dict[str, int] = {}
        for i, char in enumerate(order):
            self._order[char] = i

    def get_lex_position(self, char: str) -> int:
        if char not in self._order:
            raise KeyError(f'Character {char} not in dictionary!')
        return self._order[char]

    def is_word_couple_ordered(self, word: str, word_after: str) -> bool:
        if word == word_after:
            return True
        i = 0
        len_word = len(word)
        len_word_after = len(word_after)
        while i < len_word and i < len_word_after:
            char = word[i]
            char_after = word_after[i]
            lex_position_char = self.get_lex_position(char=char)
            lex_position_char_after = self.get_lex_position(char=char_after)
            if lex_position_char_after < lex_position_char:
                return False
            if lex_position_char_after > lex_position_char:
                return True
            i += 1
        if i >= len_word_after:
            return False
        return True

    def is_word_list_ordered(self, words: List[str]) -> bool:
        num_words = len(words)
        if num_words == 1:
            return True
        for i in range(num_words-1):
            is_ordered = self.is_word_couple_ordered(word=words[i], word_after=words[i+1])
            if not is_ordered:
                return False
        return True


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        lex_order = LexOrder(order=order)
        return lex_order.is_word_list_ordered(words=words)