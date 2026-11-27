import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        hashmap = {}

        for i in nums:

            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        
        res = []

        for item, value in hashmap.items():

            res.append([value, item])
        
        heapq.heapify(res)
        
        pop_ele = len(hashmap) - k

        while pop_ele > 0:

            heapq.heappop(res)
            pop_ele-=1
        
        ans = []

        while res:

            ans.append(heapq.heappop(res)[1])
        
        return ans