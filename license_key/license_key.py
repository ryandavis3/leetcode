import math

# https://leetcode.com/problems/license-key-formatting/

def format(S: str, K: int) -> str:
    """
    Format license key S so each group has exactly K
    characters, except for the first group, which can 
    be shorter than K.
    """
    # Convert to upper case
    S = S.upper()
    # Replace hyphens and get length
    S = S.replace('-', '')
    L = len(S)
    # Get segments between dashes in reverse order
    S_rev = S[::-1]
    segments = list()
    for i in range(int(math.ceil(L/K))):
        segments.append(S_rev[i * K : (i+1) * K][::-1])
    # Re-order segments and add dashes
    segments = segments[::-1]
    S_new = "-".join(segments)
    return S_new
    
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        return format(S, K)
