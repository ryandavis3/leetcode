from unittest import TestCase
from typing import List
from math import floor


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return get_peak_index_mountain_array(arr=arr)


def get_peak_index_mountain_array(arr: List[int]) -> int:
    L = len(arr)
    left = 0
    right = L - 1
    index = int(floor((right - left) / 2))
    while True:
        index_prev = index
        # Bisect left
        if arr[index] < arr[index - 1]:
            right = index
            index = index - int(floor((index - left) / 2))
        # Bisect right
        elif arr[index] < arr[index + 1]:
            left = index
            index = index + int(floor((right - index) / 2))
        # Found peak index
        else:
            return index
        # Raise exception if not index update
        if index == index_prev:
            raise ValueError('No index update!')


class TestPeak(TestCase):
    def test1(self) -> None:
        arr = [0, 2, 1, 0]
        peak_index = get_peak_index_mountain_array(arr=arr)
        self.assertEqual(peak_index, 1)

    def test2(self) -> None:
        arr = [0, 10, 5, 2]
        peak_index = get_peak_index_mountain_array(arr=arr)
        self.assertEqual(peak_index, 1)

    def test3(self) -> None:
        arr = [2, 5, 10, 0]
        peak_index = get_peak_index_mountain_array(arr=arr)
        self.assertEqual(peak_index, 2)

    def test4(self) -> None:
        arr = [1, 5, 4, 3, 2, 1]
        peak_index = get_peak_index_mountain_array(arr=arr)
        self.assertEqual(peak_index, 1)

    def test5(self) -> None:
        arr = [55, 59, 63, 99, 97, 94, 84, 81, 79, 66, 40, 38, 33, 23, 22, 21, 17, 9, 7]
        peak_index = get_peak_index_mountain_array(arr=arr)
        self.assertEqual(peak_index, 3)

    def test6(self) -> None:
        arr = [13, 25, 38, 55, 58, 75, 85, 88, 100, 94, 88, 82, 60, 58, 48, 43, 40, 35, 17, 2]
        peak_index = get_peak_index_mountain_array(arr=arr)
        self.assertEqual(peak_index, 8)
