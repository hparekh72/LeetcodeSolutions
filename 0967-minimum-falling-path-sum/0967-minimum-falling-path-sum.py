# Note: We cannot apply greedy algorithm over here, as uniformity is not their in the numbers.

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        minimumPathSum = float('inf')

        dp = [[-1 for c in range(n)] for r in range(n)]

        # for c in range(n):
            # minimumPathSum = min(minimumPathSum, self.solveUsingRecursion(n - 1, c, matrix, n))
            # minimumPathSum = min(minimumPathSum, self.solveUsingMemoization(n - 1, c, matrix, n, dp))
        
        # print(dp)
        # return minimumPathSum

        
        # return self.solveUsingTabulation(matrix, n, dp)
        return self.solveUsingSpaceOptimization(matrix, n)




    # TC: O(3 ^ (n * n))
    # SC: O(n) (recursion stack space)
    def solveUsingRecursion(self, r, c, matrix, n):

        # Base Case
        if c < 0 or c >= n: # Boundary condition check
            return float('inf')

        if r == 0:
            return matrix[r][c]

        up = matrix[r][c] + self.solveUsingRecursion(r - 1, c, matrix, n)
        upLeft = matrix[r][c] + self.solveUsingRecursion(r - 1, c - 1, matrix, n)
        upRight = matrix[r][c] + self.solveUsingRecursion(r - 1, c + 1, matrix, n)

        return min(up, upLeft, upRight)


    # TC: O(n * n)
    # SC: O(n * n) (dp array) + O(n) (recursion stack space)

    def solveUsingMemoization(self, r, c, matrix, n, dp):
        # Base Case
        if c < 0 or c >= n: # Boundary condition check
            return float('inf')

        if r == 0:
            return matrix[r][c]

        if dp[r][c] != -1:
            return dp[r][c]

        up = matrix[r][c] + self.solveUsingMemoization(r - 1, c, matrix, n, dp)
        upLeft = matrix[r][c] + self.solveUsingMemoization(r - 1, c - 1, matrix, n, dp)
        upRight = matrix[r][c] + self.solveUsingMemoization(r - 1, c + 1, matrix, n, dp)

        dp[r][c] = min(up, upLeft, upRight)
        return dp[r][c]


    # TC: O(n * n)
    # SC: O(n * n) (dp array) 

    # Note: Tabulation is the opposite of Memoization. Since in memoization we did (n - 1) -> 0, hence in tabulation we did 0 -> (n - 1)
    def solveUsingTabulation(self, matrix, n, dp): 

        for c in range(n): # Base Case of Memoization
            dp[0][c] = matrix[0][c] # When r == 0

        for r in range(1, n):
            for c in range(n):
                up = matrix[r][c] + dp[r - 1][c]

                upLeft = float('inf')
                if c > 0:
                    upLeft = matrix[r][c] + dp[r - 1][c - 1]

                upRight = float('inf')
                if c + 1 < n:
                    upRight = matrix[r][c] + dp[r - 1][c + 1]
            
                dp[r][c] = min(up, upLeft, upRight)

        # Return the minimum falling path.
        minimumPathSum = float('inf') 
        for c in range(n):
            if dp[n - 1][c] < minimumPathSum:
                minimumPathSum = dp[n - 1][c]

        return minimumPathSum



    # TC: O(n * n)
    # SC: O(n) (prevRow and currRow array) 

    def solveUsingSpaceOptimization(self, matrix, n): 

        prevRow = [-1] * n

        for c in range(n): # Base Case of Memoization
            prevRow[c] = matrix[0][c] # When r == 0

        for r in range(1, n):
            currRow = [-1] * n
            for c in range(n):
                up = matrix[r][c] + prevRow[c]

                upLeft = float('inf')
                if c > 0:
                    upLeft = matrix[r][c] + prevRow[c - 1]

                upRight = float('inf')
                if c + 1 < n:
                    upRight = matrix[r][c] + prevRow[c + 1]
            
                currRow[c] = min(up, upLeft, upRight)

            prevRow = currRow

        # Return the minimum falling path.
        minimumPathSum = min(prevRow)

        return minimumPathSum





   




        