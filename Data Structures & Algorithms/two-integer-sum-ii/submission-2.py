class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        first, last = 0, len(numbers)-1

        while first<last:

            sum = numbers[first]+numbers[last]

            if sum == target:
                return [first+1,last+1]
            
            elif sum<target:
                first+=1
            
            else:
                last-=1
        
        return []
        