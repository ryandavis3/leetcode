from unittest import TestCase


L = 'L'
R = 'R'


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        return is_robot_bounded(instructions=instructions)


def is_robot_bounded(instructions: str) -> bool:
    degree = 0
    for instruction in instructions:
        if instruction == L:
            degree += 1
        elif instruction == R:
            degree -= 1
    return (degree % 4) != 0


class TestRobotBounded(TestCase):
    def test1(self) -> None:
        test_cases = {
            'GGLLGG': True,
            'GG': False,
            'GL': True
        }
        for instructions, expected in test_cases.items():
            result = is_robot_bounded(instructions=instructions)
            self.assertEqual(result, expected)