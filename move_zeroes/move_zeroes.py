class Solution:
    def moveZeroes(self, nums: List[int]) -> None: # O(N)
        i = 0 # Index in new array
        j = 0 # Index in old array
        L = len(nums)
        while j < L: # O(N)
            if nums[j] != 0: # O(1)
                nums[i] = nums[j]
                i += 1
            j += 1
        for k in range(i, L): # O(N)
            nums[k] = 0 
        
