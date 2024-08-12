# TC: O(4 * m * n) + O(m * n) + O(n) + O(m) ~ O(m * n)
# SC: O(m * n) (visited array) + O(m * n) (dfs recursion stack space) ~ O(m * n)


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        # Traverse the first and last row
        for i in range(cols):
            # First row
            if grid[0][i] == 1 and visited[0][i] == 0:
                self.dfs(0, i, grid, visited)

            # Last row
            if grid[rows - 1][i] == 1 and visited[rows - 1][i] == 0:
                self.dfs(rows - 1, i, grid, visited)

        # Traverse the first and last column
        for i in range(rows):
            # First column
            if grid[i][0] == 1 and visited[i][0] == 0:
                self.dfs(i, 0, grid, visited)

            # Last column
            if grid[i][cols - 1] == 1 and visited[i][cols - 1] == 0:
                self.dfs(i, cols - 1, grid, visited)

        res = 0
        # Traverse the grid except the boundaries
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 1 and visited[r][c] == 0:
                    res += 1

        return res
        
    def dfs(self, r, c, grid, visited): # TC: O(4 * m * n)
        # Base Condition
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0 or visited[r][c] == 1:
            return
        
        visited[r][c] = 1

        self.dfs(r - 1, c, grid, visited) # Up
        self.dfs(r + 1, c, grid, visited) # Down
        self.dfs(r, c - 1, grid, visited) # Left
        self.dfs(r, c + 1, grid, visited) # Right







        