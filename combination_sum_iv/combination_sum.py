from typing import List

# Implement backtracking solution
def combinationSum4(nums: int, target: int):
    solutions = []
    def backtrack(total: int, arr: List[int]):
        print(solutions)
        if total == target:
            solutions.append(arr)
            return
        if total > target:
            return
        for i in nums:
            backtrack(total + i, arr + [i])
    backtrack(0, [])
    solutions = [tuple(s) for s in solutions]
    return len(solutions)


class Solution:
    def combinationSum4(self, k: int, n: int) -> List[List[int]]:
        return combinationSum4(k, n)

if __name__ == "__main__":
    nums = [1,2,3] 
    target = 4
    #result = combinationSum4(nums, target)
    nums = [4,2,1]
    target = 32
    result = combinationSum4(nums, target)
    breakpoint()
