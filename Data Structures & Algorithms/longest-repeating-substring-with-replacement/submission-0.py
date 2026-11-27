class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        hash_map = defaultdict(int)
        max_count = 0
        left = 0

        for right in range(0, len(s)):

            hash_map[s[right]] =  hash_map[s[right]] + 1

            while (right-left+1) - max(hash_map.values()) > k:
                hash_map[s[left]]-=1
                left+=1
            
            max_count = max(max_count, right-left+1)
        
        return max_count
        