# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(s: str) -> int:
    """
    Find the length of the longest substring without
    repeating characters.
    """
    # Cases where string is of length 0 or 1
    if not s:
        return 0
    elif len(s) == 1:
        return 1
    # Initialize start, end of string; max substring length
    # observed so far, dictionary representing positions of
    # keys in substring.
    start = 0
    end = 0
    max_len = 0
    D = {}
    # Iterate through each character in string
    for i, letter in enumerate(s):
        # If letter already in string, remove the letter and all 
        # letters that appear before it to make new substring 
        # without repeating characters.
        if letter in D:
            start = D[letter] + 1
            remove = []
            for key in D:
                if D[key] < start:
                    remove += [key]
            for key in remove:
                del D[key]
        # Add letter index to dictionary, increment end index
        D[letter] = i
        end += 1
        # Check if new string is longer than current longest. If so, 
        # update max length.
        if end - start > max_len:
            max_len = end - start
    return max_len

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return lengthOfLongestSubstring(s)
