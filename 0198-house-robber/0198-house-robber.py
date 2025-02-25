class Solution:
    def rob(self, nums: List[int]) -> int: # Recursion
        n = len(nums)

        dp = [-1 for _ in range(n)]

        # return self.solveUsingRecursion(n - 1, nums)
        # return self.solveUsingMemoization(n - 1, nums, dp)
        return self.solveUsingTabulation(nums)

    def solveUsingRecursion(self, ind, nums):
        if ind == 0:
            return nums[ind]

        if ind < 0:
            return 0

        # pick 
        pick = nums[ind] + self.solveUsingRecursion(ind - 2, nums)
        # not pick
        notPick = 0 + self.solveUsingRecursion(ind - 1, nums)

        return max(pick, notPick)

    
    # TC: O(n)
    # SC: O(n) (recursion stack space and dp)
    def solveUsingMemoization(self, ind, nums, dp):
        if ind == 0:
            return nums[ind]
        
        if ind < 0:
            return 0

        if dp[ind] != -1:
            return dp[ind]

        # pick
        pick = nums[ind] + self.solveUsingMemoization(ind - 2, nums, dp)

        # not pick
        notPick = 0 + self.solveUsingMemoization(ind - 1, nums, dp)

        dp[ind] = max(pick, notPick)
        return dp[ind]


    # TC: O(n)
    # SC: O(n) (dp)
    def solveUsingTabulation(self, nums):
        n = len(nums)
        dp = [0 for _ in range(n)]

        dp[0] = nums[0]
        for ind in range(1, n):
            pick = nums[ind]
            if ind > 1:
                pick += dp[ind - 2]
            notPick = 0 + dp[ind - 1]
            dp[ind] = max(pick, notPick)

        return dp[n - 1]

        


        
        


        
        



        