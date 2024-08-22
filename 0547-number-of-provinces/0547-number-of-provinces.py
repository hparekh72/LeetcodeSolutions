# Approach 1: Using BFS or DFS traversal
# TC: O(N) + O(V + 2E) ~ O(N)
# SC: O(N) + O(N) (recursive stack space) ~ O(N)
# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         visited = set()
#         numOfProvinces = 0
#         for start_vertex in range(len(isConnected)):
#             if start_vertex not in visited:
#                 numOfProvinces += 1
#                 self.dfs(start_vertex, isConnected, visited)
        
#         return numOfProvinces
                


#     def dfs(self, start_vertex, isConnected, visited):
#         visited.add(start_vertex)

#         for adjacent_vertex in range(len(isConnected)):
#             if isConnected[start_vertex][adjacent_vertex] == 1 and adjacent_vertex not in visited:
#                 self.dfs(adjacent_vertex, isConnected, visited)
        
# Approach 2: Using Disjoint Set

# Disjoint Set Time and Space Complexity
# TC: O(N) + O(4α), here α = constant
# SC: O(N) (parent, size, rank array) 
class DisjointSet:
    def __init__(self, n): # TC: O(N)
        self.rank = [0] * (n + 1) # Can be used for 0-based and 1-based indexing 
        self.size = [1] * (n + 1)
        self.parent = [i for i in range(n+1)] 
        
    def findUltimateParent(self, node): # TC: O(4α)
        # Base Case
        if self.parent[node] == node:
            return node
            
        self.parent[node] = self.findUltimateParent(self.parent[node])
        return self.parent[node]
        
    def unionByRank(self, u, v): # TC: O(4α)
        ulp_u = self.findUltimateParent(u)
        ulp_v = self.findUltimateParent(v)

        if (ulp_u == ulp_v):
            return
        
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_u] > self.rank[ulp_v]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1
            
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

# TC: O(N ^ 2) + O(N) + O(4α), here α = constant
# SC: O(N) (parent, size, rank array) 
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)

        ds = DisjointSet(n)

        for i in range(n): # TC: O(N ^ 2)
            for j in range(n):
                if isConnected[i][j] == 1: # ie. there is an edge between i and j
                    ds.unionBySize(i, j)

# Calculate the nodes whose ultimate parent is itself to calculate the number of provinces(basically count the number of unique parents)
        numOfProvinces = 0 
        for i in range(n):
            if ds.parent[i] == i: 
                numOfProvinces += 1
        
        return numOfProvinces


        
        


            


