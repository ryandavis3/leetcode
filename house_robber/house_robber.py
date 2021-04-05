from typing import List

def rob(nums: List[int]) -> int:
    L = len(nums)
    table = []
    for _ in range(2):
        table += [[None] * L]
    table[0][0] = nums[0]
    table[1][0] = 0
    for i in range(1, L):
        table[0][i] = table[1][i-1] + nums[i] 
        table[1][i] = max(table[0][i-1], table[1][i-1])
    breakpoint()
    return max(table[0][L-1], table[1][L-1])

class Solution:
    def rob(self, nums: List[int]) -> int:
        return rob(nums)

if __name__ == "__main__":
    #nums = [10, 1, 10, 1, 1, 10]
    #rob(nums)
    nums = [1,2,3,1]
    rob(nums)
