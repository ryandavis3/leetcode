def arrayPairSum(self, nums: List[int]) -> int:
    nums = sorted(nums, reverse=True)
    array_sum = 0
    for i, num in enumerate(nums):
        if i % 2 == 1:
            array_sum += num
    return array_sum
