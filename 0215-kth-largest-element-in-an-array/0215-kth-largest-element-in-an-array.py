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

        # Approach 3: QuickSelect Algorithm
        # TC: Worst-case: O(n^2)
            # Average-case O(n)

        # kthIndex = len(nums) - k

        # def quickSelect(l, r):
        #     pivot, p = nums[r], l
        #     for i in range(l, r):
        #         if nums[i] <= pivot:
        #             nums[p], nums[i] = nums[i], nums[p] # Swap
        #             p += 1
        #     nums[p], nums[r] = nums[r], nums[p] # Swap

        #     if p < kthIndex: 
        #         return quickSelect(p+1, r) # Right
        #     elif p > kthIndex:
        #         return quickSelect(l, p-1) # Left
        #     else: 
        #         return nums[p] # Answer

        # return quickSelect(0, len(nums) - 1)


        





