from collections import Counter


def get_first_unique_character(s: str) -> int:
    counter = Counter(s)
    unique_characters = set([char for char, count in counter.items() if count == 1])
    if len(unique_characters) == 0:
        return -1
    L = len(s)
    i = 0
    while i < L:
        if s[i] in unique_characters:
            return i
        i += 1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        return get_first_unique_character(s=s)