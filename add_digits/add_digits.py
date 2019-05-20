# https://leetcode.com/problems/add-digits/

from collections import Counter
from typing import Dict

def intToDict(num: int) -> Dict:
    """
    Convert integer to dictionary. Keys are digits
    and values are numbers of time each digit appears.
    """
    num_arr = [int(digit) for digit in str(num)]
    ct = Counter(num_arr)
    return ct

def addDigitsCounter(ct: Dict) -> int:
    """
    Add digits in integer represented by 
    dictionary/counter.
    """
    _sum = 0
    for digit in ct:
        _sum += ct[digit] * digit
    return _sum

def addDigits(num: int) -> int:
    """
    Repeatedly add digits until the result has only 
    one digit.
    """
    ct = intToDict(num)
    _sum = addDigitsCounter(ct)
    while _sum >= 10:
        ct = intToDict(_sum)
        _sum = addDigitsCounter(ct)
    return _sum

class Solution:
    def addDigits(self, num: int) -> int:
        return addDigits(num)
