from typing import List

# Use backtracking

def letterCasePermutation(S: str) -> List[str]:

    def backtrack(s: str) -> List[str]:
        # Last digit
        s0 = s[0]
        if s0.isalpha():
            strings = [s0.lower(), s0.upper()]
        else:
            strings = [s0]
        if len(s) == 1:
            return strings
        # More than one digit
        subsequent = backtrack(s[1:])
        results = []
        for string in strings:
            for sub in subsequent:
                results += [string + sub]
        return results

    return backtrack(S)


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        return letterCasePermutation(S)


if __name__ == "__main__":
    S = "a1b2"
    result = letterCasePermutation(S)
    print(result)
    S = "3z4"
    result = letterCasePermutation(S)
    print(result)
