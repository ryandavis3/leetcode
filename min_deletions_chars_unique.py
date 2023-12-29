from unittest import TestCase
from collections import Counter
from heapq import heapify, heappop, heappush


def get_min_deletions(s: str) -> int:
    counter = Counter(s)
    pq = [(-count, char) for char, count in counter.items()]
    heapify(pq)
    n_deletions = 0
    while pq:
        count_first, char_first = heappop(pq)
        if not pq:
            break
        if pq[0][0] == count_first:
            i = 0
            while i < len(pq) and pq[i][0] == count_first:
                i += 1
            for _ in range(i):
                count, char = heappop(pq)
                n_deletions += 1
                if count + 1 != 0:
                    heappush(pq, (count + 1, char))
            heapify(pq)
    return n_deletions


class Solution:
    def minDeletions(self, s: str) -> int:
        return get_min_deletions(s=s)


class TestMinDeletions(TestCase):
    def test1(self) -> None:
        s = 'aaabbbcc'
        min_deletions = get_min_deletions(s=s)
        self.assertEqual(min_deletions, 2)

    def test2(self) -> None:
        s = 'ceabaacb'
        min_deletions = get_min_deletions(s=s)
        self.assertEqual(min_deletions, 2)

    def test3(self) -> None:
        s = 'baeccdae'
        min_deletions = get_min_deletions(s=s)
        self.assertEqual(min_deletions, 5)