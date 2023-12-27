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
        if self.tail is not None:
            print(self.tail.val)
        while self.tail is not None and self.tail.val <= cutoff_timestamp:
            print(self.tail.val)
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
        if self.tail is None:
            self.tail = node
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

    def test2(self) -> None:
        counter = HitCounter()
        counter.hit(timestamp=100)
        counter.hit(timestamp=151)
        hits = counter.getHits(timestamp=173)
        self.assertEqual(hits, 2)
        hits = counter.getHits(timestamp=179)
        self.assertEqual(hits, 2)
        counter.hit(timestamp=188)
        hits = counter.getHits(timestamp=250)
        self.assertEqual(hits, 3)
        hits = counter.getHits(timestamp=267)
        self.assertEqual(hits, 3)
        hits = counter.getHits(timestamp=396)
        self.assertEqual(hits, 3)
        hits = counter.getHits(timestamp=410)
        self.assertEqual(hits, 2)
        counter.hit(timestamp=547)
        counter.hit(timestamp=552)
        counter.hit(timestamp=605)
        counter.hit(timestamp=690)
        counter.hit(timestamp=707)
        hits = counter.getHits(timestamp=713)
        self.assertEqual(hits, 5)
        hits = counter.getHits(timestamp=797)
        self.assertEqual(hits, 5)
        hits = counter.getHits(timestamp=808)
        self.assertEqual(hits, 5)
        counter.hit(timestamp=859)
        hits = counter.getHits(timestamp=943)
        self.assertEqual(hits, 3)
        counter.hit(timestamp=956)
        counter.hit(timestamp=957)
