class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_map = defaultdict(list)

        for i in strs:

            key = ''.join(sorted(i))

            if key in hash_map:
                hash_map[key].append(i)
            else:
                hash_map[key] = [i]
            
        
        result = []

        for i, v in hash_map.items():

            result.append(v)
        
        return result
        