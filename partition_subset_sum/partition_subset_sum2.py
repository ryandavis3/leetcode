from typing import List


def canPartition(nums: List[int]) -> bool:
    # Degenerate case with no numbers
    if len(nums) == 0:
        return False
    # Target sum is non-integral
    target = sum(nums) / 2
    if target % 1 != 0:
        return False
    # Sort numbers
    nums = sorted(nums)
    table = []
    for i in range(len(nums)):
        table += [[0] * int(target + 1)]
    for i in range(0, len(nums)):
        table[i][0] = 1
    for jj in range(1, int(target + 1)):
        for i in range(0, len(nums)):
            if jj == nums[i]:
                table[i][jj] = 1
            if i > 0 and table[i-1][jj] == 1:
                table[i][jj] = 1
            if i > 0 and jj - nums[i] > 0 and table[i-1][jj-nums[i]] == 1:
                table[i][jj] = 1
    return bool(table[-1][-1])


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        return canPartition(nums)


if __name__ == "__main__":
    nums = [1,2,5]
    #nums = [3,3,3,4,5]
    a = canPartition(nums)
