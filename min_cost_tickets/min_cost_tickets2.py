from typing import List
from functools import lru_cache

def mincostTickets(days: List[int], costs: List[int]) -> int:
    
    durations = [1, 7, 30]
    days_set = set(days)

    @lru_cache(None)
    def dp(i):
        if i > 365:
            return 0
        elif i in days_set:
            return min(dp(i + d) + c
                           for c, d in zip(costs, durations))
        else:
            return dp(i+1)
    
    return dp(1) 

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        return mincostTickets(days, costs)


if __name__ == "__main__":
    days = [1,4,6,7,8,20]
    costs = [2,7,15]
    result = mincostTickets(days, costs)
    print(result)
