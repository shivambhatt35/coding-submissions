class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        n = len(nums)
        start, end = 0, n-1

        if target <= nums[start]:
            return 0
        
        elif nums[end] < target:
            return n
        
        elif nums[end] == target:
            return n-1
        
        while start <= end:

            mid = (start+end)//2

            if nums[mid] >= target and nums[mid-1] < target:
                return mid
            
            elif nums[mid] <= target and nums[mid+1] > target:
                return mid+1
            
            elif nums[mid] > target:
                end = mid-1
            
            else:
                start = mid+1
        
        return 0