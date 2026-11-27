class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for i in range(0, len(nums)):

            required = target - nums[i]

            if required in hashmap:
                return [hashmap[required], i]
            
            hashmap[nums[i]] = i

        return []
        