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

            # return self.solveUsingMemoization(n - 1, target, nums, dp)

            # return self.solveUsingTabulation(target, nums, n)

            return self.solveUsingSpaceOptimization(target, nums, n)

    
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


    # TC: O(n * k)
    # SC: O(n * k) 

    def solveUsingTabulation(self, target, nums, n):

        dp = [[False for _ in range(target + 1)] for _ in range(n)]

        # Base Case
        for ind in range(n):
            dp[ind][0] = True

        if nums[0] <= target:
            dp[0][nums[0]] = True

        for ind in range(n):
            for t in range(target + 1):
                # Not Pick
                notPick = dp[ind - 1][t]

                # Pick
                pick = 0
                if nums[ind] <= t:
                    pick = dp[ind - 1][t - nums[ind]]

                dp[ind][t] = pick or notPick

        return dp[n - 1][target]

    # TC: O(n * k)
    # SC: O(k) 
    def solveUsingSpaceOptimization(self, target, nums, n):
        
        prev = [False for _ in range(target + 1)]
        prev[0] = True  # When target = 0

        # Base Case
        if nums[0] <= target:
            prev[nums[0]] = True

        for ind in range(1, n):
            curr = [False for _ in range(target + 1)]
            curr[0] = True 
            
            for t in range(1, target + 1):
                # Not Pick
                notPick = prev[t]

                # Pick
                pick = 0
                if nums[ind] <= t:
                    pick = prev[t - nums[ind]]

                curr[t] = pick or notPick

            prev = curr

        return prev[target]


