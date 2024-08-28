# Brute Force

# Visit each cell and do a graph traversal (bfs or dfs). If we can reach the pacific and atlantic ocean, then add the coordinate in our result.
# TC: O(m * n)^2
# SC: O(m * n)

# Optimal:
# TC: O(m * n)
# SC: O(m * n)

# Intuition:
# This algorithm leverages the DFS to traverse the matrix from the borders that touch the oceans, identifying cells from which water can flow to both the Pacific and Atlantic oceans. By starting from the ocean and moving inward, we ensure that every visited cell is accessible from at least one ocean under the condition that water can only flow from a cell to another adjacent one with equal or lower height. The intersection of sets that can reach both oceans gives the final result of coordinates where water flows to both oceans.


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacificOcean = set() # To track cells reachable from the Pacific Ocean
        atlanticOcean = set() # To track cells reachable from the Atlantic Ocean

        def dfs(r, c, visited, previousHeight):

            # Boundary check and ensure we only visit each cell if it's higher or equal to the previous one
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or heights[r][c] < previousHeight:
                return 

            visited.add((r, c))
            
            dRow = [-1, 1, 0, 0]
            dCol = [0, 0, -1, 1]
            for i in range(4):
                row = r + dRow[i]
                col = c + dCol[i]
                dfs(row, col, visited, heights[r][c])

        # Initialize DFS from the borders where the oceans touch
        for c in range(cols):
            dfs(0, c, pacificOcean, heights[0][c])  # Top row for Pacific
            dfs(rows - 1, c, atlanticOcean, heights[rows - 1][c]) # Bottom row for Atlantic

        # First and last column
        for r in range(rows):
            dfs(r, 0, pacificOcean, heights[r][0])  # Left column for Pacific
            dfs(r, cols - 1, atlanticOcean, heights[r][cols - 1]) # Right column for Atlantic

        res = []
        # Collect cells that can reach both oceans
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacificOcean and (r, c) in atlanticOcean:
                    res.append([r, c])

        return res


