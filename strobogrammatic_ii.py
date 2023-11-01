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
    def generate_from_number(num: str) -> List[str]:
        nums_generated: List[str] = []
        for increment_num in SAME_NUMBER:
            num_generated = increment_num + num + increment_num
            nums_generated += [num_generated]
        nums_generated += ['6' + num + '9']
        nums_generated += ['9' + num + '6']
        return nums_generated

    def generate_numbers_of_len(self, len: int) -> None:
        if len < 2:
            raise ValueError('Number length must be greater than two!')
        nums_len_minus_two = self.numbers[len-2]
        nums_generated_minus_two: List[str] = []
        for num in nums_len_minus_two:
            nums_generated = self.generate_from_number(num=num)
            nums_generated_minus_two += nums_generated
        self.numbers[len] = nums_generated_minus_two
        self.max_len = max(self.max_len, len)

    @staticmethod
    def is_valid_num(num: str) -> bool:
        if num == '0':
            return True
        if num[0] == '0':
            return False
        return True

    @staticmethod
    def remove_invalid_nums(nums: List[str]) -> List[str]:
        return [num for num in nums if StrobogrammaticNumbers.is_valid_num(num=num)]

    def generate_numbers_up_to_len(self, max_len: int) -> None:
        for len in range(2, max_len+1):
            self.generate_numbers_of_len(len=len)
        nums = self.numbers[max_len]
        nums = self.remove_invalid_nums(nums=nums)
        return nums


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        strobo = StrobogrammaticNumbers()
        nums = strobo.generate_numbers_up_to_len(max_len=n)
        return nums



class TestStrobogrammaticNumbers(TestCase):

    def test_generate_from_number(self) -> None:
        generated_nums = StrobogrammaticNumbers.generate_from_number(num='')
        generated_nums_expected = ['00', '11', '88', '69', '96']
        self.assertEqual(generated_nums, generated_nums_expected)

    def test_generate_numbers_of_len_2(self) -> None:
        strobo = StrobogrammaticNumbers()
        strobo.generate_numbers_of_len(len=2)
        numbers_expected = ['00', '11', '88', '69', '96']
        self.assertEqual(strobo.numbers[2], numbers_expected)

    def test_generate_numbers_of_len_3(self) -> None:
        strobo = StrobogrammaticNumbers()
        strobo.generate_numbers_of_len(len=3)
        numbers_expected = ['000', '010', '080', '101', '111', '181', '609', '619',
                            '689', '808', '818', '888', '906', '916', '986']
        self.assertEqual(sorted(strobo.numbers[3]), numbers_expected)

    def test_generate_numbers_up_to_len_4(self) -> None:
        strobo = StrobogrammaticNumbers()
        _ = strobo.generate_numbers_up_to_len(max_len=4)

