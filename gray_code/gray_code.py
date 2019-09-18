from typing import List

def grayCodeBinary(n: int) -> List[int]:
    """
    Generate sequence of (binary) gray codes for non-negative
    integer n representing the total number of bits in a 
    gray code. Two succcessive values differ by only one
    bit. Use backtracking.
    """
    # Zero bits!
    if not n:
        return ['0']
    # One bit case -> either 0 or 1
    if n == 1:
        return ['0', '1']
    # Get binary codes with one less bit 
    lower = grayCodeBinary(n-1)
    codes = []
    zero = True
    # Add bit to binary codes
    for low in lower:
        # Alternate using 0 or 1 first
        if zero:
            x = '0'
            y = '1'
        else:
            x = '1'
            y = '0'
        code = low + x
        codes += [code]
        code = low + y
        codes += [code]
        zero = not zero
    return codes

def grayCode(n: int) -> List[int]:
    """
    Generate integer gray codes.
    """
    codes = grayCodeBinary(n)
    nums = [int(c, 2) for c in codes]
    return nums

class Solution:
    def grayCode(self, n: int) -> List[int]:
        return grayCode(n)
