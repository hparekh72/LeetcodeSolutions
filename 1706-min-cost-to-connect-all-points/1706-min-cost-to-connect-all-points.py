# Prims Algorithm (Intution: Greedy approach)
# TC: O(ElogE). Here E represents no. of edges which is n^2 in worst case. ie. O(n^2(logn))
# SC: O(n^2) (For adjacency list and minHeap) + O(n) (visited array) ~ O(n^2)


# class Solution:

#     def manhattanDistance(self, x1, y1, x2, y2):
#         return abs(x1 - x2) + abs(y1 - y2)

#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         n = len(points)

#         # Create Adjacency List
#         adjList = {i:[] for i in range(n)} # i: list of [cost, node]
#         for i in range(n):
#             x1, y1, = points[i]
#             for j in range(i + 1, n):
#                 x2, y2 = points[j]
#                 cost = self.manhattanDistance(x1, y1, x2, y2)
#                 adjList[i].append([cost, j])
#                 adjList[j].append([cost, i])

#         # Prim's Algorithm
#         visited = set()

#         minHeap = []
#         heapq.heappush(minHeap, [0, 0])

#         minCost = 0
#         while minHeap:
#             cost, node = heapq.heappop(minHeap)
#             if node in visited:
#                 continue
            
#             visited.add(node)
#             minCost += cost

#             for neighborCost, neighbor in adjList[node]:
#                 if neighbor not in visited:
#                     heapq.heappush(minHeap, [neighborCost, neighbor])
        
#         return minCost


# Approach 2: Using Disjoint Set (Kruskal's Algorithm)

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
        


# Kruskals Algorithm (Intution: Greedy approach)
# TC: O(n^2(logn)) (sorting)
# SC: O(n^2) (For edges list) + O(n) (parent and size array of Disjoint Set) ~ O(n^2)


class Solution:

    def manhattanDistance(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # List to hold all edges in the form (cost, start_point, end_point)
        edges = []
        for i in range(n):
            x1, y1, = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                cost = self.manhattanDistance(x1, y1, x2, y2)
                edges.append((cost, i, j))

        # Kruskal's Algorithm

        ds = DisjointSet(n)

        # Sort all edges by cost
        edges.sort()  # Sorts based on the first element of the tuple by default

        minCost, connections = 0, 0
        for cost, u, v in edges:
            if ds.findUltimateParent(u) != ds.findUltimateParent(v):
                ds.unionBySize(u, v)
                minCost += cost
                connections += 1

                if connections == n - 1:
                    break
        
        return minCost
                








        

            

