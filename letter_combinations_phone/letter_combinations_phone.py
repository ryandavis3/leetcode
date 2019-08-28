from typing import List

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

D = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno',
        7: 'pqrs', 8: 'tuv', 9: 'wxyz'}

def letterCombinations(digits: str) -> List[str]:
    """
    Given a string containing digits from 2-9 inclusive, return all
    possible letter combinations the number could represent. Use
    backtracking.
    """
    # No digits passed!
    if not digits:
        return []
    # Letters for first digit
    letters = [l for l in D[int(digits[0])]]
    # Only one digit!
    if len(digits) == 1:
        return letters
    # More than one digit; recursively get combinations
    next_letters = letterCombinations(digits[1:])
    comb = []
    for l in letters:
        for nl in next_letters:
            comb += [l + nl]
    return comb

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        return letterCombinations(digits)
