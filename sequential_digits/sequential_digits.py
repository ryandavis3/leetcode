from typing import List

def sequentialDigits(low: int, high: int) -> List[int]:
    
    start = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    def backtrack(digits: List[str]) -> List[str]:
        if len(digits) == 0:
            return []
        found = []
        sub = []
        for digit in digits:
            if int(digit) >= low and int(digit) <= high:
                found += [digit]
            if int(digit[-1]) < 9 and int(digit) < high:
                sub += [str(digit) + str(int(digit[-1])+1)]
        return found+ backtrack(sub)

    return backtrack(start)


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        return sequentialDigits(low, high)


if __name__ == "__main__":
    low = 1000
    high = 13000
    result = sequentialDigits(low, high)
    print(result)
