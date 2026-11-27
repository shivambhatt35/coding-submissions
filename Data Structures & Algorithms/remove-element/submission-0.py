class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        loc = 0

        for i in range(0, len(nums)):

            if nums[i]!=val:
                nums[loc] = nums[i]
                loc+=1
        
        return loc