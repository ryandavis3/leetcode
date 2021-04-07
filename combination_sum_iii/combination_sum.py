from typing import List

# Implement backtracking solution
def combinationSum3(k: int, n: int):
    solutions = []
    def backtrack(total: int, arr: List[int]):
        if total == n and len(arr) == k:
            solutions.append(arr)
            return
        if total > n or len(arr) > k:
            return
        if not arr:
            start = 1
        else:
            start = arr[-1]+1
        for i in range(start, 10):
            backtrack(total + i, arr + [i])
    backtrack(0, [])
    return solutions


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return combinationSum3(k, n)


if __name__ == "__main__":
    k = 3 
    n = 9
    result = combinationSum3(k, n)
    breakpoint()
