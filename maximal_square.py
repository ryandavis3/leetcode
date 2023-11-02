from unittest import TestCase
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class MaximalSquareResults:
    square_size: List[List[int]]
    max_square_size: int
    max_square_area: int


def get_maximal_square(matrix: List[List[str]]) -> int:
    # Create empty array for max square size
    square_size: List[List[int]] = []
    rows = len(matrix)
    cols = len(matrix[0])
    for _ in range(rows):
        square_size += [[0] * cols]
    # Iterate through rows and columns
    for i in range(rows):
        for j in range(cols):
            # Edge of matrix -> cannot create square
            if i == 0 or j == 0:
                print(square_size[i][j])
                print(matrix[i][j])
                square_size[i][j] = int(matrix[i][j])
                continue
            # Value is zero -> square size is always zero
            if int(matrix[i][j]) == 0:
                square_size[i][j] = 0
            left = int(matrix[i][j-1])
            diag = int(matrix[i-1][j-1])
            top = int(matrix[i-1][j])
            # Max square size is extended from the smallest adjacent square
            square_size[i][j] = min(left, diag, top) + 1
    # Find max square size
    max_square_size = 0
    for i in range(rows):
        for j in range(cols):
            if square_size[i][j] > max_square_size:
                max_square_size = square_size[i][j]
    # Return results
    maximal_square_results = MaximalSquareResults(
        square_size=square_size,
        max_square_size=max_square_size,
        max_square_area=max_square_size ** 2,
    )
    return maximal_square_results


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maximal_square_results = get_maximal_square(matrix=matrix)
        return maximal_square_results.max_square_area


class TestMaximalSquare(TestCase):
    def test1(self) -> None:
        matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
                  ["1", "0", "0", "1", "0"]]
        maximal_square_results = get_maximal_square(matrix=matrix)
        self.assertEqual(maximal_square_results.max_square_area, 4)

    def test2(self) -> None:
        matrix = [["0", "1"], ["1", "0"]]
        maximal_square_results = get_maximal_square(matrix=matrix)
        self.assertEqual(maximal_square_results.max_square_area, 1)

    def test3(self) -> None:
        matrix = [["0"]]
        maximal_square_results = get_maximal_square(matrix=matrix)
        self.assertEqual(maximal_square_results.max_square_area, 0)
