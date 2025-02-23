class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1 for _ in range(n + 1)]
        # return self.solveUsingMemoization(n, dp)
        # return self.solveUsingTabulation(n, dp)
        return self.solveUsingSpaceOptimization(n)


    
    # TC: O(n) 
    # SC: O(n) (dp array and recursion stack space)
    def solveUsingMemoization(self, n, dp):
        if n <= 1:
            return 1
        
        if dp[n] != -1:
            return dp[n]

        dp[n] = self.solveUsingMemoization(n - 1, dp) + self.solveUsingMemoization(n - 2, dp)
        return dp[n]

    # TC: O(n) 
    # SC: O(n) (dp array)
    def solveUsingTabulation(self, n, dp):
        dp[0], dp[1] = 1, 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    def solveUsingSpaceOptimization(self, n):
        prev2 = 1
        prev = 1
        
        curr = prev
        for i in range(2, n + 1):
            curr = prev + prev2
            prev2 = prev
            prev = curr

        return curr
            







