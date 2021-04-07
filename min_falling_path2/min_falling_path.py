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
            options = []
            for jjj in range(m):
                if jj != jjj:
                    options += [matrix[i][jj] + path_sum[i+1][jjj]]
            path_sum[i][jj] = min(options)
        i -= 1
    min_sum = min(path_sum[0])
    return min_sum


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        return minFallingPathSum(matrix)


if __name__ == "__main__":
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    result = minFallingPathSum(matrix)
    print(result)
    matrix = [[-73,61,43,-48,-36],[3,30,27,57,10],[96,-76,84,59,-15],[5,-49,76,31,-7],[97,91,61,-46,67]]
    result = minFallingPathSum(matrix)
    print(result)
