class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        curr_ele = 1
        cnt = 1

        while curr_ele < len(nums):

            if nums[curr_ele] == nums[i]:
                curr_ele+=1
            
            else:
                i+=1
                nums[i] = nums[curr_ele]
                curr_ele+=1
                cnt +=1
        
        return cnt