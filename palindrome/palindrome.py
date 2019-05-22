import re
import math

def isPalindrome(s: str) -> bool:
    """
    Determine if string is a palindrome using
    only alphanumeric characters and ignoring cases.
    """
    # All lower case
    s = s.lower()
    # Remove punctuation
    pattern = re.compile('([^\s\w]|_)+')
    s = pattern.sub('', s)
    # Remove spaces
    s = s.replace(' ', '')
    L = len(s)
    mid = int(math.floor(L/2))
    if L % 2 == 1: # Odd length
        if s[:mid] == s[mid+1:][::-1]:
            return True
        else:
            return False
    else: # Even length

        if s[:mid] == s[mid:][::-1]:
            return True
        else:
            return False

class Solution:
    def isPalindrome(self, s: str) -> bool:
        return isPalindrome(s)
