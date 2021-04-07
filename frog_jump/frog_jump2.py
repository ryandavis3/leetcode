import sys
from functools import lru_cache
from typing import List

sys.setrecursionlimit(2500)

def canCross(stones: List[int]) -> bool:
    # Cannot make first jump
    if stones[1] - stones[0] != 1:
        return False
    # Set of stones
    stones_set = set(stones)
    L = len(stones)
    # Dynamic programming with memoization
    @lru_cache(None)
    def dp(val: int, k: int) -> bool:
        # k = 0 -> same spot; return False
        if k == 0:
            return False
        # Reached end!
        if val == stones[L - 1]:
            return True
        # Stone not in set
        if val not in stones_set:
            return False
        # Try different jumps
        return dp(val+k-1, k-1) or dp(val+k, k) or dp(val+k+1, k+1)
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
