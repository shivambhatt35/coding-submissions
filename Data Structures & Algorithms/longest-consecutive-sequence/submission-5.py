class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set()

        for a in nums:
            s.add(a)

        length = 1
        max_length = 0

        for num in nums:

            if num-1 in s:
                continue
            else:
                length = 1
                while (num+1) in s:
                    length+=1
                    num+=1
            
            max_length = max(max_length, length)
        
        return max_length

