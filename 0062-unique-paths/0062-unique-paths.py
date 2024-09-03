class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # return self.solveUsingRecursion(0, 0, m, n)

        dp = [[-1 for _ in range(n)] for _ in range(m)]
        
        return self.solveUsingMemoization(0, 0, m, n, dp)


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
