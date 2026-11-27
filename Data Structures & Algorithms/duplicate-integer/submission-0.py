class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hash_map = {}

        for i in nums:

            if i in hash_map:
                hash_map[i] += 1
            else:
                 hash_map[i] = 1

        bool = False

        for i, v in hash_map.items():

            if v>1:
                return True

        return False      