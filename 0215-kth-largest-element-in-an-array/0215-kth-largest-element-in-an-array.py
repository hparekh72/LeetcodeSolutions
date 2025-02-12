# Approach 1: Using sorting
# TC: O(nlogn)
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         return nums[len(nums) - k]

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


# Approach 3: QuickSelect Algorithm
# TC: Worst-case: O(n^2)
# Average-case O(n) 
# SC: O(n) (Recursion Stack Space)
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:

#         kthIndex = len(nums) - k  # When array is sorted

#         def quickSelect(l, r):
#             pivot, p = nums[r], l # Choose the pivot as the last element

#             # Partitioning step
#             for i in range(l, r):
#                 if nums[i] <= pivot:  # Move smaller elements to the left
#                     nums[p], nums[i] = nums[i], nums[p]
#                     p += 1
            
#             # Place the pivot in its correct position
#             nums[p], nums[r] = nums[r], nums[p]

#             # Check the position of the pivot (partition index)
#             if p > kthIndex:   # If pivot is to the right of kthIndex
#                 return quickSelect(l, p - 1)
#             elif p < kthIndex:   # If pivot is to the left of kthIndex
#                 return quickSelect(p + 1, r)
#             else:
#                 return nums[p]

#         return quickSelect(0, len(nums) - 1)





            







                       
        


        
        