class Solution:
    def climbStairs(self, n: int) -> int:

        if n<=2:
            return n

        prev_cal = 1
        last_cal = 2 
        curr_sum = 0

        for i in range(3,n+1): 
            curr_sum = prev_cal + last_cal
            prev_cal = last_cal
            last_cal = curr_sum
        
        return curr_sum
            



