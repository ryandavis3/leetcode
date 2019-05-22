import math

# https://leetcode.com/problems/valid-palindrome-ii/

def isPalindrome(s: str) -> bool:
    """
    Determine if string is a palindrome.
    """
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

def oneDeleteEqual(s1: str, s2: str) -> bool:
    """
    Check if s1 and s2 can be made equal by 
    deleting one character. The length of s2 should
    be greater than the length of s1.
    """
    i = 0
    j = 0
    deletions = 0
    L1 = len(s1)
    L2 = len(s2)
    while i < L1 or j < L2:
        if s1[min(i, L1-1)] != s2[j]:
            deletions += 1
            j += 1
        else:
            i += 1
            j += 1
        if deletions > 1:
            return False
    return True

def validPalindrome(s: str) -> bool:
    """
    Check if we can make a string a palindrome by deleting
    at most one character.
    """
    # Check if string by itself is a palindrome
    if isPalindrome(s):
        return True
    L = len(s)
    if L == 2:
        return True
    mid = int(math.floor(L/2))
    # Even number of digits in original string; odd in new one
    if L % 2 == 0:
        s1 = s[:mid-1]
        s2 = s[mid:][::-1]
        is_eq1 = oneDeleteEqual(s1, s2)
        s1 = s[mid+1:]
        s2 = s[:mid][::-1]
        is_eq2 = oneDeleteEqual(s1, s2)
    # Odd number of digits in original string; even in new one
    else:
        s1 = s[:mid]
        s2 = s[mid:][::-1]
        is_eq1 = oneDeleteEqual(s1, s2)
        s1 = s[mid+1:][::-1]
        s2 = s[:mid+1]
        is_eq2 = oneDeleteEqual(s1, s2)
    is_eq = is_eq1 or is_eq2
    return is_eq

class Solution:
    def validPalindrome(self, s: str) -> bool:
        return validPalindrome(s)
