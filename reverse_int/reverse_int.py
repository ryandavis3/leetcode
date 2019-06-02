# https://leetcode.com/problems/reverse-integer/

# Define min and max integers we can handle in 
# 32-bit signed integer range
MIN_INT = -2**31
MAX_INT = 2**31-1

def reverse(x: int) -> int:
    """
    Reverse digits of an integer.
    """
    # Convert integer to string
    x_str = str(x)
    # Check if negative
    if x_str[0] == "-":
        neg = True
        x_str = x_str[1:] 
    else:
        neg = False
    # Reverse digits and convert back to int
    x_str_rev = x_str[::-1]
    x_rev = int(x_str_rev)
    # Apply negative sign if original int was negative
    if neg:
        x_rev = - x_rev
    # Return zero if outside 32-bit range
    if x_rev < MIN_INT or x_rev > MAX_INT:
        return 0
    # Return reversed integer
    return x_rev

class Solution:
    def reverse(self, x: int) -> int:
        return reverse(x)
