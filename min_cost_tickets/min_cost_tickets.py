from typing import List

def subtractDays(days: List[int], start: int, diff: int) -> int:
    pass

def mincostTickets(days: List[int], costs: List[int]) -> int:
    L = len(days)
    lengths = [1, 7, 30]
    table = []
    for i in range(len(costs)):
        table += [[0] * L]
    for jj in range(len(days)):
        table[0][jj] = costs[0] * (jj + 1)
    for i in range(1, len(costs)):
        for jj in range(len(days)):
            options = []
            options += [table[i-1][jj]]
            if jj + 1 < lengths[i]:
                options += [costs[i]]
            else:
                breakpoint()
                options += [table[i][jj - lengths[i]] + costs[i]]
            table[i][jj] = min(options)


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        pass


if __name__ == "__main__":
    days = [1,4,6,7,8,20]
    costs = [2,7,15]
    result = mincostTickets(days, costs)
