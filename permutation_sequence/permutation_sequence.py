import math
from typing import Dict

# https://leetcode.com/problems/permutation-sequence/

def getFactorials(n: int) -> Dict:
    """
    Get factorials for values up to n.
    """
    F = {}
    k = 1
    prod = 1
    while k <= n:
        prod = prod*k
        F[k] = prod
        k += 1
    F[0] = 1
    return F

def listDigits(n: int) -> int:
    """
    List digits up to n.
    """
    digits = []
    for i in range(1, n+1):
        digits += [str(i)]
    return digits

def getDigit(digits: int, n: int, k: int, factorials: Dict) -> int:
    """
    Get digit corresponding to kth value in n! permutations.
    Use recursion.
    """
    # Edge cases: n = 1,2
    if n == 1:
        return str(digits[0])
    elif n == 2:
        i = k - 1
    # Get index of digit
    else:
        i = math.floor((k-1) / factorials[n-1])
    # Update k, n, digits
    k = k - factorials[n-1] * i
    n = n-1
    digit = digits.pop(i)
    # Add digit and recursively call on smaller sequence
    return digit + getDigit(digits, n, k, factorials)

def getPermutation(n: int, k: int) -> str:
    """
    Get kth permutation sequence of n! unique permutations.
    """
    digit = 0
    factorials = getFactorials(n)
    while digit < n:
        pass

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        digits = listDigits(n)
        factorials = getFactorials(n)
        return getDigit(digits, n, k, factorials)
