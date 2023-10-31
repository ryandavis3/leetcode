def repeated_character(s: str) -> str:
    chars_appeared = set()
    for char in s:
        if char in chars_appeared:
            return char
        chars_appeared.add(char)
    raise ValueError('No letter appears twice!')


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        return repeated_character(s=s)