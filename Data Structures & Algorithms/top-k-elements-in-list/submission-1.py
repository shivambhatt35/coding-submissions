import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash_map = {}

        for i in nums:

            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1
        
        heap = []

        # index = number and value = frequency
        for index, value in hash_map.items():

            heapq.heappush(heap, [value, index])

            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []

        while heap:
            res.append(heapq.heappop(heap)[1])
        
        return res

