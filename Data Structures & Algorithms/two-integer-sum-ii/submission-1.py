class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n = len(numbers)
        start, end = 0, n-1

        while start < end:
            
            arr_sum = numbers[start] + numbers[end]

            if arr_sum == target:
                return [start+1, end+1]
            
            elif arr_sum > target:
                end-=1
            
            else:
                start+=1
        
        return []

