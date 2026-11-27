class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0 
        min_buy = float('inf')

        for i in prices:

            if i < min_buy:
                min_buy = i
            
            elif i>=min_buy:
                profit = i - min_buy
                max_profit+=profit
                min_buy = i

        
        return max_profit
         