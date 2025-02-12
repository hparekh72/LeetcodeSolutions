# Approach 1: Using sorting
# TC: O(nlogn)

# Approach 2: Using Min-Heap
# TC: O(nlogk)
# SC: O(k)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for num in nums:
            heapq.heappush(minHeap, num)

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return minHeap[0]





        
        