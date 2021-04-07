import sys
from typing import List
from functools import lru_cache

sys.setrecursionlimit(2500)

def minJumps(arr: List[int]) -> int:
    
    L = len(arr) - 1
    # Get indices of each number in array
    index_dict = {}
    for i, num in enumerate(arr):
        if num not in index_dict:
            index_dict[num] = set()
        if i != 0:
            index_dict[num].add(i)
   
    memo = {i:10000 for i in range(len(arr))}

    @lru_cache(None)
    def dp(i):
        # Reached the end!
        if i == L - 1:
            return 0
        # Array indices
        steps = index_dict[arr[i]]
        steps = steps - {i}
        options = []
        for step in steps:
            options += [1 + dp(step)]
        if i - 1 > 0:
            options += [1 + dp(i-1)]
        options += [dp(i+1)]
        return min(options)
    
    return dp(0)


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        pass


if __name__ == "__main__":
    arr = [100,-23,-23,404,100,23,23,23,3,404]
    result = minJumps(arr)
    print(result)
