from unittest import TestCase


class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

    def add_next(self, node) -> None:
        if self.next is not None:
            raise ValueError('Next already set!')
        self.next = node


class HitCounter:

    def __init__(self):
        self.lookback_seconds = 300
        self.head = None
        self.tail = None
        self.n_hits = 0

    def apply_timestamp(self, timestamp: int) -> None:
        cutoff_timestamp = timestamp - self.lookback_seconds
        while self.tail is not None and self.tail.val <= cutoff_timestamp:
            self.tail = self.tail.next
            self.n_hits -= 1

    def hit(self, timestamp: int) -> None:
        node = Node(val=timestamp)
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        self.apply_timestamp(timestamp=timestamp)
        self.head.next = node
        self.head = node
        self.n_hits += 1

    def getHits(self, timestamp: int) -> int:
        self.apply_timestamp(timestamp=timestamp)
        return self.n_hits


class TestHitCounter(TestCase):
    def test1(self) -> None:
        counter = HitCounter()
        counter.hit(timestamp=1)
        counter.hit(timestamp=2)
        counter.hit(timestamp=3)
        hits = counter.getHits(timestamp=4)
        self.assertEqual(hits, 3)
        counter.hit(timestamp=300)
        hits = counter.getHits(timestamp=300)
        self.assertEqual(hits, 4)
        hits = counter.getHits(timestamp=301)
        self.assertEqual(hits, 3)
