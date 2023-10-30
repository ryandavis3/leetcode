from math import ceil

LARGE = 10 ** 10


def get_max_sum_with_value(n: int, index: int, value: int) -> int:
    n_left = index
    left_sum = n_left * (value - 1 + value - n_left) / 2
    n_right = n - index - 1
    right_sum = n_right * (value - 1 + value - n_right) / 2
    return value + left_sum + right_sum


def max_value(n: int, index: int, maxSum: int) -> int:
    max_sum_value = LARGE
    value = maxSum
    while max_sum_value > maxSum:
        max_sum_value = get_max_sum_with_value(n=n, index=index, value=value)
        value -= 1
    return value


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        return max_value(n=n, index=index, maxSum=maxSum)