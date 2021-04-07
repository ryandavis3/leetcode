from typing import Set

def maxUniqueSplit(s: str) -> int:
    
    def backtrack(string: str, substrings: Set) -> Set:
        if string == "":
            return substrings
        i = 1
        while string[:i] not in substrings:
            i += 1
            if i > len(string):
                return False
        return backtrack(string[i:], substrings + {string[:i]}


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        pass
