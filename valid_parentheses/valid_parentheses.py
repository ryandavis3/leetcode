OPEN = set(['(', '{', '['])
MATCH = {')':'(', '}':'{', ']':'['}

def isValid(s: str) -> bool:
    """
    Determine if a string has valid parentheses.
    """
    # Empty string returns True
    if not s:
        return True
    # L is a stack of open characters
    L = []
    for char in s:
        # L is empty, add first character
        if not L:
            L += char
        else:
            # Open character - add to stack
            if char in OPEN:
                L += char
            # Closed character
            else:
                # Return False if no open characters 
                # in stack
                if not L:
                    return False
                # Pop last open char from stack and 
                # see if it matches
                if MATCH[char] != L.pop():
                    return False
    # Unmatched open characters - return False
    if L:
        return False
    return True

class Solution:
    def isValid(self, s: str) -> bool:
        return isValid(s)
