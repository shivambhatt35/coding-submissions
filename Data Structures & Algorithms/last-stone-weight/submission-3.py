class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-x for x in stones]
        
        # Heapify ONCE before the loop - O(N)
        heapq.heapify(stones)

        # Process until 0 or 1 stone remains
        while len(stones) > 1:
            largest = -heapq.heappop(stones)
            second_largest = -heapq.heappop(stones)

            if largest != second_largest:
                diff = largest - second_largest
                heapq.heappush(stones, -diff)

        # Return the remaining stone's weight, or 0 if no stones remain
        return -stones[0] if stones else 0
        