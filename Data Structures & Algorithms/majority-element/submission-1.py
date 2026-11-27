class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        sorted_nums = sorted(nums)

        n = len(nums)//2

        return sorted_nums[n]



        