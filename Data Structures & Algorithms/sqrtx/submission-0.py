class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 0:
            return 0
        
        start, end = 1, x
        res = 0

        while start <= end:

            mid = (start+end)//2

            square = mid*mid

            if square == x:
                return mid
            
            elif square > x:
                end = mid-1

            else:
                start = mid+1
                res = mid

        return res      