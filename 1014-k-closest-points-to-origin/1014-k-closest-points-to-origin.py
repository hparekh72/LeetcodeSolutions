import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # TC: O(nlogk)
        # SC: O(k)

        heap = []
        res = []

        for point in points:
            total = 0
            for coordinate in point:
                total += pow(coordinate, 2)
            # total = math.sqrt(total) 
            print(total, point)
            # Max heap as we need the closest/smallest points in the end
            heapq.heappush(heap, (-total, point)) 

            if len(heap) > k:
                heapq.heappop(heap)

        for val, key in heap:
            res.append(key)

        return res


            

        