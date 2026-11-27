class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        word_dict = defaultdict(list)

        for i in strs:
            
            key = ''.join(sorted(i))

            if key in word_dict:
                word_dict[key].append(i)
            else:
                word_dict[key] = [i]
            
        return list(word_dict.values())
        