class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1 for _ in range(n + 1)]

        # return self.solveUsingRecursion(n, cost) # Start from "step n" (beyond the last step)
        # return self.solveUsingMemoization(n, cost, dp)
        # return self.solveUsingTabulation(n, cost)
        return self.solveUsingSpaceOptimized(n, cost)

    
    # TC: O(2^n)
    # SC: O(n) (recursion stack space)
    def solveUsingRecursion(self, ind, cost):
        if ind <= 1:
            return 0 # No cost required before step 0 or 1

        # Choose the cheaper step before reaching here
        return min(self.solveUsingRecursion(ind - 1, cost) + cost[ind - 1], self.solveUsingRecursion(ind - 2, cost) + cost[ind - 2])

    # TC: O(n)
    # SC: O(n) (recursion stack space and dp array)
    def solveUsingMemoization(self, ind, cost, dp):
        if ind <= 1:
            return 0 # No cost required before step 0 or 1

        if dp[ind] != -1:
            return dp[ind]

        # Choose the cheaper step before reaching here
        dp[ind] = min(self.solveUsingMemoization(ind - 1, cost, dp) + cost[ind - 1], self.solveUsingMemoization(ind - 2, cost, dp) + cost[ind - 2])
        return dp[ind]


    # TC: O(n)
    # SC: O(n) (dp array)
    def solveUsingTabulation(self, n, cost):
        dp = [0 for _ in range(n + 1)]
        # dp[0], dp[1] = 0, 0

        for ind in range(2, n + 1):
            dp[ind] = min(dp[ind - 1] + cost[ind - 1], dp[ind - 2] + cost[ind - 2])
        
        return dp[n]


    # TC: O(n)
    # SC: O(1) 
    def solveUsingSpaceOptimized(self, n, cost):
        prev1, prev2 = 0,0 

        curr = prev1
        for ind in range(2, n + 1):
            curr = min(prev1 + cost[ind - 1], prev2 + cost[ind - 2])
            prev2 = prev1
            prev1 = curr
        
        return curr
 



        





        

        
        

        