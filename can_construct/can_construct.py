from collections import Counter

# https://leetcode.com/problems/ransom-note/

def canConstruct(ransomNote: str, magazine: str):
    """
    Return True (False) if we can(not) construct the ransom 
    note from the magazine letters .
    """
    # Counter of available letters
    C = Counter(magazine)
    # Iterate through each character in ransom note
    for char in ransomNote:
        # Letter not available -> return False
        if char not in C:
            return False
        # Decrement count of letter
        C[char] -= 1
        # If no more of letter left, remove from counter
        if C[char] == 0:
            del C[char]
    # Made it all the way through note, return True
    return True

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return canConstruct(ransomNote, magazine)
