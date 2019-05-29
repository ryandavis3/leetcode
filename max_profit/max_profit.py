from typing import List

def maxProfit(P: List[int]) -> int:
    # Set initial max profit and min buy price
    max_prof = 0
    min_buy_px = 10000
    # Iterate through prices
    for i, p in enumerate(P):
        # If price lower than current min buy price,
        # update min buy price.
        if p < min_buy_px:
            min_buy_px = p
        # Profit attainable by selling at price
        prof_i = p - min_buy_px
        # Update max profit
        if prof_i > max_prof:
            max_prof = prof_i
    return max_prof

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return maxProfit(prices)
