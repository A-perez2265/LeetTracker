# Last updated: 8/28/2025, 5:25:41 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0 , 1
        maxp = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxp = max(maxp,profit)
            else:
                l = r
            r +=1 
        return maxp

        