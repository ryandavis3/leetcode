from collections import Counter

# https://leetcode.com/problems/custom-sort-string/

def customSortString(S: str, T: str) -> str:
    """
    S and T are composed of lowercase letters. In S, no letter 
    occurs more than once.

    S was sorted in some order previously. Permute the characters
    of T so they match the order that S was sorted. If char x occurs
    before char y in S, then x should occur before y in the returned 
    string. 
    """
    # Common characters 
    common = set(S) & set(T)
    T_common = [char for char in T if char in common]
    T_common_count = Counter(T_common)
    # Characters in T but not S
    T_only = set(T) - set(S)
    T_only_chars = [char for char in T if char in T_only]
    T_only_count = Counter(T_only_chars)
    # Build sorted string with common characters
    T_sorted = ""
    for char in S:
        if char in common:
            T_sorted += char * T_common_count[char]
    # Add characters in T but not S
    for char in T_only:
        T_sorted += char * T_only_count[char]
    return T_sorted


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        return customSortString(S, T)
