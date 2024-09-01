# Note: Refer the previous code (House Robber 1)

# Intution: Since the first house is the neighbor to the last one
# 1) Skip the last index house. So now the problem in similar to House Robber 1
# 2) Skip the first(0th-index) house. So now the problem in similar to House Robber 1
# 3) Take the maximum from both the approaches

 
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1: # Edge Case
            return nums[0]

        temp1, temp2 = [], []
        for i in range(n):     # TC: O(n), SC: O(n)
            if i != 0:
                temp1.append(nums[i]) # Skip the first index
            if i != n - 1:
                temp2.append(nums[i]) # Skip the last index

        return max(self.solveUsingSpaceOptimization(temp1), self.solveUsingSpaceOptimization(temp2))
    
    
    # TC: O(n)
    # SC: O(1)
    def solveUsingSpaceOptimization(self, nums):
        n = len(nums)

        prev = nums[0]
        prev2 = 0
        curr = 0

        for ind in range(1, n):
            
            # Pick (If we pick this element, then we will skip its next element as to avoid adjacents)
            pick = nums[ind]
            if ind > 1:
                pick += prev2

            # Not Pick
            notPick = 0 + prev

            curr = max(pick, notPick)

            # Set the variables for next iteration
            prev2 = prev
            prev = curr

        return prev # Note: Can also return curr here
        