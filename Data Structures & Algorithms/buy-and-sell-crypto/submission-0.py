class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        small_buy = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):

            if prices[i]< small_buy:
                small_buy = prices[i]
            
            profit = prices[i] - small_buy

            max_profit = max(max_profit, profit)
        
        return max_profit
        