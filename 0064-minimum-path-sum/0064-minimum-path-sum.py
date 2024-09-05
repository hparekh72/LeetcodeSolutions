class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # return self.solveUsingRecursion(m - 1, n - 1, m , n, grid)

        dp = [[-1 for _ in range(n)] for _ in range(m)]

        # return self.solveUsingMemoization(m - 1, n - 1, m , n, grid, dp)
        # return self.solveUsingTabulation(m , n, grid, dp)
        return self.solveUsingSpaceOptimization(m, n, grid)


    # TC: O(2^(m * n))
    # SC: O(m + n) (recursion. stack space)
    def solveUsingRecursion(self, r, c, m, n, grid):
        # Base Case
        if r < 0 or c < 0: # Boundary condition
            return float('inf')

        if r == 0 and c == 0: 
            return grid[0][0] # As this position will be a part of my path
        
        left = grid[r][c] + self.solveUsingRecursion(r, c - 1, m, n, grid)
        up = grid[r][c] + self.solveUsingRecursion(r - 1, c, m, n, grid)

        return min(left, up)

    # TC: O(m * n)
    # SC: O(m * n) (dp array) + O(m + n) (recursion stack space)
    def solveUsingMemoization(self, r, c, m, n, grid, dp):
        # Base Case
        if r < 0 or c < 0: # Boundary condition
            return float('inf')

        if r == 0 and c == 0: 
            return grid[0][0] # As this position will be a part of my path

        if dp[r][c] != -1:
            return dp[r][c]


        left = grid[r][c] + self.solveUsingMemoization(r, c - 1, m, n, grid, dp)
        up = grid[r][c] + self.solveUsingMemoization(r - 1, c, m, n, grid, dp)

        dp[r][c] = min(left, up)
        return dp[r][c]


    # TC: O(m * n)
    # SC: O(m * n) (dp array) 

    def solveUsingTabulation(self, m, n, grid, dp):

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    dp[r][c] = grid[r][c]
                else:
                    left, up = float('inf'), float('inf')
                    if c > 0:
                        left = grid[r][c] + dp[r][c - 1]
                    if r > 0:
                        up = grid[r][c] + dp[r - 1][c]

                    dp[r][c] = min(left, up)

        return dp[m - 1][n - 1]


    # TC: O(m * n)
    # SC: O(n) (prevRow and currRow array) 

    def solveUsingSpaceOptimization(self, m, n, grid):
        prevRow = [-1] * n
        for r in range(m):
            currRow = [-1] * n
            for c in range(n):
                if r == 0 and c == 0:
                    currRow[c] = grid[r][c]
                else:
                    left, up = float('inf'), float('inf')
                    if c > 0:
                        left = grid[r][c] + currRow[c - 1]
                    if r > 0:
                        up = grid[r][c] + prevRow[c]

                    currRow[c] = min(left, up)
            prevRow = currRow

        return prevRow[n - 1] # Can also use currRow



                



        