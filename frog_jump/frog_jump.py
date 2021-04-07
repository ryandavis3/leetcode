import sys
from functools import lru_cache
from typing import List

sys.setrecursionlimit(2500)

def canCross(stones: List[int]) -> bool:
    if stones[1] - stones[0] != 1:
        return False
    stones_set = set(stones)
    L = len(stones)
    memo = {}

    def dp(val: int, k: int) -> bool:
        tup = (val, k)
        if tup in memo:
            return memo[tup]
        if k == 0:
            return False
        if val == stones[L - 1]:
            memo[tup] = True
            return True
        if val not in stones_set:
            memo[tup] = False
            return False
        jump1 = dp(val+k-1, k-1)
        if jump1:
            return True
        else:
            memo[tup] = False
        jump2 = dp(val+k, k)
        if jump2:
            return True
        else:
            memo[tup] = False
        jump3 = dp(val+k+1, k+1)
        if jump3:
            return True
        else:
            memo[tup] = False
        return False
    return dp(stones[1], 1)


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        return canCross(stones)


if __name__ == "__main__":
    stones = [0,1,3,5,6,8,12,17]
    result = canCross(stones)
    print(result)
    stones = [0,1,2,3,4,8,9,11]
    result = canCross(stones)
    print(result)
