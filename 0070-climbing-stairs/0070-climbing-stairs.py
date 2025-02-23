class Solution:
    # def climbStairs(self, n: int) -> int: # Recursion

    #     # TC: O(2^n)
    #     # SC: O(n)
        
    #     # Base Case 
    #     if n < 0:
    #         return 0

    #     if n == 0:
    #         return 1 

    #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        def climbStairs(self, n: int) -> int: # Memoization
            dp = [-1 for _ in range(n + 1)]
            return self.solveUsingMemoization(n, dp)

        def solveUsingMemoization(self, n, dp):
            if n < 0:
                return 0

            if n == 0:
                return 1
            
            if dp[n] != -1:
                return dp[n]

            dp[n] = self.solveUsingMemoization(n - 1, dp) + self.solveUsingMemoization(n - 2, dp)
            return dp[n]

        

        





 
            








