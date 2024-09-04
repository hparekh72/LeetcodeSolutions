class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m  = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # return self.solveUsingRecursion(m - 1, n - 1, m, n, obstacleGrid)

        dp = [[-1 for _ in range(n)] for _ in range(m)]

        return self.solveUsingMemoization(m - 1, n - 1, m, n, obstacleGrid, dp)


    # TC: 2^(m * n)
    # SC: O(m + n) (recussion stack space)

    def solveUsingRecursion(self, r, c, m, n, obstacleGrid):

        # Base Case
        
        if r < 0 or c < 0 or obstacleGrid[r][c] == 1: # Boundaries and obstacle check
            return 0

        if r == 0 and c == 0:
            return 1
        

        up = self.solveUsingRecursion(r - 1, c, m, n, obstacleGrid)
        left = self.solveUsingRecursion(r, c - 1, m, n, obstacleGrid)

        return up + left

    # TC: O(m * n)
    # SC: O(m * n) (dp array) + O(m + n) (recursion stack space)
    def solveUsingMemoization(self, r, c, m, n, obstacleGrid, dp):

        # Base Case

        if r < 0 or c < 0 or obstacleGrid[r][c] == 1: # Boundaries and obstacle check
            return 0

        if r == 0 and c == 0:
            return 1


        if dp[r][c] != -1:
            return dp[r][c]

        up = self.solveUsingMemoization(r - 1, c, m, n, obstacleGrid, dp)
        left = self.solveUsingMemoization(r, c - 1, m, n, obstacleGrid, dp)

        dp[r][c] = up + left
        return dp[r][c]



        


        