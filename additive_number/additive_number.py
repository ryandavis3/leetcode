from math import ceil
from typing import List

# https://leetcode.com/problems/additive-number/

def isAdditiveNumber(num: str) -> bool:
    """
    Return True if number is additive, else return False. 
    Except for first two numbers, each subsequent number
    in the sequence should be the sum of the previous two.
    """
    if len(num) < 3:
        return False
    L = len(num)
    l1 = 1
    # First number
    while l1 <= int(ceil(L/2)):
        n1 = num[:l1]
        l2 = 1
        # Second number
        while l1 + l2 < L:
            n2 = num[l1 : l1+l2]
            l3 = max(l1, l2)
            # Third number
            while l1 + l2 + l3 <= L:
                n3 = num[l1+l2 : l1+l2+l3]
                # Recursively check smaller string
                if int(n1) + int(n2) == int(n3):
                    if search(n2, n3, num[l1+l2+l3:]):
                        return True
                l3 += 1
            l2 += 1
        l1 += 1
    return False

def search(n1: int, n2: int, num: str) -> bool:
    """
    Search for substring equaling sum of n1, n2. Use
    backtracking. Return True if num is an additive 
    string given n1, n2.
    """
    # Check for leading zeros
    if len(n1) > 1 and n1[0] == '0':
        return False
    if len(n2) > 1 and n2[0] == '0':
        return False
    # Completed number!
    if not num:
        return True
    # Find number (if it exists) equaling sum of n1, n2
    L = len(num)
    l = 1
    while l <= L:
        n3 = num[:l]
        if int(n1) + int(n2) == int(n3):
            if search(n2, n3, num[l:]):
                return True
        l += 1
    return False


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        return isAdditiveNumber(num)
