class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        # Brute Force: Sorting
        # TC: O(nlogn) + O(nlogn)

        # closest_sorted_arr = sorted(arr, key=lambda num: (abs(x - num), num))
        
        # return sorted(closest_sorted_arr[:k])

        # Optimal: Using Max-heap
        # TC: O(nlogk) + O(klogk)
        # SC: O(k)



        heap = []

        for i in range(len(arr)):
             # Max-heap
             # Negative key for reverse order on tie as default value to pop in a tie is lexicographically smaller
            heapq.heappush(heap, (-abs(arr[i] - x), -arr[i]))

            if len(heap) > k: 
                heapq.heappop(heap)

        res = []
        while heap:
            _, key = heapq.heappop(heap)
            key = -key
            res.append(key)

        return sorted(res)


        

            