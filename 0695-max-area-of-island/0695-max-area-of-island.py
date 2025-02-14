# TC: O(4 * (n * m)) ~ O(n * m)
# SC: O(n * m) (visited array and dfs recursion call stack)

# Note: Can also use count[0] = 0 and sent count in the dfs function call

class Solution:

    def dfs(self, r, c, grid, visited, rows, cols): 
        
        # Check bounds and visited status before proceeding
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r, c) in visited:
            return 0

        # Mark the current cell as visited
        visited.add((r, c))
        
        # Start count at 1 for the current cell
        count = 1

        # Directions for 4-connected components
        dRow = [-1, 1, 0, 0]
        dCol = [0, 0, -1, 1]
         
        # Recursively visit all connected land cells
        for i in range(4):
            row = r + dRow[i]
            col = c + dCol[i]
            count += self.dfs(row, col, grid, visited, rows, cols)

        return count


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        maxCount = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxCount = max(maxCount, self.dfs(r, c, grid, visited, rows, cols))
        
        return maxCount