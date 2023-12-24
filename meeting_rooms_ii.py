from enum import Enum
from dataclasses import dataclass
from unittest import TestCase
from typing import Dict, List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        return get_min_meeting_rooms(intervals=intervals)


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
        self.points = sorted(set(points))
        self.events = events
        self.index = 0
        self.current_rooms = 0
        self.max_rooms = 0

    def step_forward(self) -> None:
        point = self.points[self.index]
        self.current_rooms += self.events[point]
        self.index += 1
        if self.current_rooms > self.max_rooms:
            self.max_rooms = self.current_rooms


def get_min_meeting_rooms(intervals: List[List[int]]) -> int:
    interval_set = IntervalSet(intervals=intervals)
    for _ in range(len(interval_set.points)):
        interval_set.step_forward()
    return interval_set.max_rooms


class TestIntervalSet(TestCase):
    def test1(self) -> None:
        intervals = [[0, 30], [5, 10], [15, 20]]
        interval_set = IntervalSet(intervals=intervals)
        points_expected = [0, 5, 10, 15, 20, 30]
        self.assertEqual(interval_set.points, points_expected)
        events_expected = {0: 1, 5: 1, 15: 1, 30: -1, 10: -1, 20: -1,}
        self.assertEqual(interval_set.events, events_expected)
        interval_set.step_forward()
        self.assertEqual(interval_set.current_rooms, 1)
        interval_set.step_forward()
        self.assertEqual(interval_set.current_rooms, 2)
        interval_set.step_forward()
        self.assertEqual(interval_set.current_rooms, 1)
        self.assertEqual(interval_set.max_rooms, 2)

    def test2(self) -> None:
        intervals = [[0, 30], [5, 10], [15, 20]]
        max_rooms = get_min_meeting_rooms(intervals=intervals)
        self.assertEqual(max_rooms, 2)

    def test3(self) -> None:
        intervals = [[7, 10], [2, 4]]
        max_rooms = get_min_meeting_rooms(intervals=intervals)
        self.assertEqual(max_rooms, 1)

    def test4(self) -> None:
        intervals = [[1, 10], [1, 5], [2, 7]]
        max_rooms = get_min_meeting_rooms(intervals=intervals)
        self.assertEqual(max_rooms, 3)