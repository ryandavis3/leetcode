from unittest import TestCase
from typing import List


class Reachable:

    def __init__(self):
        self._reachable: Dict = {}

    def add(self, day: int, pass_days: int, reachable_day: int) -> None:
        if day not in self._reachable:
            self._reachable[day] = {}
        self._reachable[day][pass_days] = reachable_day


def get_reachable(days: List[int]) -> Reachable:
    passes = [1, 7, 30]
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


def get_min_cost_tickets(days: List[int], costs: List[int]) -> int:
    min_cost_table: List[List[int]] = []
    D = len(days)
    for _ in range(D):
        min_cost_row = [0] * D
        min_cost_table += [min_cost_row]
    for i in range(D):
        for j in range(D):
            if i == 0 and j == 0:
                min_cost_table[i][j] = costs[0]
                continue
            if i > j:
                min_cost_table[i][j] = min_cost_table[i-1][j]
                continue


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        pass


class TestReachable(TestCase):
    def test1(self) -> None:
        days = [1, 4, 6, 7, 8, 20]
        reachable = get_reachable(days=days)
        _reachable_expected = {1: {7: 0, 30: 0}, 2: {7: 0, 30: 0}, 3: {1: 2, 7: 0, 30: 0}, 4: {1: 3, 7: 0, 30: 0}, 5: {30: 0}}
        self.assertEqual(reachable._reachable, _reachable_expected)

class TestMinCost(TestCase):
    def test1(self) -> None:
        days = [1, 4, 6, 7, 8, 20]
        costs = [2, 7, 15]
        min_cost = get_min_cost_tickets(days=days, costs=costs)
        self.assertEqual(min_cost, 11)