class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        # return self.solveUsingRecursion(0, 0, m, triangle)

        dp = [[-1 for _ in range(m)] for _ in range(m)]

        # return self.solveUsingMemoization(0, 0, m, triangle, dp)
        return self.solveUsingTabulation(m, triangle, dp)
        

    # TC: O(2^(m * m))
    # SC: O(m) (recursion. stack space)

    def solveUsingRecursion(self, r, c, m, triangle):
        # Base Case
        if r == m - 1:
            return triangle[r][c]

        down = triangle[r][c] + self.solveUsingRecursion(r + 1, c, m, triangle)
        downRight = triangle[r][c] + self.solveUsingRecursion(r + 1, c + 1, m, triangle)

        return min(down, downRight)


    # TC: O(m * m)
    # SC: O(m * m) (dp array) + O(m) (recursion stack space)
    def solveUsingMemoization(self, r, c, m, triangle, dp):
        # Base Case
        if r == m - 1:
            return triangle[r][c]

        if dp[r][c] != -1:
            return dp[r][c]

        down = triangle[r][c] + self.solveUsingMemoization(r + 1, c, m, triangle, dp)
        downRight = triangle[r][c] + self.solveUsingMemoization(r + 1, c + 1, m, triangle, dp)

        dp[r][c] = min(down, downRight)
        return dp[r][c]

    # Note: No of columns in each row = row number. Eg: 3rd row (0-based indexing) = 0, 1, 2, 3 columns
    
    # TC: O(m * m)
    # SC: O(m * m)
    def solveUsingTabulation(self, m, triangle, dp):
        # (Base Case) Using the base case of memoization
        for c in range(m):
            dp[m - 1][c] = triangle[m - 1][c]

        for r in range(m - 2, -1, -1):
            for c in range(r, -1, -1):
                down = triangle[r][c] + dp[r + 1][c] 
                downRight = triangle[r][c] + dp[r + 1][c + 1] 

                dp[r][c] = min(down, downRight)
        
        return dp[0][0]
   

        



        

        

        


        