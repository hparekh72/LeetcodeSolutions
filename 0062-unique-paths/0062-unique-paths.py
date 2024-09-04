class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # return self.solveUsingRecursion(0, 0, m, n)

        dp = [[-1 for _ in range(n)] for _ in range(m)]
        
        # return self.solveUsingMemoization(0, 0, m, n, dp)
        # return self.solveUsingMemoization2(m - 1, n - 1, m, n, dp)
        return self.solveUsingTabulation(m, n, dp)

    # TC: 2^(m * n)
    # SC: O(m + n) (recussion stack space)
    def solveUsingRecursion(self, r, c, m, n):
        
        # Boundary Condition
        if r < 0 or r >= m or c < 0 or c >= n:
            return 0

        # Base Cases
        if r == m - 1 and c == n - 1:
            return 1

        down = self.solveUsingRecursion(r + 1, c, m, n)
        right = self.solveUsingRecursion(r, c + 1, m, n)

        return down + right
    

    # Memoization Approach 1
    # TC: O(m * n)
    # SC: O(m * n) (dp array) + O(m + n) (recursion stack space)
    def solveUsingMemoization(self, r, c, m, n, dp):
        # Boundary Condition
        if r < 0 or r >= m or c < 0 or c >= n:
            return 0

        # Base Cases
        if r == m - 1 and c == n - 1:
            return 1

        if dp[r][c] != -1:
            return dp[r][c]

        down = self.solveUsingMemoization(r + 1, c, m, n, dp)
        right = self.solveUsingMemoization(r, c + 1, m, n, dp)

        dp[r][c] = down + right
        return dp[r][c]


    # Memoization Approach 2
    # TC: O(m * n)
    # SC: O(m * n) (dp array) + O(m + n) (recursion stack space)

    def solveUsingMemoization2(self, r, c, m, n, dp):
        # Base Case
        if r < 0 or c < 0: # Boundary condition
            return 0

        if r == 0 and c == 0:
            return 1

        if dp[r][c] != -1:
            return dp[r][c]

        up = self.solveUsingMemoization2(r - 1, c, m, n, dp)
        left = self.solveUsingMemoization2(r, c - 1, m, n, dp)

        dp[r][c] = up + left
        
        return dp[r][c]

    # Tabulation
    # TC: O(m * n)
    # SC: O(m * n) (dp array) 

    def solveUsingTabulation(self, m, n, dp):
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    dp[r][c] = 1
                else:
                    up, left = 0, 0
                    if r > 0:
                        up = dp[r - 1][c]
                    
                    if c > 0:
                        left = dp[r][c - 1]

                    dp[r][c] = up + left

        return dp[m - 1][n - 1]



    





