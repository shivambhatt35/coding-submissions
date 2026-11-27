class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n

        prefix_pro, suffix_pro = 1, 1 
        
        for i in range(n):

            prefix[i] = prefix_pro
            prefix_pro *= nums[i]


        for i in range(n-1,-1,-1):
            suffix[i] = suffix_pro
            suffix_pro *= nums[i]

        res = []

        for i in range(n):

            product = prefix[i] * suffix[i]
            res.append(product)
        
        return res