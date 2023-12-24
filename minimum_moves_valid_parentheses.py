from unittest import TestCase


OPEN = '('
CLOSED = ')'


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        pass


def remove_parentheses(s: str) -> str:
    index_remove = set()
    open_parens_count = 0
    for i, char in enumerate(s):
        if char == CLOSED:
            if open_parens_count == 0:
                index_remove.add(i)
            else:
                open_parens_count -= 1
        elif char == OPEN:
            open_parens_count += 1


class TestMinRemove(TestCase):
    def test1(self) -> None:
        pass