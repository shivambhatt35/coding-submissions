class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        a_xor = 0

        for i in nums:

            a_xor = a_xor ^ i
        
        return a_xor