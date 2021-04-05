def nthUglyNumber(n: int) -> int:
    # List of ugly numbers
    dp = [0] * n
    # Generate ugly numbers
    t2 = 0
    t3 = 0
    t5 = 0
    # First ugly number is 1
    dp[0] = 1
    for i in range(1, n):
        dp[i] = min(dp[t2] * 2, dp[t3] * 3, dp[t5] * 5)
        if dp[i] == dp[t2] * 2:
            t2 += 1
        if dp[i] == dp[t3] * 3:
            t3 += 1
        if dp[i] == dp[t5] * 5:
            t5 += 1
    breakpoint()
    return dp[-1]


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        return nthUglyNumber(n)


if __name__ == "__main__":
    xx = nthUglyNumber(470)
