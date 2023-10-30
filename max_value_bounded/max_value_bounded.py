from math import ceil

def max_sum_with_value(n: int, index: int, value: int) -> int:
    n_left = index
    left_sum = n_left * (value - 1 + value - n_left) / 2
    n_right = n - index - 1
    right_sum = n_right * (value - 1 + value - n_right) / 2
    return value + left_sum + right_sum

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        pass