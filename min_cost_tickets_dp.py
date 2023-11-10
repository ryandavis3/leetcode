from unittest import TestCase
from typing import List, Optional


class Reachable:

    def __init__(self):
        self._reachable: Dict = {}

    def add(self, day: int, pass_days: int, reachable_day: int) -> None:
        if day not in self._reachable:
            self._reachable[day] = {}
        self._reachable[day][pass_days] = reachable_day

    def get_reachable_day(self, day: int, pass_days: int) -> Optional[int]:
        if day not in self._reachable:
            return None
        if pass_days not in self._reachable[day]:
            return None
        return self._reachable[day][pass_days]


def get_reachable(days: List[int]) -> Reachable:
    passes = [7, 30]
    reachable = Reachable()
    for i, _ in enumerate(days):
        if i == 0:
            continue
        for pass_days in passes:
            j = 0
            found = False
            while not found and j < i:
                if days[j] >= days[i] - pass_days:
                    found = True
                    reachable.add(day=i, pass_days=pass_days, reachable_day=j)
                j += 1
    return reachable


def get_min_cost_tickets(days: List[int], costs: List[int]) -> List[List[int]]:
    reachable = get_reachable(days=days)
    min_cost_table: List[List[int]] = []
    D = len(days)
    for _ in range(D):
        min_cost_table += [[0] * D]
    for i in range(D):
        for j in range(D):
            if i == 0 and j == 0:
                min_cost_table[i][j] = costs[0]
                continue
            if i > j:
                min_cost_table[i][j] = min_cost_table[i-1][j]
                continue
            min_cost = min_cost_table[i][j-1] + costs[0]
            reachable_7 = reachable.get_reachable_day(day=j, pass_days=7)
            if reachable_7 is not None:
                cost_7 = min_cost_table[i][reachable_7] + costs[1]
                min_cost = min(min_cost, cost_7)
            reachable_30 = reachable.get_reachable_day(day=j, pass_days=30)
            if reachable_30 is not None:
                cost_30 = min_cost_table[i][reachable_30] + costs[2]
                min_cost = min(min_cost, cost_30)
            min_cost_table[i][j] = min_cost
    return min_cost_table


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        min_cost_table = get_min_cost_tickets(days=days, costs=costs)
        min_cost = min_cost_table[-1][-1]
        return min_cost


class TestReachable(TestCase):
    def test1(self) -> None:
        days = [1, 4, 6, 7, 8, 20]
        reachable = get_reachable(days=days)
        _reachable_expected = {1: {7: 0, 30: 0}, 2: {7: 0, 30: 0}, 3: {7: 0, 30: 0}, 4: {7: 0, 30: 0}, 5: {30: 0}}
        self.assertEqual(reachable._reachable, _reachable_expected)


class TestMinCost(TestCase):
    def test1(self) -> None:
        days = [1, 4, 6, 7, 8, 20]
        costs = [2, 7, 15]
        min_cost_table = get_min_cost_tickets(days=days, costs=costs)
        min_cost = min_cost_table[-1][-1]
        self.assertEqual(min_cost, 11)

    def test2(self) -> None:
        days = [1, 4, 6, 7, 8, 20]
        costs = [7, 2, 15]
        min_cost_table = get_min_cost_tickets(days=days, costs=costs)
        min_cost = min_cost_table[-1][-1]
        self.assertEqual(min_cost, 6)

