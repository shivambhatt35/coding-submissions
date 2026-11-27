import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dict_ = []

        for i in points:

            x = i[0]
            y = i[1]

            dist = math.sqrt( ((x - 0)**2) + ((y - 0)**2) )

            dict_.append([dist,[x,y]])
        
        heapq.heapify(dict_)
        result  = []

        while k > 0:

            list_ele = heapq.heappop(dict_)[1]
            result.append(list_ele)
            k-=1
        
        return result

            


