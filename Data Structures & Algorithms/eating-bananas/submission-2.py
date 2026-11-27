import math

class Solution:
    def time_check(self, k: int, piles:  List[int]):
        time = 0
        for i in piles:
            time += math.ceil(i/k)
        
        return time


    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 1, max(piles)
        min_time = 5000000001
        res = 5000000001

        while left<= right:
            
            mid = (left+right)//2

            time = self.time_check(mid, piles)

            if time<=h:
                min_time = min(min_time, time)
                res = min(res, mid)
                right = mid-1
            else:
                left = mid+1
        
        return res

