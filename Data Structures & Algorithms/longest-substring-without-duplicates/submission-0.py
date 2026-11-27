class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # susbstring should be continueous

        set_arr = set()
        left = 0
        max_length = 0

        for right in range(0,len(s)):
            
            while s[right] in set_arr:
                set_arr.remove(s[left])
                left+=1
            set_arr.add(s[right])
            max_length = max(max_length, right-left+1)

        return max_length


            
