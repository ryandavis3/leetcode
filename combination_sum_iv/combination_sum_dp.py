from typing import List

def combinationSum4(nums: List[int], target: int) -> List[List[int]]:
    dp = [0] * (target+1)
    dp[0] = 1
    for i in range(1, target+1):
        for num in nums:
            if num <= i:
                dp[i] += dp[i-num]
    return dp[-1]


class Solution:
    def combinationSum4(self, nums: int, target: int) -> int:
        return combinationSum4(nums, target)


if __name__ == "__main__":
    nums = [1,2,3]
    target = 4
    result = combinationSum4(nums, target)
    nums = [4,2,1]
    target = 32
    result = combinationSum4(nums, target)
    breakpoint()
