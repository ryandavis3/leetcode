from typing import List

# https://leetcode.com/problems/longest-palindromic-substring/

def getStartPalindromes(s: str) -> str:
    """
    Get "start" palindromes of length 2 and 3.
    """
    L = len(s)
    # Length 3 strings
    idx3 = []
    for i in range(1, L-1):
        if s[i-1] == s[i+1]:
            idx3 += [i]
    # Length 2 strings
    idx2 = []
    for i in range(1, L):
        if s[i-1] == s[i]:
            idx2 += [i]
    # Represent palindromes by start and end indices
    # in original string
    sub3 = [tuple([c-1, c+1]) for c in idx3]
    sub2 = [tuple([c-1, c]) for c in idx2]
    substrs = sub2 + sub3
    return substrs

def extendPalindrome(substr: tuple, s: str) -> tuple:
    """
    Try to extend palindrome by one character on each side.
    If we are able to extend, return the new, longer 
    palindrome. If not, return None.
    """
    left = substr[0]-1
    right = substr[1]+1
    if left < 0:
        return None
    if right >= len(s):
        return None
    if s[left] == s[right]:
        return tuple([left, right])
    return None

def findPalindromes(substrs: List[tuple], s: str) -> List[tuple]:
    """
    Find indices of all palindromes in string by recursively 
    extending known palindromes one character at a time.
    """
    # List of palindromes that cannot be extended further
    completed = []
    while substrs:
        substrs_ex = []
        # Try to extend each palindrome
        for substr in substrs:
            substr_extend = extendPalindrome(substr, s)
            if not substr_extend:
                completed += [substr]
            else:
                substrs_ex += [substr_extend]
        substrs = substrs_ex
    return completed

def longestPalindrome(s: str) -> str:
    """
    Find longest palindrome in string.
    """
    if not s:
        return ""
    if len(s) == 1:
        return s
    substrs = getStartPalindromes(s)
    if not substrs:
        return s[0]
    pds = findPalindromes(substrs, s)
    pd_idx = max(pds, key=lambda x : x[1] - x[0])
    pd_long = s[pd_idx[0]:pd_idx[1]+1]
    return pd_long

class Solution:
    def longestPalindrome(self, s: str) -> str:
        return longestPalindrome(s)
