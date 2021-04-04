def findPeakElement(nums: List[int]) -> int:
    L = len(nums)
    if L <= 1:
        return 0
    for i in range(0, L):
        if i == 0 and nums[i] > nums[i+1]:
            return i
        if i == L-1 and nums[i] > nums[i-1]:
            return i
        if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
            return i
    return 0

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return findPeakElement(nums)
