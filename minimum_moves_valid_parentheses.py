from unittest import TestCase


OPEN = '('
CLOSED = ')'


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        pass


def remove_parentheses(s: str) -> str:
    stack = list()
    index_remove = set()
    for i, char in enumerate(s):
        if char == OPEN:
            stack.append(i)
        elif char == CLOSED:
            if not stack:
                index_remove.add(i)
            else:
                stack.pop()
    for char in stack:
        index_remove.add(char)
    s_cleaned = [char for i, char in enumerate(s) if i not in index_remove]
    return ''.join(s_cleaned)



class TestMinRemove(TestCase):
    def test1(self) -> None:
        s = "lee(t(c)o)de)"
        s_cleaned = remove_parentheses(s=s)
        s_expected = "lee(t(c)o)de"
        self.assertEqual(s_cleaned, s_expected)

    def test2(self) -> None:
        test_cases = {
            'a)b(c)d': 'ab(c)d',
            '))((': '',
            '(((a)': '(a)'
        }
        for s, s_expected in test_cases.items():
            s_cleaned = remove_parentheses(s=s)
            self.assertEqual(s_cleaned, s_expected)