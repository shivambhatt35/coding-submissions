class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        hash_map = defaultdict(int)

        for i in nums:
            hash_map[i]+=1
        

        n = len(nums)
        target = n//3
        result = []

        for i, v in hash_map.items():

            if v > target:
                result.append(i)
        

        return result
        