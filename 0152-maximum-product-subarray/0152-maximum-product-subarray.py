
# Brute Force: Generate all sub arrays and check max product
# TC: O(n^2)
# SC: O(1)
# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         maxProduct = nums[0]
#         for i in range(len(nums)):
#             curr = nums[i]
#             maxProduct = max(maxProduct, curr)
#             for j in range(i + 1, len(nums)):
#                 curr *= nums[j]
#                 maxProduct = max(maxProduct, curr)

#         return maxProduct

# Optimal: Kadane's Algorithm
# TC: O(n)
# SC: O(1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin, currMax = 1, 1

        for num in nums:
            if num == 0:
                currMin, currMax = 1, 1
                continue
            temp = num * currMax
            currMax = max(num * currMax, num * currMin, num) # eg. [-1, 8]
            currMin = min(temp, num * currMin, num) # eg. [-1, -8]
            res = max(res, currMax, currMin)

        return res

            
            


                
        