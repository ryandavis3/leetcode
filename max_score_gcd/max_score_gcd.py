import itertools
from math import gcd
from typing import List


def maxScore(nums: List[int]) -> int:
    
    # Use Dict to memoize results 
    memo = dict()

    # Backtrack to find solution
    def backtrack(i: int, index: List[int]) -> int:
       
        # Key is the turn and the index of remaining elements
        key = (i, frozenset(index))
        
        # If memoized, return
        if key in memo:
            return memo[key]

        # Reached the end! Only two elements!
        if len(index) == 2:
            return i * gcd(nums[index[0]], nums[index[1]])

        # Iterate over possible combinations
        combinations = list(itertools.combinations(index, 2))
        sub = []
        for comb in combinations:
            val = i * gcd(nums[comb[0]], nums[comb[1]])
            index_remain = [v for v in index if v not in comb] 
            sub += [val + backtrack(i+1, index_remain)]
        
        # Memoize and return result
        max_sum = max(sub)
        memo[key] = max_sum
        return max_sum

    # Start with full index
    index_start = list(range(len(nums)))
    return backtrack(1, index_start)


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        return maxScore(nums)


if __name__ == "__main__":
    nums = [3,4,6,8]
    result = maxScore(nums)
    nums = [1,2,3,4,5,6]
    result1 = maxScore(nums)
    nums = [878394,878394,878394,878394]
    result2 = maxScore(nums)
    print(result2)
