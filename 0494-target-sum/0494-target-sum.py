class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # return self.solveUsingRecursion(n - 1, target, nums)

        # dp = defaultdict(int)
        # return self.solveUsingMemoization(n - 1, target, nums, dp)

        return self.countPartitions(n, target, nums)



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

    # Approach 2: Divide them into two subsets such that the difference betweem those subsets are target
    def countPartitions(self, n, d, arr):
        # code here
        
        # s1 + s2 = totalSum
        # s1 - s2 = d 
        # totalSum - s2 - s2 = d
        # -2s2 + totalSum = d
        # (totalSum - d) // 2 = s2
        
        totalSum = sum(arr)
        
        if (totalSum - d) < 0 or (totalSum - d) % 2 == 1:
            return 0
        
        target = (totalSum - d) // 2
        
        dp = [[-1 for _ in range(target + 1)] for _ in range(n)]
        
        # return self.solveUsingMemoization(n - 1, target, arr, dp)
        
        return self.solveUsingTabulation(target, arr, n)
        
        # return self.solveUsingSpaceOptimization(target, arr, n)

    # def solveUsingMemoization(self, ind, target, arr, dp):
    #     mod = 10**9 + 7
        
    #     # Base Case
    #     if ind == 0:
    #         if arr[0] == 0 and target == 0:
    #             return 2
    #         if arr[0] == target or target == 0:
    #             return 1
    #         return 0
            
            
    #     if dp[ind][target] != -1:
    #         return dp[ind][target]
        
    #     # Not Pick 
    #     notPick = self.solveUsingMemoization(ind - 1, target, arr, dp)
        
    #     # Pick
    #     pick = 0
    #     if arr[ind] <= target:
    #         pick = self.solveUsingMemoization(ind - 1, target - arr[ind], arr, dp)
            
    #     dp[ind][target] = (pick + notPick) % mod
        
    #     return dp[ind][target] 
    
    
    # TC: O(n * k) 
    # SC: O(n * k)
    def solveUsingTabulation(self, target, arr, n):
        mod = 10**9 + 7
        
        dp = [[0 for _ in range(target + 1)] for _ in range(n)]
        
        if arr[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1
            
        if arr[0] != 0 and arr[0] <= target:
            dp[0][arr[0]] = 1
            
        for ind in range(1, n):
            for t in range(target + 1):
                
                # Not Pick 
                notPick = dp[ind - 1][t] 
                
                # Pick
                pick = 0
                if arr[ind] <= t:
                    pick = dp[ind - 1][t - arr[ind]] 
                    
                dp[ind][t] = (pick + notPick) % mod
                
        return dp[n - 1][target]


    # TC: O(n * k) 
    # SC: O(k) 
    def solveUsingSpaceOptimization(self, target, arr, n):
        mod = 10**9 + 7
        
        prev = [0] * (target + 1)
        
        if arr[0] == 0:
            prev[0] = 2
        else:
            prev[0] = 1
            
        if arr[0] != 0 and arr[0] <= target:
            prev[arr[0]] = 1
            
        for ind in range(1, n):
            curr = [0] * (target + 1)
            for t in range(target + 1):
                # Not Pick 
                notPick = prev[t] 
                
                # Pick
                pick = 0
                if arr[ind] <= t:
                    pick = prev[t - arr[ind]] 
                    
                curr[t] = (pick + notPick) % mod
            
            prev = [num for num in curr]
                
        return prev[target]





  

    
        