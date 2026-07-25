class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_max = 0
        buy_minimum = prices[0]

        for selling in prices:
            profit_max = max(profit_max, selling-buy_minimum)
            buy_minimum = min(buy_minimum, selling)

        return profit_max