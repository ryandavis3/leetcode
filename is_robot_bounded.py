from unittest import TestCase


G = 'G'
L = 'L'
R = 'R'


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        return is_robot_bounded(instructions=instructions)


def is_robot_bounded(instructions: str) -> bool:
    degree = 0
    x = 0
    y = 0
    for instruction in instructions:
        if instruction == L:
            degree = (degree + 1) / 4
        elif instruction == R:
            degree = (degree - 1) / 4
        if instruction == G:
            # north
            if degree == 0:
                y += 1
            # west
            elif degree == 1:
                x -= 1
            # south
            elif degree == 2:
                y -= 1
            else:
                x += 1
    return (degree % 4) != 0 or (x==0 and y==0)


class TestRobotBounded(TestCase):
    def test1(self) -> None:
        test_cases = {
            'GGLLGG': True,
            'GG': False,
            'GL': True,
            'GLRLLGLL': True
        }
        for instructions, expected in test_cases.items():
            result = is_robot_bounded(instructions=instructions)
            self.assertEqual(result, expected)