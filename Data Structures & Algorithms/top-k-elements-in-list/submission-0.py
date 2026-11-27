class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_hashmap = defaultdict(int)

        for i in nums:

            freq_hashmap[i]+=1
        
        
        sorted_map = dict(sorted(freq_hashmap.items(), key = lambda item:item[1], reverse = True))

        result_list = []
        cnt = 0

        for i, v in sorted_map.items():
            cnt+=1
            result_list.append(i)

            if cnt == k:
                return result_list
            
            

            
        




        