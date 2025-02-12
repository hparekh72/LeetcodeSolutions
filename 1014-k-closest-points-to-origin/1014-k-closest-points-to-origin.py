# Brute Force: Sorting
# TC: O(nlogn)
# SC: O(1)

# Better: Using Min-Heap
# TC: O(n + klogn)
# SC: O(n)

# Optimal: Using Max-Heap
# TC: O(nlogk)
# SC: O(k)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for x, y in points:
            dist = -(x**2 + y**2)
            heapq.heappush(maxHeap, [dist, x, y]) # Max heap as we need the closest/smallest points in the end


            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        res = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])

        return res
