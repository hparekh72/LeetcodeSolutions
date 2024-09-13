class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)

        if totalSum % 2 == 1:
            return False
        else:
            n = len(nums)
            target = totalSum // 2
            # return self.solveUsingRecursion(n - 1, target, nums)

            dp = [[-1 for _ in range(target + 1)] for _ in range(n)]

            return self.solveUsingMemoization(n - 1, target, nums, dp)

    
    # Subset Sum Problem

    # TC: O(2^n)
    # SC: O(n) (recursive stack space)
    def solveUsingRecursion(self, ind, target, nums):
        # Base Case
        if ind == 0:
            return nums[0] == target

        if target == 0:
            return 1

        # Not Pick
        notPick = self.solveUsingRecursion(ind - 1, target, nums)

        # Pick
        pick = 0
        if nums[ind] <= target:
            pick = self.solveUsingRecursion(ind - 1, target - nums[ind], nums)

        return pick or notPick


    # TC: O(n * k)
    # SC: O(n * k) +  O(n) (recursive stack space)

    def solveUsingMemoization(self, ind, target, nums, dp):
        # Base Case
        if ind == 0:
            return nums[0] == target

        if target == 0:
            return 1

        if dp[ind][target] != -1:
            return dp[ind][target]

        # Not Pick
        notPick = self.solveUsingMemoization(ind - 1, target, nums, dp)

        # Pick
        pick = 0
        if nums[ind] <= target:
            pick = self.solveUsingMemoization(ind - 1, target - nums[ind], nums, dp)

        dp[ind][target] = pick or notPick
        return dp[ind][target]


 