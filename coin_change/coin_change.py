from typing import List

def coinChange(coins: List[int], amount: int) -> int:
    # If amount is zero, we don't need any coins
    if amount == 0:
        return 0
    # Build shell for table
    table = []
    for i in range(len(coins)):
        table += [[-1] * amount]
    # Sort coins
    coins = sorted(coins)
    # Fill first row
    for j in range(1, amount+1):
        n = j / coins[0]
        table[0][j-1] = int(n) if n % 1 == 0 else -1
    # Fill subsequent rows
    for i in range(1, len(coins)):
        for j in range(0, amount):
            options = []
            # Use only the coin itself to make change
            if (j + 1) % coins[i] == 0:
                options += [int((j + 1) / coins[i])]
            # Make change using previous subset
            if table[i-1][j] >= 0:
                options += [table[i-1][j]]
            # Add coin amount to previous subset
            if j - coins[i] >= 0 and table[i-1][j-coins[i]] > 0:
                options += [table[i-1][j-coins[i]] + 1]
            # Add coin amount to current subset
            if j-coins[i] >= 0 and table[i][j-coins[i]] > 0:
                options += [table[i][j-coins[i]] + 1]
            if len(options) > 0:
                table[i][j] = min(options)
    return table[-1][-1]


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return coinChange(coins, amount)


if __name__ == "__main__":
    coins = [1,2,5] 
    amount = 11
    #result = coinChange(coins, amount)
    coins = [1, 2147483647]
    amount = 2
    #result = coinChange(coins, amount)
    coins = [1,2]
    amount = 2
    #result = coinChange(coins, amount)
    #print(result)
    coins = [1,2,5]
    amount = 10
    result = coinChange(coins, amount)
