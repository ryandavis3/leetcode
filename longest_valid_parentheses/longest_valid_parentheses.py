# https://leetcode.com/problems/longest-valid-parentheses/

def longestValidParentheses(s: str) -> int:
    """
    Given a string containing just the characters '(' and ')'
    find the length of the longest valid (well-formed) 
    parentheses substring.
    """
    # No string passed!
    if not s:
        return None, ""
    # Length one string passed!
    if len(s) == 1:
        return None, ""
    # Table for open parentheses to left
    left = []
    L = len(s)
    for _ in range(L):
        left += [[0] * L]
    # Substrings
    substr = []
    for _ in range(L):
        substr += [[""] * L]
    max_len = 0 
    max_str = ""
    # Iterate across possible starts
    for i in range(L):
        if L - i < max_len:
            break
        start = i
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
                    left[i][j] += 1
                elif char == ')':
                    start += 1
                continue
            # Carry over left parentheses
            left[i][j] = left[i][j-1]
            # Open parenthesis
            if char == '(':
                left[i][j] += 1
            # Closed parenthesis
            elif char == ')':
                # Add to substring
                if left[i][j] == 1:
                    substr[i][j] = s[start:j+1]
                    left[i][j] -= 1
                    # New longest substring!
                    if j - start > max_len:
                        max_len = j - start
                        max_str = substr[i][j]
                elif left[i][j] > 1:
                    left[i][j] -= 1
                # No matching open parenthesis; start over!
                else:
                    left[i][j] = 0
                    start = j+1
    return substr, max_str

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        substr, max_str = longestValidParentheses(s)
        return len(max_str)
