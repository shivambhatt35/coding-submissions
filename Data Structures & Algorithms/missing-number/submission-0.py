class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        sum = int((n*(n+1) ) / 2)
        
        curr_sum = 0 

        for i in nums:
            curr_sum+=i

        diff = sum - curr_sum

        if diff>0:
            return diff
        
        return 0