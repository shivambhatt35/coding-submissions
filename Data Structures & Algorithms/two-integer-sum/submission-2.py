class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}
        result = []

        for i,v in enumerate(nums):

            remaining = target - v

            if remaining in hash_map:
                return [hash_map[remaining],i]
            
            hash_map[v] = i
            
        