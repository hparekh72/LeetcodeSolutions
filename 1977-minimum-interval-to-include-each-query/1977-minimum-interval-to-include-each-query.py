# Brute Force:
# TC: O(nlogn) + O(n^2)
# SC: O(n) (required for result)

# class Solution:
#     def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
#         intervals.sort(key=lambda x : (x[1] - x[0] + 1))

#         res = []
#         for query in queries:
#             i = 0
#             while i < len(intervals):
#                 if query >= intervals[i][0] and query <= intervals[i][1]:
#                     res.append(intervals[i][1] - intervals[i][0] + 1)
#                     break

#                 i += 1
            
#             if i == len(intervals):
#                 res.append(-1)
        
#         return res



# Optimal:
# TC: O(nlogn) + (qlogq) + O(n+q)logn
# SC: O(n) + O(q) = O(n + q)

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        # Use a min-heap to manage overlapping intervals by their size and endpoint.
        minHeap = [] # SC: O(n)

        # Use a min-heap to manage overlapping intervals by their size and endpoint.
        res = {} # SC: O(q)

        i = 0

        # Process each query in ascending order to manage overlapping intervals efficiently.
        for q in sorted(queries):
            # Push intervals to the heap where the start is less than or equal to the query point.
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                # Push a tuple containing the size of the interval and its end point to the heap.
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1
            
            # Remove intervals from the heap that end before the current query point, as they are irrelevant.
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            # If the heap still contains any intervals, the smallest one is the best fit for this query.
            if minHeap:
                res[q] = minHeap[0][0]
            else:
                # If no intervals are left that can cover this query, return -1.
                res[q] = -1

        # Map the sorted results back to the order of the original queries.
        return [res[q] for q in queries]



            

        
        