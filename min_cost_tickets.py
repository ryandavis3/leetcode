from typing import Dict, List, Optional


class MinCosts:

    def __init__(self, min_costs_dict: Optional[Dict[int, int]]=None)
        self.min_costs_dict = min_costs_dict

    def update_cost(self, day: int, total_cost: int) -> None:
        if day not in self.min_costs_dict:
            self.min_costs_dict[day] = total_cost
            return None
        if total_cost < self.min_costs_dict[day]:
            self.min_costs_dict[day] = total_cost



def get_min_cost_tickets(days: List[int], costs: List[int], min_costs: MinCosts) -> MinCosts:
    start_day = days[0]
    end_day = days[-1]
    one_day_next = [day for day in days if day < start_day + 1]
    if not one_day_next:
        min_costs.update_cost(day=end_day, total_cost=costs[0])
    else:
        one_day_cost = get_min_cost_tickets(days=one_day_next, costs=costs, min_costs=min_costs)
    seven_day_next = [day for day in days if day < start_day + 7]
    if not seven_day_next:
        min_costs.update_cost(day=end_day, total_cost=costs[1])
    thirty_day_next = [day for day in days if day < start_day + 30]
    if not thirty_day_next:
        min_costs.update_cost(day=end_day, total_cost=costs[2])


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        pass