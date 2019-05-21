# https://leetcode.com/problems/rotate-string/

def shiftString(s: str) -> str:
    """
    Move leftmost character in string to rightmost
    position.
    """
    return s[1:] + s[0]

def rotateString(A: str, B: str) -> bool:
    """
    Return True if we can make A become B after some 
    number of shifts, else return False.
    """
    if A == B:
        return True
    if len(A) != len(B):
        return False
    for _, _ in enumerate(A):
        A = shiftString(A)
        if A == B:
            return True
    return False

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return rotateString(A, B)
