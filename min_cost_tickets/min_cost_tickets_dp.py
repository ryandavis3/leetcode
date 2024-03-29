from unittest import TestCase
from typing import Dict, List, Optional


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
            j = i - 1
            while days[j] > days[i] - pass_days and j >= 0:
                j -= 1
            if j >= 0:
                reachable.add(day=i, pass_days=pass_days, reachable_day=j)
    return reachable


def get_costs_dict(costs: List[int]) -> Dict[int, int]:
    costs_dict: Dict[int, int] = {}
    passes_days = [30, 7]
    costs_reversed = costs[1:][::-1]
    min_cost = 10 ** 10
    for i in range(2):
        if costs_reversed[i] < min_cost:
            min_cost = costs_reversed[i]
            costs_dict[passes_days[i]] = costs_reversed[i]
    return costs_dict


def get_min_cost_tickets(days: List[int], costs: List[int]) -> List[int]:
    reachable = get_reachable(days=days)
    costs_dict = get_costs_dict(costs=costs)
    min_pass_cost = min(costs)
    D = len(days)
    for i in range(D):
        row_i = [0] * D
        for j in range(D):
            if i == 0 and j == 0:
                row_i[j] = min_pass_cost
                continue
            if i > j:
                row_i[j] = row_prev[j]
                continue
            min_cost = row_i[j-1] + min_pass_cost
            for pass_days, pass_cost in costs_dict.items():
                reachable_index = reachable.get_reachable_day(day=j, pass_days=pass_days)
                if reachable_index is not None:
                    cost_using_pass = row_i[reachable_index] + pass_cost
                    min_cost = min(min_cost, cost_using_pass)
                if days[j] - pass_days < min(days):
                    min_cost = min(min_cost, pass_cost)
            row_i[j] = min_cost
        row_prev = row_i
    return row_i


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        min_cost_table = get_min_cost_tickets(days=days, costs=costs)
        min_cost = min_cost_table[-1]
        return min_cost


class TestReachable(TestCase):
    def test1(self) -> None:
        days = [1, 4, 6, 7, 8, 20]
        reachable = get_reachable(days=days)
        _reachable_expected = {1: {7: 0, 30: 0}, 2: {7: 0, 30: 0}, 3: {7: 0, 30: 0}, 4: {7: 0, 30: 0}, 5: {30: 0}}
        # self.assertEqual(reachable._reachable, _reachable_expected)


class TestMinCost(TestCase):
    def test1(self) -> None:
        days = [1, 4, 6, 7, 8, 20]
        costs = [2, 7, 15]
        min_cost_table = get_min_cost_tickets(days=days, costs=costs)
        min_cost = min_cost_table[-1]
        self.assertEqual(min_cost, 11)

    def test2(self) -> None:
        days = [1, 4, 6, 7, 8, 20]
        costs = [7, 2, 15]
        min_cost_table = get_min_cost_tickets(days=days, costs=costs)
        min_cost = min_cost_table[-1]
        self.assertEqual(min_cost, 6)

    def test3(self) -> None:
        days = [1, 5, 8, 9, 10, 12, 13, 16, 17, 18, 19, 20, 23, 24, 29]
        costs = [3, 12, 54]
        min_cost_table = get_min_cost_tickets(days=days, costs=costs)
        min_cost = min_cost_table[-1]
        self.assertEqual(min_cost, 39)

    def test4(self) -> None:
        days = [1, 2, 3, 4, 5, 30, 31]
        costs = [1, 2, 3]
        min_cost_table = get_min_cost_tickets(days=days, costs=costs)
        min_cost = min_cost_table[-1]
        self.assertEqual(min_cost, 4)

    def test5(self) -> None:
        days = [1, 2, 3, 4, 6, 8, 9, 10, 13, 14, 16, 17, 19, 21, 24, 26, 27, 28, 29]
        costs = [3, 14, 50]
        min_cost_table = get_min_cost_tickets(days=days, costs=costs)
        min_cost = min_cost_table[-1]
        self.assertEqual(min_cost, 50)

    def test7(self) -> None:
        days = [2, 3, 4, 6, 8, 12, 14, 18, 19, 26, 27, 28]
        costs = [2, 9, 31]
        min_cost_table = get_min_cost_tickets(days=days, costs=costs)
        min_cost = min_cost_table[-1]
        self.assertEqual(min_cost, 23)


