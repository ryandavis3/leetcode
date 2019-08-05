# https://leetcode.com/problems/distinct-subsequences/

def numDistinct(s: str, t: str) -> int:
    """
    Count the number of distinct subsequences in s which
    equals t. 
    
    Use dynamic programming. 
    
    Build table where axes represent letters and substrings in 
    s, t. Table entry gives number of distinct subsequences of 
    substring of s that equals substring of t.

    Recurrence relation: If s[j] = t[i], T[i][j] equals the number 
    of distinct subsequences without using s[j] (T[i][j-1]) plus
    the number of distinct subsequences of using s[j] (T[i-1][j-1]).
    """
    # At least one string not given 
    if not s or not t:
        return 0
    # Lengths of strings
    Ls = len(s)
    Lt = len(t)
    # Empty table
    T = []
    for i in range(Lt):
        T += [[0] * Ls]
    # First line of table.
    for j in range(Ls):
        # Carry forward count in case we do not use letter
        if j > 0:
            T[0][j] += T[0][j-1]
        # Found letter
        if s[j] == t[0]:
            T[0][j] += 1
    # Second and following lines
    for i in range(1, Lt):
        for j in range(Ls):
            if j > 0:
                # Do not include letter
                T[i][j] += T[i][j-1]
                # Include letter (if present)
                if s[j] == t[i]:
                    T[i][j] += T[i-1][j-1] 
    return T[-1][-1]

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return numDistinct(s, t)
