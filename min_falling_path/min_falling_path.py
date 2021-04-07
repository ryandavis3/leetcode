from typing import List

def minFallingPathSum(matrix: List[List[int]]) -> int:
    # Dimensions of matrix
    n = len(matrix)
    m = len(matrix[0])
    # Empty path sum
    path_sum = []
    for i in range(n):
        path_sum += [[None] * m]
    # Build path sum
    for jj in range(m):
        path_sum[-1][jj] = matrix[-1][jj]
    i = n - 2
    while i >= 0:
        for jj in range(m):
            if jj == 0:
                path_sum[i][jj] = matrix[i][jj] + min(path_sum[i+1][jj], path_sum[i+1][jj+1])
            elif jj == m - 1:
                path_sum[i][jj] = matrix[i][jj] + min(path_sum[i+1][jj], path_sum[i+1][jj-1])
            else:
                path_sum[i][jj] = matrix[i][jj] + min(path_sum[i+1][jj], path_sum[i+1][jj-1], path_sum[i+1][jj+1])
        i -= 1
    min_sum = min(path_sum[0])
    return min_sum


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        return minFallingPathSum(matrix)


if __name__ == "__main__":
    matrix = [[2,1,3],[6,5,4],[7,8,9]]
    result = minFallingPathSum(matrix)
