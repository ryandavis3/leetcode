from typing import List

def subtractDays(days: List[int], start: int, diff: int) -> int:
    day = start - diff
    days_set = set(days)
    while day not in days_set:
        day -= 1
        if day < 1:
            return -1
    return days.index(day)

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
            if days[jj] <= lengths[i]:
                options += [costs[i]]
            else:
                for ii in range(i):
                    if i == 1 and jj == 4:
                        pass
                    col = subtractDays(days, days[jj], lengths[ii])
                    if col != -1:
                        options += [table[i][col] + costs[ii]]
            table[i][jj] = min(options)
    breakpoint()
    return table[-1][-1]

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        return mincostTickets(days, costs)


if __name__ == "__main__":
    days = [1,4,6,7,8,20]
    costs = [2,7,15]
    #result = mincostTickets(days, costs)
    days = [1,4,6,9,10,11,12,13,14,15,16,17,18,20,21,22,23,27,28]
    costs = [3,13,45]
    result = mincostTickets(days, costs)
