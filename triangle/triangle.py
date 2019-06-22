from typing import List

# https://leetcode.com/problems/triangle/

def minimumTotal(triangle: List[List[int]]) -> int:
    """
    Given a triangle, find the minimum path sum from top to 
    bottom. Use O(n) extra space. Dynamic programming.
    """
    # Special cases: triangle has length 0 or 1
    if len(triangle) == 0:
        return 0
    if len(triangle) == 1:
        return triangle[0][0]
    # Parameters for loop. Use O(n) extra space by storing
    # only the minimum path sums for the current and previous
    # rows.
    row = 1
    L = len(triangle)
    min_sum_prev = triangle[0]
    while row < L:
        min_sum = [0] * (row+1)
        for i in range(row+1):
            # Recurrence relation: Min path sum at an index is equal
            # to the min path sum of adjacent values in previous row plus
            # the value at index.
            if i == 0:
                min_sum[i] = min_sum_prev[i] + triangle[row][i]
            elif i == row:
                min_sum[i] = min_sum_prev[i-1] + triangle[row][i]
            else:
                min_sum[i] = min([min_sum_prev[i-1] + triangle[row][i], min_sum_prev[i] + triangle[row][i]])
        row += 1
        min_sum_prev = min_sum
    return min(min_sum)

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return minimumTotal(triangle)
