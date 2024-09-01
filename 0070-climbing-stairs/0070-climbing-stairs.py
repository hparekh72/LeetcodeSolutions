class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1 for _ in range(n + 1)]
        return self.solveUsingMemoization(n, dp)

    
    # TC: O(n) 
    # SC: O(n) (dp array and recursion stack space)
    def solveUsingMemoization(self, n, dp):
        if n <= 1:
            return 1
        
        if dp[n] != -1:
            return dp[n]

        dp[n] = self.solveUsingMemoization(n - 1, dp) + self.solveUsingMemoization(n - 2, dp)
        return dp[n]





