def checkPowersOfThree(n: int) -> bool:

    def backtrack(num: int, power: int) -> bool:
        # Found number!
        if num == n:
            return True
        # Too high!
        if num + 3 ** power > n:
            return False
        return max(backtrack(num + 3 ** power, power+1), backtrack(num, power+1))

    return backtrack(0, 0)

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        return checkPowersOfThree(n)

if __name__ == "__main__":
    n = 91
    result = checkPowersOfThree(n)
    print(result)
    n = 59052
    result = checkPowersOfThree(n)
    print(result)
