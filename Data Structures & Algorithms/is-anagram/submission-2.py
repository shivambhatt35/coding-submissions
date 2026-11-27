class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hash_map = {} 

        for i in s:

            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1
        
        for i in t:

            if i not in hash_map:
                return False
            
            elif hash_map[i] <= 0:
                return False
            
            else:
                hash_map[i]-=1

        for i, v in hash_map.items():
            if v > 0:
                return False
    
        return True

        