from typing import List
from unittest import TestCase


def get_min_cost_tickets(days: List[int], costs: List[int]) -> List[int]:
    K = max(days)
    day_costs = [None] * K
    j = 0
    min_day = min(days)
    min_day_cost = min(costs)
    for d in range(K):
        day = d + 1
        if day < min_day:
            day_costs[d] = 0
        elif day < days[j]:
            day_costs[d] = day_costs[d-1]
        elif day == 1:
            day_costs[d] = costs[0]
            j += 1
        else:
            min_cost = day_costs[d-1] + min_day_cost
            if d - 7 < 0:
                min_cost = min(min_cost, costs[1])
            else:
                min_cost = min(min_cost, day_costs[d-7] + costs[1])
            if d - 30 < 0:
                min_cost = min(min_cost, costs[2])
            else:
                min_cost = min(min_cost, day_costs[d - 30] + costs[2])
            day_costs[d] = min_cost
            j += 1
    return day_costs


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        return get_min_cost_tickets(days=days, costs=costs)[-1]


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