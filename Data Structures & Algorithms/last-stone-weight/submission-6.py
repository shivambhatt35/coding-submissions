import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:

            max_ele = -heapq.heappop(stones)
            second_max = -heapq.heappop(stones)

            if max_ele > second_max:
                target = max_ele - second_max
                heapq.heappush(stones, -target)
        
        if len(stones) > 0:
            return -stones[0]

        return 0
        