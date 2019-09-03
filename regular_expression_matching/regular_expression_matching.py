# https://leetcode.com/problems/regular-expression-matching/

def isMatch(s: str, p: str):
    """
    Given an input string (s) and a pattern (p), implement regular
    expression matching with support for '.' and '*'.
    """
    # '.*' matches any string.
    if p == '.*':
        return True
    # Finished both string and pattern!
    if not s and not p:
        return True
    # Repeat character zero times
    if len(p) > 1:
        if not s and p[1] == '*':
            return isMatch(s, p[2:])
    # Finished one of string/pattern but not both.
    if not s or not p:
        return False
    # Pattern of length one 
    if len(p) == 1:
        if p[0] == s[0] or p[0] == '.':
            return isMatch(s[1:], p[1:])
        else:
            return False
    # Check if we have '*' character
    if p[1] == '*':
        # Zero of preceding character
        if p[0] != '.' and p[0] != s[0]:
            return isMatch(s, p[2:])
        # Characters (not '.') match!
        if p[0] == s[0]:
            if isMatch(s, p[2:]):
                return True
            while p[0] == s[0]:
                s = s[1:]
                if isMatch(s, p[2:]):
                    return True
                if not s:
                    return False
            return False
        # '.' characte matches any alphabetic character
        if p[0] == '.':
            if isMatch(s, p[2:]):
                return True
            while s and p:
                s = s[1:]
                if isMatch(s, p[2:]):
                    return True
            return False
    # If first character matches (or is '.'), recursively
    # check smaller pattern/string
    if p[0] == s[0] or p[0] == '.':
        return isMatch(s[1:], p[1:])
    return False

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return isMatch(s, p)
