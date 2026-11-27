class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        n = len(points)

        if n == k:
            return points
        
        res = []

        for i in points:

            distance = (math.sqrt((i[0] - 0)**2 + (i[1] - 0)**2))
            res.append([distance, i])
        
        heapq.heapify(res)
        
        final_res = []

        while  k > 0:
            list_ele = heapq.heappop(res)[1]
            final_res.append(list_ele)
            k-=1

        return final_res
