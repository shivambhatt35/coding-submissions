class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        count = 1
        max_length = 1

        sorted_nums = sorted(nums)

        for i in range(1,len(sorted_nums)):

            if sorted_nums[i] == sorted_nums[i-1] + 1:
                count+=1
                max_length = max(max_length, count)
            
            elif sorted_nums[i] == sorted_nums[i-1]:
                continue
            else:
                count = 1
        
        return max_length



        