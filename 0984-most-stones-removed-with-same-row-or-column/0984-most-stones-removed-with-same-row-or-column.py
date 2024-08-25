# Approach 1: Using DFS
# Intution: 
# The core idea of this solution is to treat each stone as a node in a graph, with edges connecting nodes if they share the same row or column.
# This transforms the problem into one of finding connected components in the graph. Each connected component represents a cluster of stones that are interconnected through shared rows or columns. 
# The key insight from this approach is that within each connected component, all stones except one can potentially be removed. Therefore, the maximum number of stones that can be removed is determined by subtracting the number of these connected components from the total number of stones. 
# This method highlights the application of graph theory to efficiently solve complex problems by abstracting them into a form where standard algorithms (like DFS for finding connected components) can be applied.


# TC: O(n ^ 2) + (V + E)
# SC: O(n ^ 2) + O(n) (visited array)

# class Solution:

#     def dfs(self, src, adjList, visited):
#         visited.add(src)

#         for neighbor in adjList[src]:
#             if neighbor not in visited:
#                 self.dfs(neighbor, adjList, visited)

#     def removeStones(self, stones: List[List[int]]) -> int:

#         # Create adjacency list
#         n = len(stones)
#         adjList = defaultdict(list)

#         for i in range(n):
#             for j in range(i + 1, n):
#                 if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
#                     adjList[i].append(j)
#                     adjList[j].append(i)

#         visited = set()
#         numOfComponents = 0
#         for i in range(n):
#             if i not in visited:
#                 numOfComponents += 1
#                 self.dfs(i, adjList, visited)

#         return n - numOfComponents

# Approach 2: Using Disjoint Set

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


# TC: O(E), E -> no. of stones
# SC: O(E) (hashSet, size and parent array)

# Intuition:
# This solution treats each stone's row and column as nodes in a graph. The key insight is to connect stones that share a row or a column, effectively creating a union-find data structure (Disjoint Set) to keep track of these connections.
# Each stone is mapped to two nodes: one for its row and one for its column, effectively doubling the indexing space to separate row indices from column indices. This mapping allows merging any stones with a shared row or column into a single connected component. The number of removable stones is then the total number of stones minus the number of these connected components, since at least one stone from each component will remain.


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # Initialize the maximum row and column index
        maxRow, maxCol = 0, 0 
        # Determine the maximum indices for rows and columns
        for r, c in stones:
            maxRow = max(r, maxRow)
            maxCol = max(c, maxCol)

        # Initialize a disjoint set for union-find operations
        ds = DisjointSet(maxRow + maxCol + 1)
        hashSet = set()

        # Unite nodes based on row and column connections
        for r, c in stones:
            nodeRowNo = r
            nodeColNo = (maxRow + 1) + c
            ds.unionBySize(nodeRowNo, nodeColNo)
            hashSet.add(nodeRowNo)
            hashSet.add(nodeColNo)

        # Count the number of unique components
        numOfComponents = 0
        for nodeNo in hashSet:
            if ds.findUltimateParent(nodeNo) == nodeNo:
                numOfComponents += 1
        
        # The result is the total number of stones minus the number of unique components
        return len(stones) - numOfComponents




