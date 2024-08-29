# Approach 1: Multiple DFS Traversals
# 1) Construct graph by adding edges one after the another.
# 2) After each addition of a new edge, we will do a dfs traversal to check if any cycle has formed.  
# 3) If a cycle is detected, we know that the last edge addition has led to the formation of cycle and hence we will simply return that edge.

# TC: O(n ^ 2)
# SC: o(n)


# Approach 2: Using Disjoint Set

# Note: Disjoint Set is used in Dynamic Graphs, where we are needed some connections or merging between the nodes

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


# Intution:
# We are given various edges of the graph. These can be consider as different disconnected components. We will join these one by one. A component will be represented as a tree with all its members linked to some parent and the top parent will be considered that component's representative. When we find an edge that joins two nodes which are already in the same component, we will return that edge as answer. Otherwise, we will just Union it, i.e, connect the two components by picking that edge.

# TC: O(n) (size and parent array initilization in disjoint set) + O(n) (iterating over edges) ~ O(n)
# SC: O(n) (size and parent array in disjoint set)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        ds = DisjointSet(n)

        for u, v in edges:
            if ds.findUltimateParent(u) != ds.findUltimateParent(v):
                ds.unionBySize(u, v)
            else:
                return [u, v]



        