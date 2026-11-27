class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        n = len(s)
        m = len(t)

        if n!=m:
            return False
        
        hash_map1 = {}
        hash_map2 = {}

        for i in range(n):

            if s[i] in hash_map1:
                hash_map1[s[i]] += 1
            
            if t[i] in hash_map2:   
                hash_map2[t[i]] += 1

            if s[i] not in hash_map1:
                hash_map1[s[i]] = 1
            
            if t[i] not in hash_map2:
                hash_map2[t[i]] = 1
        
        return hash_map1==hash_map2
        