class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}

        for index, value in enumerate(nums):

            value_check = target - value

            if value_check in hash_map:
                return [hash_map[value_check], index]
            
            hash_map[value] = index
        
        return []
        