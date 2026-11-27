class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        left_max = [0]*n
        right_max = [0]*n

        left_m, right_m = 0, 0
        for i in range(0, n):
            left_max[i] = left_m
            left_m = max(left_m, height[i])
        
        for i in range(n-1, -1,-1):
            right_max[i] = right_m
            right_m = max(right_m, height[i])

        area = 0
        for i in range(0, n):

           sum_ =  (min(left_max[i], right_max[i])) - height[i]

           if sum_ > 0:
            area+=sum_
        
        return area