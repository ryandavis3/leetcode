from unittest import TestCase
from typing import Dict, List

SAME_NUMBER = ['0', '1', '8']

class StrobogrammaticNumbers:
    def __init__(self):
        self.numbers: Dict[int, str] = {}
        self.numbers[0] = ['']
        self.numbers[1] = ['0', '1', '8']
        self.max_len = 1

    @staticmethod
    def generate_from_number(self, num: str) -> List[str]:
        nums_generated: List[str] = []
        for increment_num in SAME_NUMBER:
            num_generated = increment_num + num + increment_num
            nums_generated += [num_generated]
        nums_generated += ['6' + num + '9']
        nums_generated += ['9' + num + '6']
        return num_generated

    def generate_numbers_of_len(self, len: int) -> None:
        if len < 2:
            raise ValueError('Number length must be greater than two!')
        numbers_len_minus_two = self.numbers[len-2]


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        pass


class TestStrobogrammaticNumbers(TestCase):

    def test_generate_from_number(self) -> None:
        generated_nums = StrobogrammaticNumbers.generate_from_number(num='')
        generated_nums_expected = ['00', '11', '88', '69', '96']
        self.assertEqual(generated_nums, generated_nums_expected)
