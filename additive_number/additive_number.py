from math import ceil
from typing import List

# https://leetcode.com/problems/additive-number/

def isAdditiveNumber(num: str) -> bool:
    
    L = len(num)
    l1 = 1
    # First number
    while l1 <= int(ceil(L/2)):
        n1 = int(num[:l1])
        l2 = 1
        # Second number
        while l1 + l2 < L:
            n2 = int(num[l1 : l1+l2])
            l3 = max(l1, l2)
            # Third number
            while l1 + l2 + l3 <= L:
                n3 = int(num[l1+l2 : l1+l2+l3])
                # Recursively check smaller string
                if n1 + n2 == n3:
                    if additive2(n2, n3, num[l1+l2+l3:]):
                        return True
                l3 += 1
            l2 += 1
        l1 += 1
    return False

def additive(prev: int, num: str) -> bool:

    # Completed number!
    if not num:
        return True
    
    L = len(num)
    l1 = 1
    # Length of second number
    while l1 <= int(ceil(L/2)):
        prev_next = int(num[:l1])
        l2 = l1 + 1
        # Length of third number (sum)
        while l2 <= L:
            _sum = int(num[l1:l2])
            if prev_next == _sum:
                if additive(prev_next, num[l1:]):
                    pass

def additive2(n1: int, n2: int, num: str) -> bool:
    
    print('n1: %s' % n1)
    print('n2: %s' % n2)
    print('num: %s' % num)
    
    # Completed number!
    if not num:
        return True

    L = len(num)
    l = 1
    while l <= L:
        n3 = int(num[:l])
        if n1 + n2 == n3:
            if additive2(n2, n3, num[l:]):
                return True
        l += 1
    return False


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        pass
