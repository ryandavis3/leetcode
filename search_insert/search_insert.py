def searchInsert(nums, target):
    prev = -10000
    for i, num in enumerate(nums):
        if target > prev and target <= num:
            return i
        prev = num
    return i+1
