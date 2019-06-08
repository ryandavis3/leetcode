# https://leetcode.com/problems/wildcard-matching

def buildGrid(s: str, p: str):
    """
    Build dynamic programming grid / table to solve wildcard
    matching.
    """
    # Add null character to beginning of each of the strings.
    s = '#' + s
    p = '#' + p
    # Length of both strings.
    Ls = len(s)
    Lp = len(p)
    # Initialize grid with all zeros.
    G = []
    for i in range(Lp):
        G += [[0] * Ls]
    # Fill in first row (vs null string)
    G[0][0] = 1
    for j in range(1, Ls):
        if s[j] == '#':
            G[0][j] = G[0][j-1]
    # Fill in first column (vs null string)
    for i in range(1, Lp):
        if p[i] in set(['#', '*']):
            G[i][0] = G[i-1][0]
    # Fill in subsequent rows
    for i in range(1, Lp):
        for j in range(1, Ls):
            # If s char matches p char (or p char is ?), 
            # match will be the same as for case where both
            # strings omit last letter.
            if s[j] == p[i] or p[i] == '?':
                G[i][j] = G[i-1][j-1]
            # For star character, see if we can match by adding
            # zero, one, or more than one characters.
            if p[i] == '*':
                G[i][j] = max([G[i][j-1], G[i-1][j-1], G[i-1][j]])
    return G

def isMatch(s: str, p: str) -> bool:
    """
    Check to see if string s matches wildcard pattern p.
    """
    G = buildGrid(s, p)
    return bool(G[-1][-1])


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return isMatch(s, p)
