class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        cnt_zeros = 0

        for i in nums:
            if i == 0:
                cnt_zeros+=1

        
        if cnt_zeros == 0:
            
            product = 1
            for i in nums:
                product*=i
            result = []

            for i in nums:
                ele = int(product/i)
                result.append(ele)
            return result
        
        elif cnt_zeros == 1:
            product = 1
            for i in nums:
                if i!=0:
                    product*=i
                
            result = []

            for i in nums:
                if i!=0:
                    result.append(0)
                else:
                    result.append(product)
            return result
        
        else:
            result = []
            for i in nums:
                result.append(0)
            
            return result
