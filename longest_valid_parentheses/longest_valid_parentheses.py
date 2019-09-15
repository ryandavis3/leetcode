# https://leetcode.com/problems/longest-valid-parentheses/

def reverseStr(s: str) -> str:
    """
    Reverse string of parentheses.
    """
    # Replace parentheses with tokens
    d1 = {'(': 'a', ')': 'b'}
    for key, val in d1.items():
        s = s.replace(key, val)
    # Replace tokens with opposite parentheses
    d2 = {'a': ')', 'b': '('}
    for key, val in d2.items():
        s = s.replace(key, val)
    return s[::-1]

def longest(s: str) -> str:
    """
    Given a string containing just the characters '(' and ')'
    find the longest valid (well-formed) parentheses substring.
    """
    # No string passed!
    if not s:
        return ""
    # Length one string passed!
    if len(s) == 1:
        return ""
    # Initial max length string is empty string
    max_len = 0 
    max_str = ""
    L = len(s)
    # Iterate across possible starts
    for i in range(1):
        if L - i < max_len:
            break
        start = i
        left = 0
        # Iterate across possible ends
        for j, char in enumerate(s):
            if L - start < max_len:
                break
            # String index before start
            if j < i:
                continue
            # First character in string
            elif j == i:
                if char == '(':
                    left += 1
                elif char == ')':
                    start += 1
                continue
            # Open parenthesis
            if char == '(':
                left += 1
            # Closed parenthesis
            elif char == ')':
                # Add to substring
                if left == 1:
                    left -= 1
                    # New longest substring!
                    if j - start > max_len:
                        max_len = j - start
                        max_str = s[start:j+1]
                elif left > 1:
                    left -= 1
                # No matching open parenthesis; start over!
                else:
                    left = 0
                    start = j+1
    return max_str

def longestValidParentheses(s: str) -> int:
    """
    Get length of substring with longest valid parentheses.
    """
    # Get max substring of string (and reversed string)
    max_str = longest(s)
    max_str_rev = longest(reverseStr(s))
    # Return lenth of longer string
    if len(max_str) > len(max_Str_rev):
        return max_str
    else:
        return max_str_rev

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_str = longestValidParentheses(s)
        return len(max_str)
