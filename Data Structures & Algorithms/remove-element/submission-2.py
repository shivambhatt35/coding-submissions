class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        n = len(nums) 
        loc = 0       

        for i in range(0,n):

            if nums[i] != val:
                nums[loc] = nums[i]
                loc+=1
            
            else:
                continue

        return loc
        
    