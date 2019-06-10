from typing import List
from collections import Counter

def moveLeft(s: str, left: int, T: Counter, Ts: Counter) -> List:
    """
    Move left pointer to the right as far as possible while
    substring is valid.

    Args:
        s (str): Our full string.
        left (int): Pointer to left end of substring
        T (Counter): Counter representing target string t
        Ts (Counter): Counter representing our substring

    Returns
        * left -> New left pointer
        * Ts -> New substring Counter
    """
    while True:
        char_l = s[left]
        if char_l in T:
            # Moving pointer further would make an invalid
            # substring
            if Ts[char_l] == T[char_l]:
                break
            else:
                Ts[char_l] -= 1
        left += 1
    return [left, Ts]

def minWindow(s: str, t: str) -> str:
    """
    Find the minimum window in t which will contain all the characters
    in t in O(n) time.
    """
    # t larger than s
    if len(t) > len(s):
        return ""
    # At least one letter in t not available in s
    if set(t) - set(s):
        return ""
    # At least one letter in t has a higher count
    # than in s
    Cs = Counter(s)
    Ct = Counter(t)
    for char in Ct:
        if Ct[char] > Cs[char]:
            return ""
    # Set left, right pointers to zero
    left = 0
    right = 0
    # Use counter to represent letter counts
    T = Counter(t)
    # Remaining characters for first valid window
    R = T.copy()
    # Move right pointer to build first valid window
    while R:
        char = s[right]
        if char in R:
            R[char] -= 1
            if not R[char]:
                del R[char]
        right += 1
    # Counter for our substring
    Ts = Counter(s[left:right])
    # Move left pointer
    [left, Ts] = moveLeft(s, left, T, Ts)
    # Initial minimum window, best left and right pointers
    min_window = right - 1 - left
    min_win_s = s[left:right]
    # Move right pointer in t
    while right < len(s):
        char_r = s[right]
        # Letter in t found; move pointer left in s while 
        # still having all characters in t.
        if char_r in T:
            Ts[char_r] += 1
            [left, Ts] = moveLeft(s, left, T, Ts)
            # Update minimum window substring
            if right - left < min_window:
                min_window = right - left
                min_win_s = s[left:right+1]
        right += 1
    return min_win_s


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        return minWindow(s, t)
