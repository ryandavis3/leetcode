# https://leetcode.com/problems/zigzag-conversion/

def convert(s: str, numRows: int) -> str:
    """
    Convert string to a "zigzag" pattern on a given
    number of rows.
    """
    # Easy cases of missing string, length one string,
    # only one row.
    if not s:
        return ""
    if len(s) == 1:
        return s
    if numRows == 1:
        return s
    # Initialize dictionaries for substrings on
    # each row of zigzag pattern
    D = {}
    for i in range(numRows):
        D[i] = ""
    # Assign each character to a row. Zigzag pattern repeats
    # every M = 2 * (numRows-1) characters, so we can use
    # a modular approach.
    M = 2 * (numRows-1)
    for i, char in enumerate(s):
        mod = i % M
        if mod <= numRows-1: # "Down" the zigzag
            row = mod
        else: # "Up" the zigzag
            row = M - mod
        D[row] += char
    # Concatenate rows to make full "zigzag" string
    s_z = ""
    for row in D:
        s_z += D[row]
    return s_z

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        return convert(s, numRows)
