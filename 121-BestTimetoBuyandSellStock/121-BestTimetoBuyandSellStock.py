# Last updated: 8/27/2025, 10:27:15 PM
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

        