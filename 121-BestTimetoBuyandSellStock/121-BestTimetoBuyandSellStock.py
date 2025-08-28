# Last updated: 8/27/2025, 10:08:52 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        max_profit= 0

        for i in range(1,len(prices)):
            profit = prices[i] - lowest_price

            max_profit = max(max_profit, profit)

            lowest_price = min(lowest_price, prices[i])
        return max_profit
        