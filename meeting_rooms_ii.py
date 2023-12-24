from enum import Enum
from dataclasses import dataclass
from unittest import TestCase
from typing import Dict, List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        pass


@dataclass(frozen=True)
class Interval:
    num: int
    start: int
    end: int

    def __post_init__(self):
        if self.start > self.end:
            raise ValueError('start cannot be before end!')


class IntervalSet:

    def __init__(self, intervals: List[List[int]]):
        points: List[int] = []
        events: Dict[int, Event] = {}
        for interval in intervals:
            start, end = interval
            points.append(start)
            points.append(end)
            if start not in events:
                events[start] = 0
            if end not in events:
                events[end] = 0
            events[start] += 1
            events[end] -= 1
        self.points = sorted(points)
        self.events = events


def get_min_meeting_rooms(intervals: List[List[int]]) -> int:
    pass


class TestIntervalSet(TestCase):
    def test1(self) -> None:
        intervals = [[0, 30], [5, 10], [15, 20]]
        interval_set = IntervalSet(intervals=intervals)
        points_expected = [0, 5, 10, 15, 20, 30]
        self.assertEqual(interval_set.points, points_expected)
        events_expected = {0: 1, 5: 1, 15: 1, 30: -1, 10: -1, 20: -1,}
        self.assertEqual(interval_set.events, events_expected)