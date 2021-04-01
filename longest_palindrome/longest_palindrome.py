from collections import Counter

def longestPalindrome(s: str) -> str:
    """
    Find longest palindrome in string.

    Args:
        s (str)
    Returns:
        str
    """
    ct = Counter(s)
    even = 0
    odd = 0
    max_odd = 0
    # Iterate over items
    for _, count in ct.items():
        # If even, add to length of total
        if count % 2 == 0:
            even += count
        # Get longest odd numbered collection of characters
        else:
            odd += count - 1
            if count > max_odd:
                max_odd = count
    if odd == 0:
        total = even + (max_odd == 1)
    else:
        total = even + odd + 1
    return total

class Solution:
    def longestPalindrome(self, s: str) -> int:
        return longestPalindrome(s)
