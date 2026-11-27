import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-x for x in stones]

        heap = heapq.heapify(stones)

        while len(stones) > 1:

            largest = -heapq.heappop(stones)
            second_largest = -heapq.heappop(stones)

            if largest!=second_largest:
                diff = largest - second_largest
                heapq.heappush(stones, -diff)

        
        if stones:
            return -stones[0]
        
        return 0