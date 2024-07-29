class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Approach 1: Using sorting
        # TC: O(nlogn)

        # Approach 2: Using Min-Heap
        # TC: O(nlogk)
        # SC: O(k)

        heap = []

        for i in range(len(nums)):
            if i < k:
                heapq.heappush(heap, nums[i])
            else:
                heapq.heappushpop(heap, nums[i])

        return heap[0]


        





