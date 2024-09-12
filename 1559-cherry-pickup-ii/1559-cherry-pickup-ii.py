class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dp = [[[-1 for _ in range(cols)] for _ in range(cols)] for _ in range(rows)]

        # return self.solveUsingRecursion(0, 0, cols - 1, rows, cols, grid) 
        # return self.solveUsingMemoization(0, 0, cols - 1, rows, cols, grid, dp) 
        return self.solveUsingTabulation(rows, cols, grid, dp)
    

    # TC: O(3^n * 3^n)
    # SC: O(n) + O(n) ~ O(n) (recursion stack space)

    # Here row (r) is common between the robots as both will be moving at the same time
    # (r, c1) -> Robot 1
    # (r, c2) -> Robot 2
    def solveUsingRecursion(self, r, c1, c2, rows, cols, grid):
        # Base Case
        if c1 < 0 or c1 >= cols or c2 < 0 or c2 >= cols:    # Boundary check
            return float('-inf')

        if r == rows - 1:
            # If both robots are on the same cell
            if c1 == c2:
                return grid[r][c1]
            else:
                return grid[r][c1] + grid[r][c2]

        # Explore all paths of Robot1 and Robot2 simultaneously
        
        maxCherries = float('-inf')
        for dr1 in range(-1, 2):
            for dr2 in range(-1, 2):
                value = 0
                if c1 == c2:
                    value = grid[r][c1]
                else:
                    value = grid[r][c1] + grid[r][c2]

                value += self.solveUsingRecursion(r + 1, c1 + dr1, c2 + dr2, rows, cols, grid)
                maxCherries = max(maxCherries,  value)

        return maxCherries


    # TC: O(rows * cols * cols)
    # SC: O(rows * cols * cols) + O(cols) + O(cols) (recursion stack space) ~ O(rows * cols * cols) 
    def solveUsingMemoization(self, r, c1, c2, rows, cols, grid, dp):
        # Base Case:
        if c1 < 0 or c1 >= cols or c2 < 0 or c2 >= cols: # Boundary conditions
            return float('-inf')

        if r == rows - 1:
            # If both robots are on the same cell
            if c1 == c2:
                return grid[r][c1]
            else:
                return grid[r][c1] + grid[r][c2]

        if dp[r][c1][c2] != -1:
            return dp[r][c1][c2]


        # Explore all paths of Robot1 and Robot2 simultaneously
        maxCherries = float('-inf')
        for dr1 in range(-1, 2):
            for dr2 in range(-1, 2):
                value = 0
                if c1 == c2:
                    value = grid[r][c1]
                else:
                    value = grid[r][c1] + grid[r][c2]
                
                value += self.solveUsingMemoization(r + 1, c1 + dr1, c2 + dr2, rows, cols, grid, dp)
                maxCherries = max(maxCherries, value)
        
        dp[r][c1][c2] = maxCherries
        return dp[r][c1][c2]

    # TC: O(rows * cols * cols)
    # SC: O(rows * cols * cols) 

    def solveUsingTabulation(self, rows, cols, grid, dp):

        # Base Case
        for c1 in range(cols):
            for c2 in range(cols):
                # If both robots are on the same cell
                if c1 == c2:
                    dp[rows - 1][c1][c2] = grid[rows - 1][c1]
                else:
                    dp[rows - 1][c1][c2] = grid[rows - 1][c1] + grid[rows - 1][c2]

        for r in range(rows - 2, -1, -1):
            for c1 in range(cols):
                for c2 in range(cols):
                    # Explore all paths of Robot1 and Robot2 simultaneously
                    maxCherries = float('-inf')
                    for dr1 in range(-1, 2):
                        for dr2 in range(-1, 2):
                            value = 0
                            if c1 == c2:
                                value = grid[r][c1]
                            else:
                                value = grid[r][c1] + grid[r][c2]
                            
                            if c1 + dr1 >= 0 and c1 + dr1 < cols and c2 + dr2 >= 0 and c2 + dr2 < cols:
                                value += dp[r + 1][c1 + dr1][c2 + dr2] 
                            else:
                                value += float('-inf')

                            maxCherries = max(maxCherries, value)
                    dp[r][c1][c2] = maxCherries

        return dp[0][0][cols - 1]

                            


    

        

            
    





        

        
            