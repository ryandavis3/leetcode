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

    def hit(self, timestamp: int) -> None:

    def getHits(self, timestamp: int) -> int:
