# Note for me:
# 1) DSU extra edge of same component ko ignore karta hai
# 2) DSU minimum edge ka connected graph hota hai ( for visualization )
# 3) component of graph ki bat ho rahi think of DSU once


# Approach: Using Disjoint Set

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

# TC: O(N)+ O(4α) + O(E) (total connection) + O(N), here α = constant
# SC: O(N) (parent, size, rank array) 
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        ds = DisjointSet(n)

        extraCables = 0
        for edge in connections:
            u = edge[0]
            v = edge[1]
            if ds.findUltimateParent(u) == ds.findUltimateParent(v):
                extraCables += 1
            else:
                ds.unionBySize(u, v)

# Calculate the nodes whose ultimate parent is itself to calculate the number of connections pending (basically count the number of unique parents)
        cablesNeeded = 0
        for i in range(n):
            if ds.parent[i] == i: 
                cablesNeeded += 1
        
        # -1 because one node parent will be an ultimate parent to form a connection
        res = cablesNeeded - 1

        # If we have enough cables, then network connection is possible
        if res <= extraCables:
            return res
        else:
            return -1


        


