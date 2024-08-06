# Brute Force:
# TC: O(N^3)
# SC: O(1)

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         maxSum = float('-inf')
#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 total = 0
#                 for k in range(i, j+1):
#                     total += nums[k]
#                     maxSum = max(total, maxSum)
#         return maxSum
                    


# Better:
# TC: O(N^2)
# SC: O(1)

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         maxSum = float('-inf')
#         for i in range(len(nums)):
#             total = 0
#             for j in range(i, len(nums)):
#                 total += nums[j]
#                 maxSum = max(maxSum, total)

#         return maxSum

# Optimal: Kadane's Algorithm
# TC: O(N)
# SC: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        maxSum = float('-inf')
        for i in range(len(nums)):
            total += nums[i]

            if total > maxSum:
                maxSum = total

            if total < 0:
                total = 0
        
        return maxSum

# Follow-up: Print the maximum subarray numbers
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         total = 0
#         maxSum = float('-inf')
#         start, ansStartIndex, ansEndIndex = 0, 0, 0
#         for i in range(len(nums)):

#             if total == 0:
#                 start = i

#             total += nums[i]

#             if total > maxSum:
#                 maxSum = total
#                 ansStartIndex = start
#                 ansEndIndex = i

#             if total < 0:
#                 total = 0

#         for i in range(ansStartIndex, ansEndIndex +1)
#             print(nums[i])
        
#         return maxSum




            




        