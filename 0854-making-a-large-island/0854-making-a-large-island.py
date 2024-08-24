# Disjoint Set Time and Space Complexity
# TC: O(N) + O(4α), here α = constant
# SC: O(N) (parent, size, rank array) 

class DisjointSet:
    def __init__(self, n): # TC: O(N)
        # self.rank = [0] * (n + 1) # Can be used for 0-based and 1-based indexing 
        self.size = [1] * (n + 1)
        self.parent = [i for i in range(n+1)] 
        
    def findUltimateParent(self, node): # TC: O(4α)
        # Base Case
        if self.parent[node] == node:
            return node
            
        self.parent[node] = self.findUltimateParent(self.parent[node])
        return self.parent[node]
        
    # def unionByRank(self, u, v): # TC: O(4α)
    #     ulp_u = self.findUltimateParent(u)
    #     ulp_v = self.findUltimateParent(v)

    #     if (ulp_u == ulp_v):
    #         return
        
    #     if self.rank[ulp_u] < self.rank[ulp_v]:
    #         self.parent[ulp_u] = ulp_v
    #     elif self.rank[ulp_u] > self.rank[ulp_v]:
    #         self.parent[ulp_v] = ulp_u
    #     else:
    #         self.parent[ulp_v] = ulp_u
    #         self.rank[ulp_u] += 1
            
    def unionBySize(self, u, v): # TC: O(4α)
        ulp_u = self.findUltimateParent(u)
        ulp_v = self.findUltimateParent(v)

        if (ulp_u == ulp_v):
            return
        
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]


# TC: O(4 * n ^ 2) ~ O(n ^ 2)
# TC: O(n ^ 2) (disjoint set size array)

class Solution:

    def _isValid(self, r, c, n):
         # Helper function to check if the indices are within the bounds of the grid.
        return r >= 0 and r < n and c >= 0 and c < n 

    def largestIsland(self, grid: List[List[int]]) -> int:
        # Step 1: Build disjoint sets for all 1's in the grid (Connecting components)

        n = len(grid)
        ds = DisjointSet(n * n)

        # 4 Directions (up, down, right, left)
        dRow = [-1, 1, 0, 0]
        dCol = [0, 0, 1, -1]

        for r in range(n): # TC: O(4 * n ^ 2)
            for c in range(n):
                if grid[r][c] == 0:
                    continue

                for i in range(4):
                    adjRow = r + dRow[i]
                    adjCol = c + dCol[i]

                    if self._isValid(adjRow, adjCol, n) and grid[adjRow][adjCol] == 1:
                        nodeNo = r * n + c
                        adjNodeNo = adjRow * n + adjCol
                        ds.unionBySize(nodeNo, adjNodeNo)

        # Step 2: Try converting each 0 to 1 and calculate the potential size of the resulting island.

        largestIslandSize = -1

        for r in range(n): # TC: O(4 * n ^ 2)
            for c in range(n):
                components = set()

                if grid[r][c] == 1:
                    continue
                
                currIslandSize = 1
                for i in range(4):
                    adjRow = r + dRow[i]
                    adjCol = c + dCol[i]

                    if self._isValid(adjRow, adjCol, n) and grid[adjRow][adjCol] == 1:
                        adjNodeNo = adjRow * n + adjCol
                        components.add(ds.findUltimateParent(adjNodeNo))

                for nodeNo in components:
                    currIslandSize += ds.size[nodeNo]
                
                largestIslandSize = max(largestIslandSize, currIslandSize)

        # Edge case: If the grid has all 1's
        if largestIslandSize == -1:
            return n * n
        else:
            return largestIslandSize

        
        
                
                

                
                







        