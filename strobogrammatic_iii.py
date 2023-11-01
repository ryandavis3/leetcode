from unittest import TestCase
from typing import Dict, List


SAME_NUMBER = ['0', '1', '8']


class StrobogrammaticNumbers:
    def __init__(self):
        self.numbers: Dict[int, str] = {}
        self.numbers[0] = ['']
        self.numbers[1] = ['0', '1', '8']
        self.max_len = 1

    def get_all_numbers(self) -> List[str]:
        nums: List[str] = []
        for len, nums_len in self.numbers.items():
            if len > 0:
                nums += nums_len
        return nums

    @staticmethod
    def generate_from_number(num: str, high: int) -> List[str]:
        nums_generated: List[str] = []
        for increment_num in SAME_NUMBER:
            num_generated = increment_num + num + increment_num
            if int(num_generated) <= high:
                nums_generated += [num_generated]
        six_start_num = '6' + num + '9'
        if int(six_start_num) <= high:
            nums_generated += [six_start_num]
        nine_start_num = '9' + num + '6'
        if int(nine_start_num) <= high:
            nums_generated += [nine_start_num]
        return nums_generated

    def generate_numbers_of_len(self, len: int, high: int) -> bool:
        if len < 2:
            raise ValueError('Number length must be greater than two!')
        nums_len_minus_two = self.numbers[len-2]
        nums_generated_minus_two: List[str] = []
        for num in nums_len_minus_two:
            nums_generated = self.generate_from_number(num=num, high=high)
            nums_generated_minus_two += nums_generated
        self.numbers[len] = nums_generated_minus_two
        self.max_len = max(self.max_len, len)
        if not nums_generated_minus_two:
            return False
        return True

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

    def generate_numbers_up_to_len(self, max_len: int, low: int, high: int) -> List[int]:
        for len in range(2, max_len+1):
            self.generate_numbers_of_len(len=len, high=high)
        nums = self.numbers[max_len]
        nums = self.remove_invalid_nums(nums=nums)
        num_ints = [int(num) for num in nums]
        num_ints = [num_int for num_int in num_ints if num_int >= low and num_int >= high]
        return num_ints

    def generate_numbers_low_high(self, low: int, high: int) -> List[int]:
        numbers_below_high = True
        len = 2
        while numbers_below_high:
            numbers_below_high = self.generate_numbers_of_len(len=len, high=high)
            len += 1

class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        pass


class TestStrobogrammaticNumbers(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.high = 10 ** 10

    def test_generate_from_number(self) -> None:
        generated_nums = StrobogrammaticNumbers.generate_from_number(num='', high=self.high)
        generated_nums_expected = ['00', '11', '88', '69', '96']
        self.assertEqual(generated_nums, generated_nums_expected)

    def test_generate_from_number_max_70(self) -> None:
        generated_nums = StrobogrammaticNumbers.generate_from_number(num='', high=70)
        generated_nums_expected = ['00', '11', '69']
        self.assertEqual(generated_nums, generated_nums_expected)

    def test_generate_numbers_of_len_2(self) -> None:
        strobo = StrobogrammaticNumbers()
        strobo.generate_numbers_of_len(len=2, high=self.high)
        numbers_expected = ['00', '11', '88', '69', '96']
        self.assertEqual(strobo.numbers[2], numbers_expected)
        numbers = strobo.get_all_numbers()
        numbers_expected = ['0', '1', '8', '00', '11', '88', '69', '96']
        self.assertEqual(numbers, numbers_expected)

    def test_generate_numbers_of_len_3(self) -> None:
        strobo = StrobogrammaticNumbers()
        strobo.generate_numbers_of_len(len=3, high=self.high)
        numbers_expected = ['000', '010', '080', '101', '111', '181', '609', '619',
                            '689', '808', '818', '888', '906', '916', '986']
        self.assertEqual(sorted(strobo.numbers[3]), numbers_expected)

    def test_generate_numbers_up_to_len_4(self) -> None:
        strobo = StrobogrammaticNumbers()
        _ = strobo.generate_numbers_up_to_len(max_len=4, low=0, high=self.high)