class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # return self.solveUsingRecursion(n - 1, target, nums)

        dp = defaultdict(int)
        return self.solveUsingMemoization(n - 1, target, nums, dp)

    # TC: O(2^n)
    # SC: O(n) (recursion stack space)
    def solveUsingRecursion(self, ind, target, nums):
        # Base Case
        if ind == 0:
            if target + nums[0] == 0 or target - nums[0] == 0:
                return 1
            else:
                return 0

        # Add
        add = self.solveUsingRecursion(ind - 1, target + nums[ind], nums)

        # Subtract
        subtract = self.solveUsingRecursion(ind - 1, target - nums[ind], nums)

        return add + subtract

    # TC: O(n * target)
    # SC: O(n * target) + O(n) (recursion stack space)

    def solveUsingMemoization(self, ind, target, nums, dp):
        # Base Case
        if ind < 0:
            if target == 0:
                return 1
            else:
                return 0
                
        if (ind, target) in dp:
            return dp[(ind, target)]

        # Add
        add = self.solveUsingMemoization(ind - 1, target + nums[ind], nums, dp)

        # Subtract
        subtract = self.solveUsingMemoization(ind - 1, target - nums[ind], nums, dp)

        dp[(ind, target)] = add + subtract
        return dp[(ind, target)]



  

    
        