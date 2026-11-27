class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        zero_pointer = 0
        two_pointer = n-1
        curr = 0

        while curr <= two_pointer:

            if nums[curr] == 0:
                nums[zero_pointer], nums[curr] = nums[curr], nums[zero_pointer]
                zero_pointer+=1
                curr+=1

            elif nums[curr] == 2:
                nums[two_pointer], nums[curr] = nums[curr], nums[two_pointer]
                two_pointer-=1
            
            else:
                curr+=1
        