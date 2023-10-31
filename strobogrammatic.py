from unittest import TestCase

SAME_NUMBER = {0, 1, 8}
ILLEGAL_NUMBERS = {2, 3, 4, 5, 7}


def swap_integer(integer: int) -> int:
    if integer in SAME_NUMBER:
        return integer
    if integer == 6:
        return 9
    if integer == 9:
        return 6
    raise ValueError(f'Cannot swap integer {integer}!')


def is_strobogrammatic(num: str) -> bool:
    unique_characters = set(num)
    unique_integers = {int(char) for char in unique_characters}
    illegal_integers = unique_integers & ILLEGAL_NUMBERS
    if len(illegal_integers) > 0:
        return False
    num_integers = [int(char) for char in num]
    num_swapped = [swap_integer(integer=integer) for integer in num_integers]
    num_rotated = num_swapped[::-1]
    return num_integers == num_rotated


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        return is_strobogrammatic(num=num)


class TestStrobogrammatic(TestCase):
    def test1(self) -> None:
        test_cases = {
            '69': True,
            '88': True,
            '962': False,
        }
        for num, expected in test_cases.items():
            result = is_strobogrammatic(num=num)
            self.assertEqual(result, expected)
