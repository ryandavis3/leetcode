from unittest import TestCase
from typing import List


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        return get_winner(colors=colors)


def count_moves_char(colors: str, char: str) -> int:
    moves = 0
    for i in range(1, len(colors) - 1):
        if colors[i] == char and colors[i-1] == char and colors[i+1] == char:
            moves += 1
    return moves


def get_winner(colors: str) -> bool:
    if len(colors) < 3:
        return False
    moves_a = count_moves_char(colors=colors, char='A')
    moves_b = count_moves_char(colors=colors, char='B')
    if moves_a > moves_b:
        return True
    return False


class TestWinner(TestCase):
    def test1(self) -> None:
        test_cases = {
            'AAABABB': True,
            'AA': False,
            'ABBBBBBBAAA': False,
        }
        for colors, expected_result in test_cases.items():
            result = get_winner(colors=colors)
            self.assertEqual(result, expected_result)
