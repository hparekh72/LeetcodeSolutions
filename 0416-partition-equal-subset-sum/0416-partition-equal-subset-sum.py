# Subset Sum Problem

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = 0
        for num in nums:
            total += num

        if total % 2 == 1:
            return False
        else:
            n = len(nums)
            target = total // 2
            # return self.solveUsingRecursion(n - 1, target, nums)

            # dp = [[-1 for _ in range(target + 1)] for _ in range(n)]
            # return self.solveUsingMemoization(n - 1, target, nums, dp)

            return self.solveUsingTabulation(target, nums)
        
    def solveUsingRecursion(self, ind, target, nums):

        # Base Case
        if ind == 0:
            return nums[0] == target

        if target == 0:
            return True

        # Not Pick
        notPick = self.solveUsingRecursion(ind - 1, target, nums)

        pick = False
        if nums[ind] <= target:
            pick = self.solveUsingRecursion(ind - 1, target - nums[ind], nums)
        
        return pick or notPick


    # TC: O(n * target)
    # SC: O(n * target) + O(target) (recursion stack space)
    def solveUsingMemoization(self, ind, target, nums, dp):
        # Base Case
        if ind == 0:
            return nums[0] == target

        if target == 0:
            return True

        if dp[ind][target] != -1:
            return dp[ind][target]

        # Not Pick
        notPick = self.solveUsingMemoization(ind - 1, target, nums, dp)

        # Pick
        pick = False
        if nums[ind] <= target:
            pick = self.solveUsingMemoization(ind - 1, target - nums[ind], nums, dp)
        
        dp[ind][target] = pick or notPick
        return dp[ind][target]

    # TC: O(n * target)
    # SC: O(n * target) 
    def solveUsingTabulation(self, target, nums):
        n = len(nums)

        dp = [[False for _ in range(target + 1)] for _ in range(n)]

        # Base Case
        if nums[0] == target:
            dp[0][nums[0]] = True

        for ind in range(n):
            dp[ind][0] = True

        for ind in range(n):
            for num in range(target + 1):
                # Not Pick
                notPick = dp[ind - 1][num] 

                # Pick
                pick = False
                if nums[ind] <= num:
                    pick = dp[ind - 1][num - nums[ind]] 
                
                dp[ind][num] = pick or notPick
        return dp[n - 1][target]
        


        


