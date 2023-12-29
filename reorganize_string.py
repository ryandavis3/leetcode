from collections import Counter
from heapq import heapify, heappop, heappush

from unittest import TestCase


class Solution:
    def reorganizeString(self, s: str) -> str:
        pass


def reorganize_string(s: str) -> str:
    counter = Counter(s)
    pq = [(-count, char) for char, count in counter.items()]
    heapify(pq)
    ans = ''
    while pq:
        count_first, char_first = heappop(pq)
        if not ans or char_first != ans[-1]:
            ans += char_first
            if count_first + 1 != 0:
                heappush(pq, (count_first + 1, char_first))
        else:
            if not pq:
                return ''
            count_second, char_second = heappop(pq)
            ans += char_second
            if count_second + 1 != 0:
                heappush(pq, (count_second + 1, char_second))
            heappush(pq, (count_first, char_first))
    return ans


class TestReorganizeString(TestCase):
    def test1(self) -> None:
        s = 'aab'
        result = reorganize_string(s=s)
        expected = 'aba'
        self.assertEqual(result, expected)

    def test2(self) -> None:
        s = 'aaab'
        result = reorganize_string(s=s)
        expected = ''
        self.assertEqual(result, expected)

    def test3(self) -> None:
        s = 'bcaaa'
        result = reorganize_string(s=s)
        expected = 'abaca'
        self.assertEqual(result, expected)
