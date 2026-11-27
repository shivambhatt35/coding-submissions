class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left_buy = 9999999 
        profit, max_profit = 0, 0

        for i in range(0,len(prices)):

            if left_buy > prices[i]:
                left_buy = prices[i]
            else:
                profit = prices[i] - left_buy
                max_profit = max(max_profit, profit)   

        return max_profit     